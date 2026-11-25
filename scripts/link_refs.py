#!/usr/bin/env python3
"""Add PDF hyperlinks to a handout or solutions source and print the linked source.

Usage: python3 scripts/link_refs.py path/to/handout.tex > linked.tex
scripts/build.sh runs this on a temporary copy, so the .tex files in the repository stay plain.

Targets (anchors, set a little above the line so a viewer shows the whole box):
  * numbered results, from the start of a box title ("[Prop.~84 / LADR 6.24: ...]",
    "[Def.~46, 47 / ...]", "\\begin{wex}{Example 70 ...}") or from a book tag in it
    ("[Triangular matrices (Lay 3.1, Thm.~2)]", "[... (Nagle Thm.~3)]")
  * items of a labelled list "\\begin{enumerate}[label=(T\\arabic*)]" (facts T1, T2, ...)
  * problem headings at the start of a line: "\\textbf{HW10 P1. }", "\\begin{prob}\\textbf{P2.}"

  * named results: an unnumbered box's title name ("[The key formula]",
    "[LADR 8.4, 8.5: splitting off the nilpotent part]") and a bold lead-in naming a rule, formula,
    test or identity ("\\ii \\textbf{Row-vector rule}: "), and a numbered box whose name names a theorem,
    formula, method ... ("[Orthogonal decomposition theorem (Lay Thm.~8)]"); every later use of the exact name
    links to it, in the same week or (outside shortcut and trap boxes) in later weeks

  * worked methods "\\method{Method 2: ...}", cited as "Method 2" or "Method 2 of Week 7"

References that become links: "Prop.~84", "Props.~84, 85", "Def.~46", "Ex.~70", "Example 70",
"Thm.~4", "Theorem~4", "Lemma~2", "Cor.~3", facts and problems ("(T3)", "F2", "HW10 P2", "O4"),
and "Week N". Links to another PDF open it in the course website's PDF viewer at the target.

How a number is resolved depends on course.toml "numbering":
  "global"  (MATH 110) results are numbered once for the term: Prop. 84 is one statement, so a
            reference links to wherever it is stated, in this week or an earlier one.
  "chapter" (Math 54) theorems, lemmas and corollaries restart in each chapter of each book, and
            examples in each section, so "Thm. 4" is read with its chapter (and "Example 3" with
            its section): from a tag right before it ("Lay 1.4, Thm.~3", "Nagle Thm.~1",
            "Week 9, Thm.~8"), else from the current subsection title ("(Lay 6.2)") or fact tag
            ("\\tool{...} (Week 11)"), else the only one with that number in the week (and book).
            Theorems link across weeks; other kinds within the week only.
  "local"   (default) links within the week only.
A reference that cannot be resolved to exactly one target stays plain text.
Text inside math, comments, tikz pictures and section titles is never changed.
"""
import bisect
import glob
import os
import re
import sys
import tomllib
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KIND = {"prop": "prop", "props": "prop", "def": "def", "defs": "def", "ex": "ex", "exs": "ex",
        "example": "ex", "examples": "ex", "thm": "thm", "thms": "thm", "theorem": "thm",
        "theorems": "thm", "lemma": "lemma", "lemmas": "lemma", "cor": "cor", "corollary": "cor",
        "corollaries": "cor"}
# numbering = "chapter": theorems restart each chapter, examples each section (Lay, Nagle)
UNIT = {"thm": "chapter", "lemma": "chapter", "cor": "chapter", "ex": "section"}
WORD = r"(Props?\.|Defs?\.|Exs?\.|Examples?|Thms?\.|Theorems?|Lemmas?|Cor\.|Corollar(?:y|ies))"
SEP = r"(?:~|\\ | )"
LIST = r"(\d+(?:(?:,\s*(?:and\s+)?|\s+and\s+|--)\d+)*)"
REF = re.compile(WORD + SEP + LIST + r"(?![\d.]\d)")
NUM = re.compile(r"\d+")
LABEL = re.compile(r"(?<![A-Za-z\\\d])(?:HW(\d+) )?(?!HW\d)([A-Z]{1,2}\d+)(?![\dA-Za-z])")
WEEK = re.compile(r"(?<![A-Za-z])Week(?:~| )(\d+)(?!\d)")
HEADING = re.compile(r"(?m)^((?:\\begin\{prob\})?\\textbf\{)((?:HW(\d+) )?(?!HW\d)([A-Z]{1,2}\d+))(?=[ .(,])")
BOOK_TAG = re.compile(r"(Lay|Nagle)[~ ]((\d+)\.\d+)")
# a tag right before a reference: "Lay 1.4, " / "Lay 1.5 " / "Nagle " / "Week 9, "
# (also past earlier references in the same tag: "Lay 4.5, Thm.~9, Thm.~11")
QUALIFIER = re.compile(r"(?:(?P<book>Lay|Nagle)(?:[~ ](?P<section>(?P<chapter>\d+)\.\d+)(?:--\d+\.\d+)?)?"
                       r"|Week[~ ](?P<week>\d+))[,;]?[~ ]*"
                       r"(?:(?:Thms?\.|Theorems?|Lemmas?)~\d+,[~ ]*)*\(?$")
