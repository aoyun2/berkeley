#!/usr/bin/env python3
"""Build the public course website into _site/ (same plain style as the Putnam course site).

Usage: python3 scripts/build_site.py [--out _site]

Reads site.toml and every semesters/<term>/<course>/course.toml. For each [[week]] it links the
PDFs found in handouts/<start>-*/ and copies only those PDFs into the output. Nothing from
materials/ is ever copied. Solutions are linked only if publish_solutions = true in site.toml.
"""
import argparse, datetime as dt, glob, html, os, shutil, tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERMS = {"spring": "Spring", "summer": "Summer", "fall": "Fall"}

CSS = """
:root { --bg:#ffffff; --fg:#111111; --muted:#555555; --rule:#bbbbbb; --link:#0000cc; --visited:#551a8b; color-scheme: light dark; }
@media (prefers-color-scheme: dark) { :root { --bg:#161616; --fg:#e8e8e8; --muted:#a0a0a0; --rule:#444444; --link:#8ab4ff; --visited:#c9a6ff; } }
body { background:var(--bg); color:var(--fg); font-family:"Palatino Linotype",Palatino,"Book Antiqua","Iowan Old Style",Georgia,serif;
  font-size:17px; line-height:1.5; max-width:46rem; margin:0 auto; padding:32px 16px 64px; }
h1 { font-size:1.9em; font-weight:normal; margin:0 0 4px; }
h2 { font-size:1.25em; font-weight:normal; margin:32px 0 8px; border-bottom:1px solid var(--rule); padding-bottom:2px; }
a { color:var(--link); } a:visited { color:var(--visited); }
.sub, .pending, footer { color:var(--muted); }
dl { display:grid; grid-template-columns:max-content minmax(0,1fr); gap:2px 16px; margin:12px 0; }
dt { font-style:italic; } dd { margin:0; }
.tablewrap { overflow-x:auto; }
table { border-collapse:collapse; width:100%; }
th, td { text-align:left; vertical-align:top; padding:5px 10px 5px 0; border-bottom:1px solid var(--rule); }
th { font-weight:normal; font-style:italic; color:var(--muted); }
td.nw { white-space:nowrap; }
ul { padding-left:1.3em; }
footer { margin-top:40px; font-size:.9em; }
"""

def as_date(x):
    return x.date() if isinstance(x, dt.datetime) else x

def esc(x):
    return html.escape(str(x), quote=True).replace("--", "&ndash;")

def term_name(folder):
    year, _, term = folder.partition("-")
    return f"{TERMS.get(term, term.title())} {year}"

def date_range(start):
    end = start + dt.timedelta(days=6)
    if start.month == end.month:
        return f"{start.day}&ndash;{end.day} {end.strftime('%b')}"
    return f"{start.day} {start.strftime('%b')}&ndash;{end.day} {end.strftime('%b')}"

def page(title, sub, body, up=None):
    nav = f'<p class="sub"><a href="{up}">All courses</a></p>' if up else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>{CSS}</style>
