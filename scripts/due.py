#!/usr/bin/env python3
"""What needs building this week, across all active courses.

Usage: python3 scripts/due.py [--today YYYY-MM-DD] [--days N] [--exam-days N]

Reads every semesters/*/*/course.toml with status = "active" and prints:
  * weeks whose start date falls in (today, today + days]  -> a weekly handout is due,
    marked BUILT if a folder handouts/<start>-* already exists;
  * exams within exam-days                                  -> exam review is due;
  * active courses with no [[week]] entries                 -> schedule missing.
"""
import argparse, datetime as dt, glob, os, tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def as_date(x):
    return x.date() if isinstance(x, dt.datetime) else x

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--exam-days", type=int, default=21)
    a = ap.parse_args()
    end = a.today + dt.timedelta(days=a.days)
    found = False
    for path in sorted(glob.glob(os.path.join(ROOT, "semesters", "*", "*", "course.toml"))):
        with open(path, "rb") as f:
            c = tomllib.load(f)
        if c.get("status") != "active":
            continue
        cdir = os.path.dirname(path)
        rel = os.path.relpath(cdir, ROOT)
        name = c.get("name", rel)
        weeks = c.get("week", [])
        if not weeks:
            print(f"[SCHEDULE MISSING] {name} ({rel}): no [[week]] entries; ask Aaron for the syllabus/homework schedule.")
            found = True
        for w in weeks:
            start = as_date(w["start"])
            if a.today < start <= end:
                built = glob.glob(os.path.join(cdir, "handouts", f"{start.isoformat()}-*"))
                status = "BUILT" if built else "TO BUILD"
                print(f"[WEEK {status}] {name} ({rel}): week of {start}: {w.get('topics','')}")
                print(f"    material: {w.get('material','')}")
                print(f"    homework: {w.get('homework','')} (due {w.get('due','?')})")
                found = True
        for e in c.get("exam", []):
            d = as_date(e["date"])
            if a.today <= d <= a.today + dt.timedelta(days=a.exam_days):
                print(f"[EXAM IN {(d - a.today).days} DAYS] {name} ({rel}): {e['name']} on {e['date']}; covers {e.get('covers','?')}")
                found = True
    if not found:
        print("Nothing due in this window.")

if __name__ == "__main__":
    main()