EXTERNAL = re.compile(r"(Midterm|Final|Quiz|Exam|Lay|LADR|Nagle|Section|Ch\.)[~ ]?[\d.,~ ]*$")


def kind_of(word):
    return KIND[word.rstrip(".").lower()]


# ---------------------------------------------------------------- named results
# A result without a number is cited by the name its box title or bold lead-in gives it
# ("[The key formula]", "[LADR 8.4, 8.5: splitting off the nilpotent part]", "\ii \textbf{Row-vector rule}: ...").
BOLD = re.compile(r"(?m)^[ \t]*(?:\\ii[ \t]+)?(\\textbf\{((?:[^{}]|\{[^{}]*\})*)\})")
NAME_SKIP = re.compile(r"(worked example|examples?\b|why\b|the question|steps?\b|instance|reason|hint|idea|"
                       r"problem|answer|check|note|condition|method \d|proof|case\b|part\b)", re.I)


RESULT_NAME = re.compile(r"\b(rule|formula|criterion|test|identity|inequality|theorem|lemma|principle|trick|"
                         r"process|method|law|decomposition)\b", re.I)
METHOD = re.compile(r"\\method\{Method (\d+)")
METHOD_REF = re.compile(r"(?<![\w\\{])Method (\d+)(?: of Week[~ ](\d+))?")


def name_of(text):
    """The name a box title or bold lead-in gives a result (restored text), or None."""
    t = " ".join(text.split())
    head, sep, rest = t.partition(": ")
    if sep and re.search(r"\d|LADR|Lay|Nagle", head):
        t = rest
    elif re.match(WORD + SEP + LIST, t) or re.match(r"(LADR|Lay|Nagle)\b", t):
        return None
    while True:
        u = re.sub(r"\s*\([^()]*\)$", "", t)
        u = re.sub(r",\s*(LADR|Lay|Nagle)\b[^,]*$", "", u).rstrip(" .:;,")
        if u == t:
            break
        t = u
    if NAME_SKIP.match(t):
        return None
    t = re.sub(r"^(the|a|an)\s+", "", t, flags=re.I)
    words = re.findall(r"[A-Za-z]{2,}", re.sub(r"\$[^$]*\$", " ", t))
    return t if len(words) >= 2 and len(t) <= 70 else None


def name_key(name):
    return "name-" + "-".join(re.findall(r"[a-z0-9]+", re.sub(r"\$[^$]*\$", " m ", name.lower())))[:60]


def name_pattern(name):
    """Regex for a name in shielded text (its math as placeholders), and the math it must contain."""
    rx, maths = "", []
    for part in re.split(r"(\$[^$]*\$)", name):
        if part.startswith("$"):
            rx += r"\x00(\d+)\x00"
            maths.append(" ".join(part.split()))
        elif part:
            lead = r"\s+" if part[0].isspace() else ""
            trail = r"\s+" if part[-1].isspace() else ""
            rx += lead + r"\s+".join(re.escape(w) for w in part.split()) + trail
    return re.compile(r"(?<![\w-])" + rx + r"(?![\w-])", re.I), maths


# ---------------------------------------------------------------- protected regions
class Shield:
    """Swap regions that must not be edited for placeholders, and back."""

    def __init__(self):
        self.store = []

    def put(self, text):
        self.store.append(text)
        return f"\x00{len(self.store) - 1}\x00"

    def hide(self, pattern, s, flags=0):
        return re.sub(pattern, lambda m: self.put(m.group(0)), s, flags=flags)

    def restore(self, s):
        while "\x00" in s:
            s = re.sub(r"\x00(\d+)\x00", lambda m: self.store[int(m.group(1))], s)
        return s


