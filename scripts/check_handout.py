#!/usr/bin/env python3
"""Layout checks for built handouts (standard: "Page-by-page visual review").

Usage: python3 scripts/check_handout.py PATH [PATH ...]
  PATH is a .tex file, a .pdf file, or a folder (every .tex and .pdf in it, recursively).
Prints one line per finding: file:page-or-line  kind  text.  Exit status 1 if anything is found.

PDF checks (the rendered page):
  heading-at-bottom   the last line of a page is a run-in heading (all bold, or ends with ':')
  idea-at-top         a page starts with an idea box, so its statement is on the previous page
  operator-at-end     a text line ends with =, +, -, <, >, so a formula was split across lines
  tall-inline         a line of running text is 21pt or taller (normal is 10-15pt; a 2x2 small
                      matrix, or a sum or integral with limits, gives 18-20pt, which is acceptable): a matrix or
                      a stack of fractions written inline (it belongs in a display)
  long-idea-box       an idea box taller than a quarter of a page. Idea boxes cannot break and stay
                      with the statement above them, so a long one leaves a blank area; keep the
                      idea in the box and move the plan of the proof or a large figure out of it
  qed-at-top          the end-of-proof box is alone at the top of a page
  line-after-display  a page starts with the one-line end of a paragraph whose display ended
                      the previous page
  blank-space         more than a third of the page is empty above the footer, and the next
                      page does not start a new section (look at it)
  label-on-line       a character is drawn on top of a stroked line or curve (a figure label
                      touching an axis, grid line, curve or edge), unless a white fill between
                      them hides the line. Radical signs are skipped (the sign meets its bar).
TeX checks (the source):
  inline-computation  an inline formula with two or more relation signs and more than about 32
                      rendered characters, or with two or more of \\frac, \\sum, \\int, \\prod
  figure-removed      the handout's folder has fewer figures than in its last committed version
                      (a rebuild must not drop a figure without a replacement)
  inline-matrix       inside $...$: a full-size matrix, an augmented matrix (\\aug), or a small
                      matrix with 3 or more rows
  inline-dfrac        \\dfrac inside $...$ (a full-size fraction in running text)
  vague-reference     a result cited so that the reader cannot find it: "the theorem above",
                      "(call this the ... rule)", "part (b) of the splitting result", or a nickname
                      such as "the restriction rule" that no box title or bold lead-in defines.
                      Cite a numbered result by its number and an unnumbered one by the exact name
                      in its box title (scripts/link_refs.py links both).
The visual review is still required; these checks find the common defects automatically.
"""
import glob, os, re, subprocess, sys
import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import link_refs

BOLD = ("CMBX", "CMSSBX", "Bold", "BX")
TEXT_FONTS = ("CMR10", "CMBX10", "CMTI10", "CMSS10")
OPERATORS = "=+−-<>≤≥·×"
PAGE_W, PAGE_H = 612, 792
IDEA_FILL = (0.943, 0.962, 0.936)     # background of \\begin{ideabox} (OliveGreen!5)
TOP, BOTTOM = 45, 755          # header rule above TOP, page number below BOTTOM


def rows(page):
    """Visual rows of a page: spans merged when their vertical ranges overlap."""
    spans = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if s["text"].strip() and TOP < s["bbox"][1] and s["bbox"][3] < BOTTOM:
                    spans.append(s)
    spans.sort(key=lambda s: s["bbox"][1])
    out = []
    for s in spans:
        y0, y1 = s["bbox"][1], s["bbox"][3]
        if out and y0 < out[-1]["y1"] - 3:
            r = out[-1]
            r["spans"].append(s); r["y0"] = min(r["y0"], y0); r["y1"] = max(r["y1"], y1)
        else:
            out.append({"spans": [s], "y0": y0, "y1": y1})
    for r in out:
        r["spans"].sort(key=lambda s: s["bbox"][0])
        r["text"] = "".join(s["text"] for s in r["spans"]).strip()
        r["x1"] = max(s["bbox"][2] for s in r["spans"])
    return out


def content_bottom(page):
    ys = [r["y1"] for r in rows(page)]
    for d in page.get_drawings():
        if d["rect"].y1 < BOTTOM and d["rect"].y0 > TOP:
            ys.append(d["rect"].y1)
    return max(ys, default=TOP)


