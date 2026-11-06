# CS 61A Fall 2026 source collection

Retrieved from the official Fall 2026 calendar and its linked materials on 2026-11-06. These are source materials for the requested private study backfill. No CS 61A handout has been authored or approved at this stage.

## Start here

- `calendar.json`: exact calendar rows, dates, item labels, titles and links, grouped by the site's 15 numbered weeks.
- `week-source-index.json`: the same weekly inventory with local material paths. The partial first week begins Monday August 24 (first lecture Wednesday August 26). **Eleven** lecture weeks start on or before November 2.
- `source-manifest.json`: original URLs, response metadata, SHA-256 hashes, and local paths. It includes lecture pages/slides/examples, Composing Programs readings, discussions, labs, homework, projects, study guides and selected real exams/solutions.
- `missing-sources.json`: calendar titles without published links, plus the verified 404 for Homework 8. A calendar title is not an exercise statement.
- `starter-code-manifest.json`: authentic source/test/config files extracted from official starter ZIPs, with archive URL, archive SHA-256, member path and extracted-file hash. Bundled graders/vendor code and audiovisual assets were not extracted.
- `lecture-playground-manifest.json`: exact official lecture share URLs and their decoded source paths. The LZ-String Base64 fragments for lectures 27, 28 and 29 were decoded and round-trip verified; the saved `.gleam` files contain the actual published examples.

HTML pages have original `.html` and normalized `.txt` copies. Official PDF originals are retained with `.pdf.txt` extractions. Consult the original PDFs for mathematical notation, diagrams and page identifiers. Extracted starter code is under `starter-code/`; decoded Gleam examples are under `lecture-examples/`.

The original ZIP downloads are supplementary **local archive caches**, with their URLs and hashes retained in the manifest. The root agent will exclude ZIP caches from Git locally while committing the readable statements, PDFs, authentic selected source/config files and manifests. The ZIPs remain physically in this materials folder and can be downloaded again from their exact URLs. A typical Python starter repeats about 6 MB of bundled `.grader/pygments` code; the Cats and Ants archives also include music/images/fonts unrelated to the study explanations. Do not mistake bundled vendor assets for course lecture content.

## Schedule conventions

`course.toml` uses the Monday of each actual lecture week for `start`, including August 24. Its required `due` is an actual primary assignment deadline: a newly released homework when one exists, otherwise an explicitly identified lab/project/continuing-work deadline. It is not a fabricated Friday date or a claim that every assignment covers every lecture in that week.

Every newly listed lab, discussion, quiz, homework and project is retained separately in `[[week.assignments]]`, with its calendar date, exact description, actual due date when supplied, source URL when published, and checkpoint text. Weeks without newly released homework say so explicitly. A previous assignment is identified as continuing work rather than reassigned to a different lecture week.

There are 15 term weeks and six main/optional exam-window entries. The final remains Friday December 18, 11:30 a.m.–2:30 p.m. Midterm 2 is a booked one-hour CBTF appointment during October 5–9, not one common exam time. Optional retake windows are recorded as windows; the November window offers November 5–6 and November 9–10, not the intervening weekend.

## Current missing material and naming caveats

- **Homework 8, Gleam Data:** calendar item on November 6, due Thursday November 12, with no link. The pattern-supported public URL `https://cs61a.org/fa26/hw/hw08/` returned 404. No problem statements or answers were invented. The November 2 packet cannot be approved as complete until the actual assignment is available.
- **Project 4, Animator:** the November 6 calendar lists Gleam and TypeScript alternatives with final/checkpoint dates, but no linked project source. Their titles/deadlines are recorded only. Do not invent project specifications.
- Lecture 31 intentionally says “No Lecture (just videos)”; do not invent a separate lecture note. Lectures 29–30, their slides, Lab 8, Discussion 9 and the Gleam appendices are saved.
- Later weeks retain the official calendar's titles and dates even when pages are unpublished. They belong in the schedule; no handouts for November 9 or later should be generated.
- The official past-exam index calls `fa26-mt2` **“Fall 2026 Midterm 3.”** Its legacy path is not the identity of this course's CBTF Midterm 2. Use the official name and problem identifiers, not a guessed name from the filename.
- Some optional instructional videos require a Berkeley login. Public text, slides and code are saved; authenticated video content has not been represented as downloaded or reviewed.

## Executable languages

This is the actual Fall 2026 curriculum: Python first, then **Gleam**, not Scheme, in weeks 10–11. Homework 7 and Lab 8 have these exact project requirements:

```toml
target = "javascript"
gleam = ">= 1.14.0"
[dependencies]
gleam_stdlib = ">= 1.0.0 and < 2.0.0"
[dev-dependencies]
gleeunit = ">= 1.0.0 and < 2.0.0"
```

Lab 8 requires Node.js 22 or newer. It explicitly says Erlang is unnecessary for these JavaScript-target assignments. Inside an extracted official project, use `gleam test`, `gleam test -- <question>`, `gleam test -- score`, and `gleam run`. The untouched starter contains `todo` placeholders, so failing starter tests are expected; they are not a readiness pass or a reason to disable tests. Do not modify the saved source originals. The separate tooling agent is verifying the compiler/runtime using scratch copies.

## Attribution and source notices

Composing Programs, third edition, identifies **John DeNero** as author and marks its content **CC BY-NC-SA 4.0**: https://creativecommons.org/licenses/by-nc-sa/4.0/. The original page frontmatter and notices are retained. Attribute adaptations, identify changes, and retain the source identifiers; use original explanations in the study packets.

CS 61A course pages state **Copyright ©2026, Regents of the University of California and respective authors**. No blanket open license for the course assignments was found; do not describe them as public-domain or freely licensed. The collection preserves the official statements, source URLs and notices for the user's requested private study reference.

Official past-exam PDFs and solutions from Fall 2026, Fall 2025, Spring 2026 and Summer 2026 were selected from the official `resources/_exams/exam_files.json` index. Each downloaded PDF's SHA-256 matches that index. The saved topic indexes let a future author choose real questions that use only the current or earlier week's material, with original term/exam/problem labels. Do not invent exam provenance.
