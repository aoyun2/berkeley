#!/usr/bin/env python3
"""Build the course website in the layout of the Putnam course site: a home page listing the
current term's courses, and one page per course (facts and a weekly schedule).

Usage: python3 scripts/build_site.py            # writes index.html at the repository root
       python3 scripts/build_site.py --out _site  # also copies index.html and the linked PDFs into _site/

The page lists every active course of the current term. For each course: a short facts list and a
schedule table (Week, Dates, Topic, Materials). A week's Topic is its `title` in course.toml.
Materials links the handout (and, if publish_solutions is true in site.toml, the solutions) when the
handout folder exists; otherwise it says "not yet posted".

Links are relative paths into the repository, so the page works both when GitHub Pages serves the
branch directly and when the workflow deploys _site/. Nothing from materials/ is linked or copied.
"""
import argparse, datetime as dt, glob, html, os, re, shutil, tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERM_NAMES = {"spring": "Spring", "summer": "Summer", "fall": "Fall"}
REPO_URL = "https://github.com/aoyun2/berkeley/tree/main/"

CSS = """
:root {
  --bg: #ffffff; --fg: #111111; --muted: #555555; --rule: #bbbbbb;
  --link: #0000cc; --visited: #551a8b;
  color-scheme: light dark;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #161616; --fg: #e8e8e8; --muted: #a0a0a0; --rule: #444444; --link: #8ab4ff; --visited: #c9a6ff; }
}
body {
  background: var(--bg); color: var(--fg);
  font-family: "Palatino Linotype", Palatino, "Book Antiqua", "Iowan Old Style", Georgia, serif;
  font-size: 17px; line-height: 1.5;
  max-width: 44rem; margin: 0 auto; padding: 32px 16px 64px;
}
h1 { font-size: 1.9em; font-weight: normal; margin: 0 0 4px; }
h2 { font-size: 1.25em; font-weight: normal; margin: 32px 0 8px; border-bottom: 1px solid var(--rule); padding-bottom: 2px; }
a { color: var(--link); }
a:visited { color: var(--visited); }
.sub, .pending { color: var(--muted); }
dl { display: grid; grid-template-columns: max-content minmax(0, 1fr); gap: 2px 16px; margin: 12px 0; }
dt { font-style: italic; }
dd { margin: 0; }
.tablewrap { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; }
th, td { text-align: left; vertical-align: top; padding: 5px 10px 5px 0; border-bottom: 1px solid var(--rule); }
th { font-weight: normal; font-style: italic; color: var(--muted); }
td.nw, span.nw { white-space: nowrap; }
ul { padding-left: 1.3em; }
ul.courses { list-style: none; padding-left: 0; }
ul.courses li { margin: 0 0 12px; }
""".strip()


def as_date(x):
    if isinstance(x, dt.datetime):
        return x.date()
    return x if isinstance(x, dt.date) else None


def esc(s):
    return html.escape(str(s), quote=True)


def dash(s):
    """Escape, use an en dash between numbers (1-2 -> 1–2), and keep a trailing
    parenthetical such as (Lectures 1–2) on one line."""
    t = re.sub(r"(?<=\d)-(?=\d)", "&ndash;", esc(s)).replace("–", "&ndash;")
    return re.sub(r"(\([^()]*\))", r'<span class="nw">\1</span>', t)


def day(d):
    return f"{d.strftime('%a')} {d.day} {d.strftime('%b')}"


def week_range(start):
    end = start + dt.timedelta(days=6)
    if start.month == end.month:
        return f"{start.day}&ndash;{end.day} {end.strftime('%b')}"
    return f"{start.day} {start.strftime('%b')}&ndash;{end.day} {end.strftime('%b')}"


def clock(t):
    h, m = t.hour, t.minute
    return f"{(h - 1) % 12 + 1}:{m:02d}", ("am" if h < 12 else "pm")