def is_heading(row):
    text = row["text"]
    if text.endswith(":"):
        return True
    words = [s for s in row["spans"] if re.search(r"[A-Za-z]{2}", s["text"])]
    # drop a leading list label such as (T6), 1., (a)
    if words and re.fullmatch(r"\(?[A-Za-z]?\d*[a-z]?[.)]?", words[0]["text"].strip()):
        words = words[1:]
    return bool(words) and all(any(b in s["font"] for b in BOLD) for s in words) and len(text) < 70


def one_line(row):
    """True if the row's running-text spans share one baseline. A row whose text sits on
    two baselines is two text lines merged beside a display or a figure, not a tall line."""
    bases = sorted({round(s["origin"][1]) for s in row["spans"] if s["font"] in TEXT_FONTS})
    return bool(bases) and bases[-1] - bases[0] <= 3


def continues_paragraph(prev, row):
    """True if row is a continuation line: the previous row reached the right margin and
    sits directly above it (no paragraph or list spacing in between)."""
    return prev is not None and prev["x1"] > PAGE_W - 80 and row["y0"] - prev["y1"] < 3


MATH_WORDS = {"cos", "sin", "tan", "sec", "exp", "log", "det", "dim", "rank", "Span", "Nul", "Col",
              "Row", "proj", "diag", "max", "min", "lim", "for", "and", "with", "text"}


def running_text(row):
    """At least five ordinary words in the text fonts (operator names such as cos, det do not count)."""
    words = re.findall(r"[A-Za-z]{3,}", " ".join(s["text"] for s in row["spans"] if s["font"] in TEXT_FONTS))
    return len([w for w in words if w not in MATH_WORDS]) >= 5


def is_display(row, page_rows):
    """A centered row (both ends well inside the text block): a displayed formula."""
    left = min(s["bbox"][0] for r in page_rows for s in r["spans"])
    x0 = row["spans"][0]["bbox"][0]
    return x0 > left + 40 and row["x1"] < PAGE_W - left - 40


def ends_paragraph(rs):
    """The first row of a page is running text that stops short of the right margin and is
    followed by paragraph spacing (or nothing): the last line of a paragraph."""
    first = rs[0]
    if not any(s["font"] in TEXT_FONTS for s in first["spans"]) or first["x1"] > PAGE_W - 80:
        return False
    if not (len(rs) == 1 or rs[1]["y0"] - first["y1"] > 5):
        return False
    return not is_heading(first) and not any(b in first["spans"][0]["font"] for b in BOLD)


def continues_sentence(display, first):
    """The display does not end its sentence, or the next line starts in lower case."""
    return not display["text"].rstrip().endswith(".") or first["text"][:1].islower()


def _bezier(p0, p1, p2, p3, n):
    for i in range(n + 1):
        t = i / n; u = 1 - t
        yield (u**3 * p0.x + 3 * u * u * t * p1.x + 3 * u * t * t * p2.x + t**3 * p3.x,
               u**3 * p0.y + 3 * u * u * t * p1.y + 3 * u * t * t * p2.y + t**3 * p3.y)


def _samples(item, step=0.5):
    """Points every `step` pt along a line ('l') or cubic curve ('c') of a drawing."""
    if item[0] == "l":
        a, b = item[1], item[2]
        n = max(1, int(abs(b - a) / step))
        for i in range(n + 1):
            yield (a.x + (b.x - a.x) * i / n, a.y + (b.y - a.y) * i / n)
    elif item[0] == "c":
        a, b, c, d = item[1:5]
        yield from _bezier(a, b, c, d, max(2, int((abs(b - a) + abs(c - b) + abs(d - c)) / step)))


