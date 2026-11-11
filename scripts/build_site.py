#!/usr/bin/env python3
"""Build the course website, in the layout of the Putnam course site.

Usage: python3 scripts/build_site.py              # writes the pages into the repository
       python3 scripts/build_site.py --out _site  # also copies the pages and linked PDFs into _site/

Pages written:
  index.html                              home page: every term, newest first, one line per course
  semesters/<term>/<course>/index.html    course page: instructor, text, and a table of weeks

The site is for study, not for running the course: it shows no exam, quiz or due dates.
A week's Topic is its `title` in course.toml. Materials links the handout (and, if
publish_solutions is true in site.toml, the solutions) when the handout folder exists.
Links are relative, so the pages work whether GitHub Pages serves the branch or the workflow
deploys _site/. Nothing from materials/ is linked or copied.
"""
import argparse, glob, html, os, re, shutil, tomllib

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
span.nw, td.nw { white-space: nowrap; }
ul.courses { list-style: none; padding-left: 0; }
ul.courses li { margin: 0 0 12px; }
""".strip()


def esc(s):
    return html.escape(str(s), quote=True)


def topic_html(s):
    """Escape; en dash between numbers (Ch. 1-2 -> Ch. 1–2); keep a trailing (…) on one line."""
    t = re.sub(r"(?<=\d)[-–](?=\d)", "&ndash;", esc(s))
    return re.sub(r"(\([^()]*\))", r'<span class="nw">\1</span>', t)


def plain(s):
    """A course fact without bookkeeping: drop parentheses and anything after a semicolon."""
    s = re.sub(r"\s*\([^)]*\)", "", str(s)).split(";")[0].strip()
    return s[:1].upper() + s[1:]


def link(href, text):
    return f'<a href="{esc(href)}" target="_blank" rel="noopener">{text}</a>'


def term_label(term):
    year, _, t = term.partition("-")
    return f"{TERM_NAMES.get(t, t.title())} {year}"


def instructor(c):
    return c.get("instructor") or c.get("instructors") or ""


def weeks_label(nums):
    if not nums:
        return "no handouts yet"
    if nums == list(range(nums[0], nums[-1] + 1)):
        span = f"week {nums[0]}" if len(nums) == 1 else f"weeks {nums[0]}&ndash;{nums[-1]}"
    else:
        span = "weeks " + ", ".join(map(str, nums))
    return "handouts for " + span


def page(title, body):
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


def course_page(term, course, c, publish_solutions):
    """Return (html, posted week numbers, repo paths of linked PDFs)."""
    rel = f"semesters/{term}/{course}"
    facts = []
    if instructor(c):
        facts.append(("Instructors" if c.get("instructors") else "Instructor", esc(instructor(c))))
    if c.get("textbook"):
        facts.append(("Text", esc(plain(c["textbook"]))))

    rows, posted, files = [], [], []
    for i, w in enumerate(c.get("week", []), 1):
        num = w.get("number", i)
        folders = sorted(glob.glob(os.path.join(ROOT, rel, "handouts", f"{w['start']}-*")))
        links = []
        if folders:
            name = os.path.basename(folders[0])
            wanted = [("handout.pdf", "Handout")] + ([("solutions.pdf", "Solutions")] if publish_solutions else [])
            for fn, label in wanted:
                if os.path.exists(os.path.join(folders[0], fn)):
                    files.append(f"{rel}/handouts/{name}/{fn}")
                    links.append(link(f"handouts/{name}/{fn}", label))
            if os.path.isdir(os.path.join(folders[0], "exercises")):
                links.append(link(f"{REPO_URL}{rel}/handouts/{name}/exercises", "Exercises"))
        if links:
            posted.append(num)
            cell = '<td class="nw">' + ", ".join(links) + "</td>"
        else:
            cell = '<td class="pending">not yet posted</td>'
        topic = topic_html(w.get("title") or w.get("topics") or "")
        rows.append(f"    <tr><td>{num}</td><td>{topic}</td>{cell}</tr>")

    name = c.get("name", course)
    body = [
        '<p class="sub"><a href="../../../index.html">All courses</a></p>',
        "",
        f"<h1>{esc(name)}</h1>",
        f'<p class="sub">{term_label(term)}</p>',
        "",
    ]
    if facts:
        body += ["<dl>"] + [f"  <dt>{k}</dt><dd>{v}</dd>" for k, v in facts] + ["</dl>", ""]
    body += [
        "<h2>Handouts</h2>",
        '<div class="tablewrap">',
        "<table>",
        "  <thead><tr><th>Week</th><th>Topic</th><th>Materials</th></tr></thead>",
        "  <tbody>",
        *rows,
        "  </tbody>",
        "</table>",
        "</div>",
    ]
    return page(name, "\n".join(body)), posted, files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", help="also copy the pages and linked PDFs into this folder")
    a = ap.parse_args()
    with open(os.path.join(ROOT, "site.toml"), "rb") as f:
        cfg = tomllib.load(f)
    publish = cfg.get("publish_solutions", False)

    written, linked, sections = [], [], []
    terms = sorted((os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "semesters", "*"))), reverse=True)
    for term in terms:
        items = []
        for path in sorted(glob.glob(os.path.join(ROOT, "semesters", term, "*", "course.toml"))):
            course = os.path.basename(os.path.dirname(path))
            with open(path, "rb") as f:
                c = tomllib.load(f)
            html_text, posted, files = course_page(term, course, c, publish)
            rel = f"semesters/{term}/{course}/index.html"
            with open(os.path.join(ROOT, rel), "w") as f:
                f.write(html_text)
            written.append(rel)
            linked += files
            line = "; ".join(x for x in (esc(instructor(c)), weeks_label(posted)) if x)
            items.append(f'  <li><a href="{rel}">{esc(c.get("name", course))}</a><br>'
                         f'<span class="sub">{line[:1].upper() + line[1:]}</span></li>')
        if items:
            sections.append(f"<h2>{term_label(term)}</h2>\n<ul class=\"courses\">\n" + "\n".join(items) + "\n</ul>")

    title = cfg.get("title", "Courses")
    home = f'<h1>{esc(title)}</h1>\n<p class="sub">{esc(cfg.get("subtitle", ""))}</p>\n\n' + "\n\n".join(sections)
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(page(title, home))
    written.insert(0, "index.html")

    if a.out:
        shutil.rmtree(a.out, ignore_errors=True)
        os.makedirs(a.out)
        open(os.path.join(a.out, ".nojekyll"), "w").close()
        for p in written + linked:
            os.makedirs(os.path.join(a.out, os.path.dirname(p)), exist_ok=True)
            shutil.copy2(os.path.join(ROOT, p), os.path.join(a.out, p))
    print(f"wrote {len(written)} pages" + (f"; copied with {len(linked)} PDFs to {a.out}/" if a.out else ""))


if __name__ == "__main__":
    main()