def time_range(start, end):
    a, ap = clock(start)
    if not end:
        return f"{a} {ap}"
    eh, em = (int(x) for x in str(end).split(":"))
    b, bp = clock(dt.time(eh, em))
    return f"{a}&ndash;{b} {bp}" if ap == bp else f"{a} {ap}&ndash;{b} {bp}"


def first_clause(s):
    """Plain fact without bookkeeping: drop anything in parentheses and after a semicolon."""
    s = re.sub(r"\s*\([^)]*\)", "", str(s)).split(";")[0].strip()
    return s[:1].upper() + s[1:]


def exams_text(exams):
    items = []
    for e in exams:
        name = re.sub(r"\s*\([^)]*\)", "", e.get("name", "Exam")).strip()
        if "retake" in name.lower():
            continue
        when = e.get("date")
        d = as_date(when)
        if d is None:
            continue
        text = f"{esc(name)} {day(d)}"
        end_d = as_date(e.get("end_date"))
        if end_d:
            text = f"{esc(name)} {d.day}&ndash;{end_d.day} {end_d.strftime('%b')}" if end_d.month == d.month else \
                   f"{esc(name)} {d.day} {d.strftime('%b')}&ndash;{end_d.day} {end_d.strftime('%b')}"
        if isinstance(when, dt.datetime) and (when.hour or when.minute):
            text += ", " + time_range(when.time(), e.get("end"))
        items.append(text)
    return "; ".join(items)


HW = re.compile(r"\b(Homework \d+|HW ?\d+|Worksheet Packet \d+)")


def homework_text(w):
    hw = w.get("homework")
    if isinstance(hw, list):
        hw = " ".join(map(str, hw))
    hw = str(hw or "")
    m = HW.search(hw)
    if hw.lower().startswith("no new") or not m:
        return ""
    label = m.group(1).replace("Worksheet Packet", "Worksheet packet")
    due = as_date(w.get("due"))
    return f"{esc(label)} (due {day(due)})" if due else esc(label)


def link(href, text):
    return f'<a href="{esc(href)}" target="_blank" rel="noopener">{text}</a>'


def num_of(w, i):
    return w.get("number", i)


def course_section(term, course, c, publish_solutions, files, posted):
    rel = f"semesters/{term}/{course}"
    facts = []
    if c.get("instructor") or c.get("instructors"):
        who = c.get("instructor") or c.get("instructors")
        facts.append(("Instructor" if c.get("instructor") else "Instructors", esc(who)))
    if c.get("textbook"):
        facts.append(("Text", esc(first_clause(c["textbook"]))))
    if c.get("quizzes"):
        facts.append(("Quizzes", esc(first_clause(c["quizzes"]))))
    ex = exams_text(c.get("exam", []))
    if ex:
        facts.append(("Exams", ex))

    rows = []
    for i, w in enumerate(c.get("week", []), 1):
        start = as_date(w["start"])
        topic = dash(w.get("title") or w.get("topics") or "")
        folders = sorted(glob.glob(os.path.join(ROOT, rel, "handouts", f"{start.isoformat()}-*")))
        links = []
        if folders:
            name = os.path.basename(folders[0])
            for fn, label, show in (("handout.pdf", "Handout", True), ("solutions.pdf", "Solutions", publish_solutions)):
                if show and os.path.exists(os.path.join(folders[0], fn)):
                    files.append(f"{rel}/handouts/{name}/{fn}")
                    links.append(link(f"handouts/{name}/{fn}", label))
            if os.path.isdir(os.path.join(folders[0], "exercises")):
                links.append(link(f"{REPO_URL}{rel}/handouts/{name}/exercises", "Exercises"))
        if links:
            posted.append(num_of(w, i))
            hw = homework_text(w)
            cell = "<td>" + ", ".join(links) + (f"; {hw}" if hw else "") + "</td>"
        else:
            cell = '<td class="pending">not yet posted</td>'
        num = w.get("number", i)
        rows.append(f'    <tr><td>{num}</td><td class="nw">{week_range(start)}</td><td>{topic}</td>\n        {cell}</tr>')

    out = []
    if facts:
        out.append("<dl>")
        out += [f"  <dt>{k}</dt><dd>{v}</dd>" for k, v in facts]
        out.append("</dl>")
    out.append('<h2>Schedule</h2>\n<div class="tablewrap">\n<table>\n  <thead><tr><th>Week</th><th>Dates</th><th>Topic</th><th>Materials</th></tr></thead>\n  <tbody>')
    out += rows
    out.append("  </tbody>\n</table>\n</div>")
    return "\n".join(out)