def shield_source(s, sh):
    s = sh.hide(r"\A.*?\\begin\{document\}", s, re.S)
    s = sh.hide(r"(?<!\\)%[^\n]*", s)
    s = sh.hide(r"\\begin\{(tikzpicture|align|equation|gather|multline|alignat|array|tabular)(\*?)\}.*?\\end\{\1\2\}",
                s, re.S)
    s = sh.hide(r"\$\$.*?\$\$", s, re.S)
    s = sh.hide(r"\\\[.*?\\\]", s, re.S)
    s = sh.hide(r"\\\(.*?\\\)", s, re.S)
    s = sh.hide(r"(?<!\\)\$(?:\\.|[^$\\])+\$", s, re.S)
    s = sh.hide(r"\\(?:sub)*section\*?\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}", s)
    s = sh.hide(r"\\(?:title|subtitle|label|ref|eqref|cref|href|url|includegraphics|hyperlink|hypertarget|input)\b\*?"
                r"(?:\[[^\]]*\])?(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}){1,2}", s)
    s = sh.hide(r"(?<=\\begin\{enumerate\})\[[^\]]*\]", s)
    return s


# ---------------------------------------------------------------- chapter context (numbering = "chapter")
def book_chapter(text):
    """{"book", "chapter", "section"} from a tag like "(Lay 6.2)"; {"week"} from "(Week 11)"; else None."""
    m = BOOK_TAG.search(text)
    if m:
        return {"book": m.group(1).lower(), "chapter": m.group(3), "section": m.group(2)}
    w = re.search(r"Week[~ ](\d+)", text)
    return {"week": int(w.group(1))} if w else None


def context_markers(s, sh):
    """Sorted (position, (book, chapter) or None) where the chapter in force changes."""
    marks, in_facts = [], False
    pattern = re.compile(r"\x00(\d+)\x00|\\tool\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}\s*\(([^()]*)\)")
    for m in pattern.finditer(s):
        if m.group(1) is not None:
            stored = sh.restore(sh.store[int(m.group(1))])
            if stored.startswith("\\section"):
                in_facts = "Facts" in stored
                marks.append((m.start(), None))
            elif stored.startswith("\\subsection"):
                marks.append((m.start(), book_chapter(stored)))
        elif in_facts:
            marks.append((m.start(), book_chapter(sh.restore(m.group(2)))))
    return marks


def context_at(marks, pos):
    i = bisect.bisect_right([p for p, _ in marks], pos) - 1
    return marks[i][1] if i >= 0 else None


# ---------------------------------------------------------------- a course and one file
class Course:
    def __init__(self, handout_dir):
        self.handout_dir = handout_dir
        self.rel = os.path.relpath(handout_dir, ROOT).replace(os.sep, "/")
        try:
            with open(os.path.join(os.path.dirname(handout_dir), "course.toml"), "rb") as fh:
                self.numbering = tomllib.load(fh).get("numbering", "local")
        except OSError:
            self.numbering = "local"
        try:
            with open(os.path.join(ROOT, "site.toml"), "rb") as fh:
                self.base = tomllib.load(fh).get("url", "").rstrip("/") + "/"
        except OSError:
            self.base = ""
        self.weeks, self._files = {}, {}
        for f in sorted(glob.glob(os.path.join(handout_dir, "*", "handout.tex"))):
            wm = re.search(r"\\title\{[^}]*Week (\d+)", open(f, encoding="utf-8").read())
            if wm:
                self.weeks[int(wm.group(1))] = os.path.basename(os.path.dirname(f))

    def viewer_url(self, folder, pdf="handout.pdf", dest=None):
        """URL of a PDF on the course website, opened in the site's PDF viewer."""
        site_path = urlparse(self.base).path
        url = f"{self.base}pdfjs/web/viewer.html?file={site_path}{self.rel}/{folder}/{pdf}"
        return url + (f"\\#nameddest={dest}" if dest else "")

    def handout(self, folder):
        """The anchors of a folder's handout.tex (cached)."""
        if folder not in self._files:
            path = os.path.join(self.handout_dir, folder, "handout.tex")
            self._files[folder] = Source(path, self, scan_only=True) if os.path.exists(path) else None
        return self._files[folder]

    def shared_names(self, exclude):
        """Names stated in other weeks' handouts (earliest week first): key -> (folder, name)."""
        found = {}
        for folder in sorted(set(self.weeks.values()) - {exclude}):
            h = self.handout(folder)
            for key in (h.shared if h else ()):
                found.setdefault(key, (folder, h.names[key]))
        return found

    def folder_defining(self, key, exclude):
        """Earliest other week whose handout states this result (numbering global or chapter)."""
        if self.numbering == "local":
            return None
        if self.numbering == "chapter" and key.split("-")[0] not in UNIT:
            return None
        for folder in sorted(set(self.weeks.values()) - {exclude}):
            h = self.handout(folder)
            if h and key in h.results:
                return folder
        return None


