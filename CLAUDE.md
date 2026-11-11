# College course system (Aaron)

This repo holds every course Aaron takes at UC Berkeley (Fall 2026 to Spring 2030): materials, schedules, and the handouts Claude builds. Read `standards/handout-standard.md` before building anything; it is not optional.

## Layout
- `semesters/<yyyy-term>/<course>/course.toml`: course facts, one `[[week]]` per homework week (start, material, topics, homework, due), and `[[exam]]` entries.
- `semesters/<yyyy-term>/<course>/materials/`: syllabus, lecture notes, textbook text, homework, practice and past exams, graded work. Aaron adds files here as courses post them.
- `semesters/<yyyy-term>/<course>/handouts/<week-start-date>-<short-name>/`: built handouts (`handout.tex/.pdf`, `solutions.tex/.pdf`).
- `semesters/<yyyy-term>/<course>/log.md`: one line per thing built or sent, and notes on Aaron's weak spots (from graded work).
- `standards/`, `templates/` (evan.sty, handout.sty, starter .tex files), `scripts/due.py`, `scripts/build.sh`.
- `scripts/build_site.py`, `site.toml`, `.github/workflows/pages.yml`: the public course website (same plain style as the Putnam course site). It is rebuilt and deployed by GitHub Actions on every push to `main`; it lists each course's weeks from `course.toml` and links the handout PDFs that exist. It never copies anything from `materials/`. Solutions are published only if `publish_solutions = true` in `site.toml`; do not change that setting without Aaron saying so.

## Weekly run (scheduled every Saturday morning, Pacific time)
1. `python3 scripts/due.py` lists, for every active course: weeks starting in the next 7 days (TO BUILD or BUILT), exams in the next 21 days, and courses with no schedule.
2. For each week marked TO BUILD: read the material it names (lecture notes chapters, textbook sections) and the homework problems, then build `handout` and `solutions` per the standard in `handouts/<start>-<short-name>/`. Build with `scripts/build.sh`. Run the checks in the standard, including the independent audit, before sending.
3. For each exam within 21 days: once per exam, send Aaron a day-by-day review plan to the exam date using the existing weekly handouts; in the final two weeks build review handouts one topic at a time (same standard), using real past exams.
4. For each course with no schedule, or a week whose homework/notes are not in `materials/` yet: do not guess. Tell Aaron exactly which files are missing.
5. Commit with a clear message and push to `main`. Append to `log.md`.
6. Send the PDFs to Aaron and a short message: what was built for which course, what is missing.

## Adding a course or semester
Create `semesters/<yyyy-term>/<course>/` with `course.toml` (`status = "active"`) and the syllabus in `materials/`. Fill in `[[week]]` entries from the syllabus. At the end of a term set `status = "done"`.

## Rules
- Aaron's preferences live in Claude's memory and in the standard; both apply.
- Never delete Aaron's materials. Never commit secrets.
- Textbooks are not stored in this repo. Do not add textbook PDFs or text. Work from the lecture notes, homework and exams in `materials/`; if a textbook is needed, tell Aaron which sections and ask him to provide it in the conversation.