def label_on_line(page):
    """Characters drawn over a stroked line or curve that no white fill hides."""
    draws = page.get_drawings()
    strokes = [d for d in draws if d.get("color") is not None and d["type"] in ("s", "fs")
               and any(it[0] in ("l", "c") for it in d["items"])]
    if not strokes:
        return []
    whites = [(d["seqno"], d["rect"]) for d in draws
              if d.get("fill") is not None and all(c > 0.98 for c in d["fill"][:3])]
    chars = []
    for sp in page.get_texttrace():
        for ch in sp["chars"]:
            c = chr(ch[0])
            if c.isspace() or c == "\u221a":
                continue
            x0, y0, x1, y1 = ch[3]; w, h = x1 - x0, y1 - y0
            # the glyph box includes ascender and descender space: test its middle only
            r = (x0 + 0.2 * w, y0 + 0.3 * h, x1 - 0.2 * w, y1 - 0.3 * h)
            if r[2] > r[0] and r[3] > r[1]:
                chars.append((r, sp["seqno"], c))
    found = {}
    for d in strokes:
        R = d["rect"]
        near = [c for c in chars if c[1] > d["seqno"] and c[0][2] >= R.x0 - 1 and c[0][0] <= R.x1 + 1
                and c[0][3] >= R.y0 - 1 and c[0][1] <= R.y1 + 1]
        if not near:
            continue
        cover = [wr for ws, wr in whites if ws > d["seqno"]]
        for it in d["items"]:
            for x, y in _samples(it):
                for r, _, c in near:
                    if r[0] <= x <= r[2] and r[1] <= y <= r[3] and not any(
                            w.x0 <= x <= w.x1 and w.y0 <= y <= w.y1 for w in cover):
                        found.setdefault((round(x / 25), round(y / 10)), f"'{c}' at ({x:.0f},{y:.0f})")
    return list(found.values())


def check_pdf(path):
    found = []
    doc = pymupdf.open(path)
    pages = [rows(p) for p in doc]
    for i, rs in enumerate(pages):
        n = i + 1
        if not rs:
            continue
        last, first = rs[-1], rs[0]
        prev = rs[-2] if len(rs) > 1 else None
        if i < len(pages) - 1 and is_heading(last) and not continues_paragraph(prev, last):
            found.append((n, "heading-at-bottom", last["text"]))
        if i > 0 and first["text"] in ("\u25a1", "\u220e", "\u25a0"):
            found.append((n, "qed-at-top", "end-of-proof box alone at the top of the page"))
        # an idea box may start a page, unless its statement was left on the previous page
        if i > 0 and pages[i - 1] and ends_paragraph(rs) and is_display(pages[i - 1][-1], pages[i - 1]) \
                and continues_sentence(pages[i - 1][-1], first):
            found.append((n, "line-after-display", first["text"][:60]))
        statement_before = i > 0 and any(
            re.match(r"(Theorem|Proposition|Lemma|Corollary)", r["text"].replace(" ", ""))
            for r in pages[i - 1][-4:])
        if statement_before and first["text"].replace(" ", "").startswith("Theidea"):
            found.append((n, "idea-at-top", first["text"]))
        for r in rs:
            hyphenated = re.search(r"[A-Za-z]-$", r["text"])
            if running_text(r) and r["text"][-1:] in OPERATORS and not hyphenated and r["x1"] > PAGE_W - 80:
                found.append((n, "operator-at-end", r["text"][-60:]))
            if running_text(r) and one_line(r) and r["y1"] - r["y0"] > 20.5:
                found.append((n, "tall-inline", r["text"][:70]))
        for d in doc[i].get_drawings():
            fill = d.get("fill")
            if fill and all(abs(a - b) < 0.01 for a, b in zip(fill, IDEA_FILL)) and d["rect"].height > (BOTTOM - TOP) / 4:
                found.append((n, "long-idea-box", f"{d['rect'].height:.0f}pt tall"))
        for where in label_on_line(doc[i]):
            found.append((n, "label-on-line", where))
        if i < len(pages) - 1:
            gap = BOTTOM - content_bottom(doc[i])
            nxt = pages[i + 1][0]["text"] if pages[i + 1] else ""
            if gap > (BOTTOM - TOP) / 3 and not nxt.startswith("§"):
                found.append((n, "blank-space", f"{gap:.0f}pt empty; next page starts: {nxt[:40]}"))
    return found


INLINE = re.compile(r"(?<![\\$])\$([^$]+)\$(?!\$)")
RELATION = re.compile(r"=|\\le\b|\\ge\b|\\leq|\\geq|<|>|\\ne\b|\\iff|\\implies")
MATRIX = re.compile(r"(?:\\begin\{[bpvBV]?matrix\*?\}|\\begin\{array\}|\\aug\b)(?:(?!\\end).)*?\\\\", re.S)
SMALL3 = re.compile(r"\\begin\{[bpvBV]?smallmatrix\}(?:(?!\\end).)*?\\\\(?:(?!\\end).)*?\\\\", re.S)