class Source:
    def __init__(self, path, course, scan_only=False):
        self.path = path
        self.course = course
        self.folder = os.path.basename(os.path.dirname(path))
        self.is_solutions = os.path.basename(path) != "handout.tex"
        self.sh = Shield()
        self.text = shield_source(open(path, encoding="utf-8").read(), self.sh)
        self.results, self.facts, self.problems = set(), set(), set()
        self.aliases = {}          # "P1" -> {"prob-HW10-P1"}
        self.names, self.shared = {}, set()   # name key -> name; keys other weeks may link to
        self.methods = set()                  # "method-2" for \method{Method 2: ...}
        self.week_handout = None
        self._scan()
        self.methods = self._method_keys(self.text)
        if not scan_only and self.is_solutions:
            self.week_handout = course.handout(self.folder)

    # -- result keys a box title states
    def title_keys(self, title, env, pos, marks):
        if env == "wex":
            m = re.match(r"\s*" + WORD + SEP + LIST, title)
        else:
            m = re.match(r"\s*" + WORD + SEP + LIST, title) or \
                re.search(r"\((?:Lay|Nagle)[^()]*?(?<!after )(?<!before )(?<!of )" + WORD + SEP + LIST, title)
        if not m:
            return [], None
        kind = kind_of(m.group(1))
        nums = NUM.findall(m.group(2))
        if self.course.numbering == "chapter" and kind in UNIT:
            where = self.place(kind, title[:m.start(1)], pos, marks)
            if not where.get("unit"):
                return [], (m.start(1), m.end(2))
            keys = [f"{kind}-{where['book']}-{where['unit']}-{n}" for n in nums]
        else:
            keys = [f"{kind}-{n}" for n in nums]
        return keys, (m.start(1), m.end(2))

    @staticmethod
    def place(kind, before, pos, marks):
        """Where a chapter-numbered result lives: {"book", "unit" (chapter or section), "week",
        "explicit" (the tag gave the unit)}, from a tag right before it, else from the context."""
        q = QUALIFIER.search(before[-60:])
        ctx = context_at(marks, pos) or {}
        unit = UNIT[kind]
        where = {"book": None, "unit": None, "week": ctx.get("week"), "explicit": False}
        if q and q.group("week"):
            where["week"] = int(q.group("week"))
        elif q:
            where["book"] = q.group("book").lower()
            if q.group(unit):
                where.update(unit=q.group(unit), explicit=True)
        if "book" in ctx and where["week"] is None:
            if where["book"] is None:
                where["book"] = ctx["book"]
            if where["book"] == ctx["book"] and where["unit"] is None:
                where["unit"] = ctx[unit]
        return where

    def _boxes(self, s):
        for m in re.finditer(r"(\\begin\{(\w+)\*?\}\[)([^\]\n]*)(\])", s):
            # an option list ([style=...], [label=...]) is not a title
            if m.group(2) not in ("enumerate", "itemize") and not re.match(r"\s*[\w-]+\s*=", m.group(3)):
                yield m, m.group(3), m.group(2)
        for m in re.finditer(r"(\\begin\{wex\}\{)([^\n]*)()", s):
            yield m, m.group(2), "wex"

    def _scan(self):
        """Find every anchor; a result stated by two boxes of this file is ambiguous and dropped."""
        marks = context_markers(self.text, self.sh)
        seen = {}
        for m, title, env in self._boxes(self.text):
            for k in self.title_keys(title, env, m.start(), marks)[0]:
                seen[k] = seen.get(k, 0) + 1
        # Two boxes with one key state parts of one result (Lay 5.3 Thm. 7 in two boxes), unless the
        # number alone does not identify the result (local numbering, or Lay's per-section examples).
        def identifies(k):
            return self.course.numbering == "global" or (
                self.course.numbering == "chapter" and k.split("-")[0] in UNIT)
        self.results = {k for k, c in seen.items() if c == 1 or identifies(k)}
        self.ambiguous = {k for k, c in seen.items() if c > 1 and not identifies(k)}
        for _, letter, count in self._fact_items(self.text):
            self.facts.add(f"fact-{letter}{count}")
        for m in HEADING.finditer(self.text):
            key = self._problem_key(m)
            self.problems.add(key)
            if m.group(3):
                self.aliases.setdefault(m.group(4), set()).add(key)
        local_only = [(m.start(), m.end()) for m in
                      re.finditer(r"\\begin\{(shortcuts|trapbox)\}.*?\\end\{\1\}", self.text, re.S)]
        # names only for results without a number (a numbered one is cited by its number), and for
        # bold lead-ins that name a rule, formula, test, identity ...
        # (a numbered box's name too when it names a theorem, formula, method ...)
        named = [(m.start(), title) for m, title, env in self._boxes(self.text)
                 if env != "wex" and (self.title_keys(title, env, m.start(), marks)[1] is None
                                      or RESULT_NAME.search(name_of(self.sh.restore(title)) or ""))]
        named += [(m.start(), m.group(2)) for m in BOLD.finditer(self.text)
                  if RESULT_NAME.search(name_of(self.sh.restore(m.group(2))) or "")]
        # every name a title or bold lead-in gives (scripts/check_handout.py accepts these as citations)
        self.all_names = {n for n in (name_of(self.sh.restore(t)) for _, t, e in self._boxes(self.text) if e != "wex") if n}
        self.all_names |= {n for n in (name_of(self.sh.restore(m.group(2))) for m in BOLD.finditer(self.text)) if n}
        for pos, text in sorted(named):
            name = name_of(self.sh.restore(text))
            if name and name_key(name) not in self.names:
                self.names[name_key(name)] = name
                if not any(a <= pos < b for a, b in local_only):
                    self.shared.add(name_key(name))

    @staticmethod
    def _method_keys(s):
        return {f"method-{m.group(1)}" for m in METHOD.finditer(s)}

    @staticmethod
    def _problem_key(m):
        return f"prob-HW{m.group(3)}-{m.group(4)}" if m.group(3) else f"prob-{m.group(4)}"

    def _fact_items(self, s):
        """(position just after \\ii, letter, item number) for labelled lists like (T1), (T2)."""
        # items of nested lists (enumerate, itemize, steps, ...) are not facts
        tok = re.compile(r"\\begin\{(?:enumerate|itemize|steps|description)\}|\\end\{(?:enumerate|itemize|steps|description)\}"
                         r"|\\(?:ii|item)(?![A-Za-z])")
        for m in re.finditer(r"\\begin\{enumerate\}(\x00\d+\x00)", s):
            opt = self.sh.restore(m.group(1))
            lm = re.search(r"label=\(?([A-Z]{1,2})\\arabic\*\)?", opt)
            if not lm:
                continue
            st = re.search(r"start=(\d+)", opt)
            count, depth = (int(st.group(1)) - 1 if st else 0), 0
            for t in tok.finditer(s, m.end()):
                w = t.group(0)
                if w.startswith("\\begin"):
                    depth += 1
                elif w.startswith("\\end"):
                    if depth == 0:
                        break
                    depth -= 1
                elif depth == 0:
                    count += 1
                    yield t.end(), lm.group(1), count

    # -- writing the linked source
    def anchor(self, key):
        # \linktarget (templates/handout.sty) sits two lines up, so a viewer shows the top of the box
        return self.sh.put(f"\\linktarget{{{key}}}")

    def add_anchors(self):
        s, sh, placed = self.text, self.sh, set()
        marks = context_markers(s, sh)

        def titled(m, title, env):
            keys, span = self.title_keys(title, env, m.start(), marks)
            name = name_of(sh.restore(title)) if env != "wex" else None
            if name and name_key(name) in self.names:
                keys.append(name_key(name))
            keys = [k for k in keys if (k in self.results or k in self.names) and k not in placed]
            placed.update(keys)
            if span is None:
                new = "".join(self.anchor(k) for k in keys) + title
            else:
                a, b = span
                new = "".join(self.anchor(k) for k in keys) + title[:a] + sh.put(title[a:b]) + title[b:]
            return m.group(1) + new + (m.group(4) if env != "wex" else "")

        out, last = [], 0
        for m, title, env in sorted(self._boxes(s), key=lambda x: x[0].start()):
            out.append(s[last:m.start()] + titled(m, title, env))
            last = m.end()
        s = "".join(out) + s[last:]

        out, last = [], 0
        for pos, letter, count in self._fact_items(s):
            out.append(s[last:pos] + self.anchor(f"fact-{letter}{count}"))
            last = pos
        s = "".join(out) + s[last:]

        handout = self.week_handout

        def head(m):
            key = self._problem_key(m)
            if key in placed:
                return m.group(0)
            placed.add(key)
            text = m.group(2)
            if handout and key in handout.problems:
                url = self.course.viewer_url(self.folder, dest=key)
                text = sh.put(f"\\protect\\href{{{url}}}{{{text}}}")
            else:
                text = sh.put(text)
            return m.group(1) + self.anchor(key) + text

        s = HEADING.sub(head, s)

        def bold(m):
            name = name_of(sh.restore(m.group(2)))
            key = name_key(name) if name else None
            if key not in self.names or key in placed:
                return m.group(0)
            placed.add(key)
            return m.group(0)[:m.start(1) - m.start(0)] + self.anchor(key) + m.group(1)

        s = BOLD.sub(bold, s)

        def method(m):
            key = f"method-{m.group(1)}"
            if key in placed:
                return m.group(0)
            placed.add(key)
            return self.anchor(key) + m.group(0)

        self.text = METHOD.sub(method, s)

    def target(self, key):
        """LaTeX wrapper for a link to key, or None."""
        if key in self.ambiguous:
            return None
        if key in self.results or key in self.facts or key in self.problems:
            return lambda t: f"\\protect\\hyperlink{{{key}}}{{{t}}}"
        h = self.week_handout
        if h and (key in h.results or key in h.facts or key in h.problems):
            url = self.course.viewer_url(self.folder, dest=key)
            return lambda t: f"\\protect\\href{{{url}}}{{{t}}}"
        if key.startswith("name-"):
            if key in self.names:
                return lambda t: f"\\protect\\hyperlink{{{key}}}{{{t}}}"
            if h and key in h.names:
                url = self.course.viewer_url(self.folder, dest=key)
                return lambda t: f"\\protect\\href{{{url}}}{{{t}}}"
            other = self.course.shared_names(self.folder).get(key)
            if other:
                url = self.course.viewer_url(other[0], dest=key)
                return lambda t: f"\\protect\\href{{{url}}}{{{t}}}"
            return None
        if key.startswith(("fact-", "prob-")) or (h and key in h.ambiguous):
            return None
        folder = self.course.folder_defining(key, self.folder)
        if folder:
            url = self.course.viewer_url(folder, dest=key)
            return lambda t: f"\\protect\\href{{{url}}}{{{t}}}"
        return None

    def week_result(self, kind, n, week=None, book=None):
        """The only qualified key kind-<book>-<unit>-n stated in a given week (default this week)."""
        pool = set()
        if week is None:
            pool = self.results | (self.week_handout.results if self.week_handout else set())
        elif week in self.course.weeks:
            h = self.course.handout(self.course.weeks[week])
            pool = h.results if h else set()
        start = f"{kind}-{book}-" if book else f"{kind}-"
        hits = [k for k in pool if k.startswith(start) and k.endswith(f"-{n}") and k.count("-") == 3]
        return hits[0] if len(hits) == 1 else None

    def result_key(self, kind, n, before, pos, marks):
        if self.course.numbering != "chapter" or kind not in UNIT:
            return f"{kind}-{n}"
        where = self.place(kind, before, pos, marks)
        if where["book"] and where["unit"]:
            key = f"{kind}-{where['book']}-{where['unit']}-{n}"
            if self.target(key) or where["explicit"]:
                return key
        # unit not known: the only such result in the week named (or this week), of that book
        return self.week_result(kind, n, where["week"], where["book"])

    def link_refs(self):
        s, sh = self.text, self.sh
        marks = context_markers(s, sh)

        def link(key, text):
            dest = self.target(key) if key else None
            return sh.put(dest(text)) if dest else text

        def ref(m):
            word, lst = m.group(1), m.group(2)
            kind = kind_of(word)
            before = s[max(0, m.start() - 60):m.start()]
            out, pos, first = [], 0, True
            for n in NUM.finditer(lst):
                out.append(lst[pos:n.start()])
                key = self.result_key(kind, n.group(0), before, m.start(), marks)
                if first:
                    sep = m.group(0)[len(word):m.start(2) - m.start(0)]
                    out.append(link(key, word + sep + n.group(0)))
                    first = False
                else:
                    out.append(link(key, n.group(0)))
                pos = n.end()
            out.append(lst[pos:])
            return "".join(out)

        # named results, longest name first; never inside the title or bold lead-in that defines one
        names = dict((k, v[1]) for k, v in self.course.shared_names(self.folder).items())
        if self.week_handout:
            names.update(self.week_handout.names)
        names.update(self.names)
        for key, name in sorted(names.items(), key=lambda kv: -len(kv[1])):
            pattern, maths = name_pattern(name)

            def named(m, key=key, maths=maths):
                if [" ".join(sh.restore(sh.store[int(g)]).split()) for g in m.groups()] != maths:
                    return m.group(0)
                line = s[s.rfind("\n", 0, m.start()) + 1:m.start()]
                if re.search(r"\\begin\{\w+\*?\}[\[{][^\]]*$", line) or \
                        re.match(r"[ \t]*(?:\\ii[ \t]+)?(?:\x00\d+\x00)*\\textbf\{[^}]*$", line):
                    return m.group(0)
                return link(key, m.group(0))

            s = pattern.sub(named, s)

        def method_ref(m):
            if s[s.rfind("\n", 0, m.start()) + 1:m.start()].lstrip().startswith("\\method"):
                return m.group(0)
            key = f"method-{m.group(1)}"
            if m.group(2):
                folder = self.course.weeks.get(int(m.group(2)))
                h = self.course.handout(folder) if folder else None
                if h and key in h.methods and folder != self.folder:
                    url = self.course.viewer_url(folder, dest=key)
                    return sh.put(f"\\protect\\href{{{url}}}{{{m.group(0)}}}")
                return m.group(0)
            if key in self.methods:
                return sh.put(f"\\protect\\hyperlink{{{key}}}{{{m.group(0)}}}")
            h = self.week_handout
            if h and key in h.methods:
                url = self.course.viewer_url(self.folder, dest=key)
                return sh.put(f"\\protect\\href{{{url}}}{{{m.group(0)}}}")
            return m.group(0)

        s = METHOD_REF.sub(method_ref, s)
        s = REF.sub(ref, s)
        current = s

        def label(m):
            hw, lab = m.group(1), m.group(2)
            if EXTERNAL.search(current[max(0, m.start() - 22):m.start()]):
                return m.group(0)
            if hw:
                return link(f"prob-HW{hw}-{lab}", m.group(0))
            for key in (f"fact-{lab}", f"prob-{lab}"):
                if self.target(key):
                    return link(key, m.group(0))
            own = self.aliases.get(lab, set())
            if not own and self.week_handout:
                own = self.week_handout.aliases.get(lab, set())
            return link(next(iter(own)), m.group(0)) if len(own) == 1 else m.group(0)

        s = LABEL.sub(label, s)
        this_week = next((n for n, f in self.course.weeks.items() if f == self.folder), None)

        def week(m):
            n = int(m.group(1))
            if n == this_week or n not in self.course.weeks:
                return m.group(0)
            return sh.put(f"\\protect\\href{{{self.course.viewer_url(self.course.weeks[n])}}}{{{m.group(0)}}}")

        self.text = WEEK.sub(week, s)

    def linked(self):
        self.add_anchors()
        self.link_refs()
        return self.sh.restore(self.text)


def main(path):
    path = os.path.abspath(path)
    course = Course(os.path.dirname(os.path.dirname(path)))
    sys.stdout.write(Source(path, course).linked())


if __name__ == "__main__":
    main(sys.argv[1])