</head>
<body>
{nav}
<h1>{esc(title)}</h1>
<p class="sub">{esc(sub)}</p>
{body}
</body>
</html>
"""

def link(href, text):
    return f'<a href="{href}" target="_blank" rel="noopener">{text}</a>'

def build_course(term, course, c, out, publish_solutions):
    src = os.path.join(ROOT, "semesters", term, course)
    dst = os.path.join(out, term, course)
    os.makedirs(dst, exist_ok=True)
    info = []
    for key, label in (("instructor", "Instructor"), ("instructors", "Instructors"), ("textbook", "Text"), ("quizzes", "Quizzes"), ("grading", "Grading")):
        if c.get(key):
            info.append(f"<dt>{label}</dt><dd>{esc(c[key])}</dd>")
    rows, built = [], 0
    for i, w in enumerate(c.get("week", []), 1):
        start = as_date(w["start"])
        topic = w.get("topics") or w.get("topic") or w.get("title") or ""
        material = w.get("material") or ""
        if isinstance(topic, list): topic = "; ".join(map(str, topic))
        if isinstance(material, list): material = ", ".join(map(str, material))
        show_material = material and len(material) <= 60 and "materials/" not in material
        desc = esc(topic) + (f" ({esc(material)})" if show_material else "")
        folders = sorted(glob.glob(os.path.join(src, "handouts", f"{start.isoformat()}-*")))
        links = []
        if folders:
            name = os.path.basename(folders[0])
            wanted = [("handout.pdf", "Handout")] + ([("solutions.pdf", "Solutions")] if publish_solutions else [])
            for fn, label in wanted:
                p = os.path.join(folders[0], fn)
                if os.path.exists(p):
                    os.makedirs(os.path.join(dst, name), exist_ok=True)
                    shutil.copy2(p, os.path.join(dst, name, fn))
                    links.append(link(f"{name}/{fn}", label))
        hw = w.get("homework")
        if isinstance(hw, list): hw = ", ".join(map(str, hw))
        due = w.get("due")
        extra = ""
        if hw:
            short = str(hw).split(" (")[0].split(":")[0].strip()
            due = as_date(due) if isinstance(due, (dt.date, dt.datetime)) else None
            extra = esc(short) + (f" due {due.strftime('%a %-d %b')}" if due else "")
        if links:
            built += 1
            cell = "<td>" + ", ".join(links) + (f"; {extra}" if extra else "") + "</td>"
        else:
            cell = '<td class="pending">not yet posted' + (f"; {extra}" if extra else "") + "</td>"
        rows.append(f'<tr><td>{w.get("number", i)}</td><td class="nw">{date_range(start)}</td><td>{desc}</td>{cell}</tr>')
    exams = []
    for e in c.get("exam", []):
        when = e.get("date")
        when = as_date(when) if isinstance(when, (dt.date, dt.datetime)) else None
        exams.append(f"<li>{esc(e.get('name', 'Exam'))}" + (f": {when.strftime('%a %-d %b %Y')}" if when else "") + (f", {esc(e['time'])}" if e.get("time") else "") + "</li>")
    body = ""
    if info: body += "<dl>\n" + "\n".join(info) + "\n</dl>\n"
    if exams: body += "<h2>Exams</h2>\n<ul>\n" + "\n".join(exams) + "\n</ul>\n"
    body += '<h2>Schedule</h2>\n<div class="tablewrap">\n<table>\n<thead><tr><th>Week</th><th>Dates</th><th>Topic</th><th>Materials</th></tr></thead>\n<tbody>\n' + "\n".join(rows) + "\n</tbody>\n</table>\n</div>\n"
    body += "<footer>Handouts are study notes written for these courses; homework and exam problems quoted in them belong to the course staff.</footer>"
    with open(os.path.join(dst, "index.html"), "w") as f:
        f.write(page(c.get("name", course), term_name(term), body, up="../../index.html"))
    return built, len(c.get("week", []))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "_site"))
    a = ap.parse_args()
    with open(os.path.join(ROOT, "site.toml"), "rb") as f:
        cfg = tomllib.load(f)
    shutil.rmtree(a.out, ignore_errors=True)
    os.makedirs(a.out)
    open(os.path.join(a.out, ".nojekyll"), "w").close()
    body = ""
    for tdir in sorted(glob.glob(os.path.join(ROOT, "semesters", "*")), reverse=True):
        term = os.path.basename(tdir)
        items = []
        for path in sorted(glob.glob(os.path.join(tdir, "*", "course.toml"))):
            course = os.path.basename(os.path.dirname(path))
            with open(path, "rb") as f:
                c = tomllib.load(f)
            built, total = build_course(term, course, c, a.out, cfg.get("publish_solutions", False))
            status = f"{built} of {total} weekly handouts posted" if total else "schedule not yet entered"
            items.append(f'<li><a href="{term}/{course}/index.html">{esc(c.get("name", course))}</a> <span class="sub">({status})</span></li>')
        if items:
            body += f"<h2>{term_name(term)}</h2>\n<ul>\n" + "\n".join(items) + "\n</ul>\n"
    body += "<footer>One handout per homework week, built to a common standard. Typeset with evan.sty by Evan Chen.</footer>"
    with open(os.path.join(a.out, "index.html"), "w") as f:
        f.write(page(cfg.get("title", "Course handouts"), cfg.get("subtitle", ""), body))
    print("built", a.out)

if __name__ == "__main__":
    main()