def inline_matrix(t):
    """A full-size or augmented matrix with 2 or more rows, or a small matrix with 3 or more
    rows. (A one-row matrix reads as an ordinary list.)"""
    return bool(MATRIX.search(t) or SMALL3.search(t))


# Tall pieces: a fraction that is not two numbers, and a sum, integral or product with an upper
# limit. \\frac12 and \\sum_i a_i are normal in running text and are not counted.
TALL = re.compile(r"\\d?frac(?!\s*(?:\d|\{\d+\})\s*(?:\d|\{\d+\}))|\\(?:sum|int|prod)\s*(?:_(?:\{[^{}]*\}|\\?\w+)\s*)?\^")


def computation(t):
    """An inline formula that belongs in a display: a chain of two or more relations longer
    than 40 characters (a 2x2 small matrix counts as one symbol), or two or more tall
    pieces (sums, integrals, products, fractions that are not two numbers)."""
    short = re.sub(r"\\begin\{[bpvBV]?smallmatrix\}.*?\\end\{[bpvBV]?smallmatrix\}", "M", t, flags=re.S)
    return (len(RELATION.findall(short)) >= 2 and rendered_length(short) > 32) or len(TALL.findall(t)) >= 2


def rendered_length(t):
    """Rough number of characters the formula occupies on the page: a command such as
    \\vv, \\mathsf or \\left counts as nothing, a symbol command (\\lambda, \\cdot) as one."""
    t = re.sub(r"\\(?:vv|mathbf|mathsf|mathrm|operatorname|left|right|bigl|bigr|Bigl|Bigr|,|;|!|quad|qquad|tfrac|dfrac|frac|sqrt)(?![A-Za-z])", "", t)
    t = re.sub(r"\\[A-Za-z]+", "x", t)
    return len(re.sub(r"[{}\s^_]", "", t))


def check_tex(path):
    found = []
    src = open(path).read()
    # blank out displays, comments and verbatim-like code so only inline math is tested
    masked = re.sub(r"(?<!\\)%.*", lambda m: " " * len(m.group()), src)
    masked = re.sub(r"(?<!\\)\\\[.*?(?<!\\)\\\]|\\begin\{(align|equation|gather|multline)\*?\}.*?\\end\{\1\*?\}",
                    lambda m: re.sub(r"[^\n]", " ", m.group()), masked, flags=re.S)
    masked = re.sub(r"\\begin\{(py|rcode|plain|lstlisting)\}.*?\\end\{\1\}",
                    lambda m: re.sub(r"[^\n]", " ", m.group()), masked, flags=re.S)
    # a table of matrices, a figure, or a figure label is a place where an inline matrix belongs
    masked = re.sub(r"\\begin\{(tabular|tikzpicture|fig)\}.*?\\end\{\1\}",
                    lambda m: re.sub(r"[^\n]", " ", m.group()), masked, flags=re.S)
    for m in INLINE.finditer(masked):
        t = m.group(1)
        line = masked.count("\n", 0, m.start()) + 1
        if inline_matrix(t):
            found.append((line, "inline-matrix", t[:70]))
        elif computation(t):
            found.append((line, "inline-computation", t[:70]))
        if "\\dfrac" in t:
            found.append((line, "inline-dfrac", t[:70]))
    return found


VAGUE = [re.compile(p) for p in (
    r"\bthe (theorem|proposition|lemma|corollary|result|definition) (above|below|earlier)\b",
    r"\b[Cc]all (this|it) the\b",
    r"\bthe (paragraph|text) (above|below)\b",
    r"\b(first|second|third|fourth|last) consequence\b",
    r"\bthe (first|second|third|last) (item|bullet|paragraph|line) of\b",
    r"\bpart \([a-z]\) of the (\w+ )?(result|rule|lemma|theorem|proposition|formula)\b",
)]
# "the same rule", "the first formula", "the additive identity" refer to the text next to them
NICKNAME = re.compile(r"\bthe (?!(?:same|given|stated|first|second|third|last|following|previous|other|additive|multiplicative)\b)"
                      r"((?:[A-Za-z'-]+ ){1,2})(rule|formula|criterion|test|result|trick|identity)\b(?!\s*\()")