def html_page(title, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>
{CSS}
</style>
</head>
<body>

{body}

</body>
</html>
"""


def term_label(term):
    year, _, t = term.partition("-")
    return f"{TERM_NAMES.get(t, t.title())} {year}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="also copy the page and linked PDFs into this folder")
    a = ap.parse_args()
    with open(os.path.join(ROOT, "site.toml"), "rb") as f:
        cfg = tomllib.load(f)
    publish = cfg.get("publish_solutions", False)

    terms = sorted(os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "semesters", "*")))
    term = terms[-1]
    courses = []
    for path in sorted(glob.glob(os.path.join(ROOT, "semesters", term, "*", "course.toml"))):
        with open(path, "rb") as f:
            c = tomllib.load(f)
        courses.append((os.path.basename(os.path.dirname(path)), c))

    files, pages, rows = [], [], []
    for course, c in courses:
        posted = []
        body = course_section(term, course, c, publish, files, posted)
        name = c.get("name", course)
        rel = f"semesters/{term}/{course}/index.html"
        pages.append(rel)
        with open(os.path.join(ROOT, rel), "w") as f:
            f.write(html_page(name, f'<p class="sub"><a href="../../../index.html">All courses</a></p>\n\n<h1>{esc(name)}</h1>\n<p class="sub">{term_label(term)}</p>\n\n{body}'))
        final = next((e for e in c.get("exam", []) if e.get("name", "").lower().startswith("final")), None)
        final_txt = exams_text([final]).split(" ", 1)[1] if final else ""
        if not posted:
            got = '<span class="pending">none yet</span>'
        elif posted == list(range(posted[0], posted[-1] + 1)):
            got = f"Week {posted[0]}" if len(posted) == 1 else f"Weeks {posted[0]}&ndash;{posted[-1]}"
        else:
            got = "Weeks " + ", ".join(map(str, posted))
        who = c.get("instructor") or c.get("instructors") or ""
        facts = [esc(who)] if who else []
        facts.append(f"handouts for {got.lower()}" if posted else "no handouts yet")
        if final_txt:
            facts.append(f"final {final_txt}")
        line = "; ".join(facts)
        rows.append(f'  <li><a href="{rel}">{esc(name)}</a><br><span class="sub">{line[:1].upper() + line[1:]}</span></li>')

    body = f"""<h1>{esc(cfg.get("title", "Courses"))}</h1>
<p class="sub">{esc(cfg.get("subtitle", ""))}</p>

<h2>{term_label(term)}</h2>
<ul class="courses">
{chr(10).join(rows)}
</ul>"""
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html_page(cfg.get("title", "Courses"), body))
    if a.out:
        shutil.rmtree(a.out, ignore_errors=True)
        os.makedirs(a.out)
        open(os.path.join(a.out, ".nojekyll"), "w").close()
        for p in ["index.html"] + pages + files:
            os.makedirs(os.path.join(a.out, os.path.dirname(p)), exist_ok=True)
            shutil.copy2(os.path.join(ROOT, p), os.path.join(a.out, p))
    print("wrote index.html and", len(pages), "course pages" + (f"; copied to {a.out}/" if a.out else ""))


if __name__ == "__main__":
    main()