# standard names from other courses that need no box of their own
COMMON = {"product rule", "chain rule", "quotient rule", "sum rule", "power rule", "quadratic formula",
          "cubic formula", "binomial formula", "ratio test", "root test", "integral test", "comparison test",
          "second derivative test", "first derivative test", "triangle inequality", "midpoint rule",
          "parallelogram identity", "parallelogram law", "polarization identity"}


def check_references(path):
    """vague-reference findings for one .tex file."""
    try:
        src = link_refs.Source(os.path.abspath(path), link_refs.Course(os.path.dirname(os.path.dirname(os.path.abspath(path)))))
    except Exception:
        return []
    known = set(src.all_names)
    for folder in src.course.weeks.values():
        h = src.course.handout(folder)
        known |= h.all_names if h else set()
    known = {k.lower() for k in known}
    text = src.sh.restore(src.text)
    text = re.sub(r"(?<!\\)%.*", "", text)
    found = []
    for rx in VAGUE:
        for m in rx.finditer(text):
            found.append((text.count("\n", 0, m.start()) + 1, "vague-reference", m.group(0)))
    for m in NICKNAME.finditer(text):
        words = (m.group(1) + m.group(2)).lower().split()
        phrases = {" ".join(words[i:]) for i in range(len(words))}
        if not phrases & (known | COMMON):
            found.append((text.count("\n", 0, m.start()) + 1, "vague-reference", m.group(0)))
    return found


FIGURE = re.compile(r"\\begin\{tikzpicture\}|\\includegraphics")


def figures_in(texts):
    return sum(len(FIGURE.findall(t)) for t in texts)


def check_figures(path):
    """Compare the figures in a handout's folder (all .tex files) with the last commit."""
    folder = os.path.dirname(os.path.abspath(path))
    now = figures_in(open(p).read() for p in glob.glob(os.path.join(folder, "*.tex")))
    try:
        top = subprocess.run(["git", "-C", folder, "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
        rel = os.path.relpath(folder, top)
        names = subprocess.run(["git", "-C", top, "ls-tree", "--name-only", "HEAD", rel + "/"],
                               capture_output=True, text=True, check=True).stdout.split()
        before = figures_in(subprocess.run(["git", "-C", top, "show", f"HEAD:{n}"], capture_output=True,
                                           text=True).stdout for n in names if n.endswith(".tex"))
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    if now < before:
        return [(0, "figure-removed", f"{now} figures now, {before} in the last commit")]
    return []


# Banned phrasing and meta commentary (standard, Section 4: Revisiting the question; No meta commentary).
BANNED = [(re.compile(p, re.I), kind) for p, kind in (
    (r"question answered", "question-answered: use \\revisit"),
    (r"\(cited[^)]*\)|\bcited (?:here|without proof|from)\b|\bproves? this in (?:Ch|chapter)|\bproved for \$?2\s*\\times\s*2\$?\)|\bwe omit\b|\bnot covered here\b|\bthis handout\b|\bbeyond (?:the scope of|this course)\b", "meta-commentary"),
    (r"\[\s*Worked examples?\s+\d+\s*(?:--|-|–)\s*\d+", "bundled-examples: one example box per example"),
)]

def check_banned(path):
    text = re.sub(r"(?<!\\)%.*", "", open(path, encoding="utf-8").read())
    found = []
    for rx, kind in BANNED:
        for m in rx.finditer(text):
            found.append((text.count("\n", 0, m.start()) + 1, kind, m.group(0)))
    return found


def main():
    files = []
    for p in sys.argv[1:]:
        if os.path.isdir(p):
            files += sorted(glob.glob(os.path.join(p, "**", "*.tex"), recursive=True))
            files += sorted(glob.glob(os.path.join(p, "**", "*.pdf"), recursive=True))
        else:
            files.append(p)
    total = 0
    for f in files:
        if "/exercises/" in f or "/solutions/" in f and f.endswith(".py"):
            continue
        res = check_pdf(f) if f.endswith(".pdf") else check_tex(f) + check_references(f) + check_banned(f) if f.endswith(".tex") else []
        if os.path.basename(f) == "handout.tex":
            res += check_figures(f)
        for where, kind, text in res:
            print(f"{f}:{where}  {kind}  {text}")
        total += len(res)
    print(f"{total} findings")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
