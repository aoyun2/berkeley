# Backfill restart status and questions

## Current regenerated release

- **MATH 110 week 1 (2026-08-31): revised and re-reviewed**, 14-page [handout](semesters/2026-fall/math110/handouts/2026-08-31-sets-fields-subspaces/handout.pdf) and 4-page [solutions](semesters/2026-fall/math110/handouts/2026-08-31-sets-fields-subspaces/solutions.pdf). Fresh correctness/coverage and teaching review passed after specific corrections; every final page inspected, exact computations passed.
- **MATH 110 weeks 2–10: not yet regenerated**, previous versions remain rejected.
- CS 61A, STAT 20, MATH 54: validated sources/schedules collected; no handouts built. Production follows the MATH 110 rework in that order.


## Previous MATH 110 release — rejected; revision required

Aaron rejected the previous packets for unclear prose, insufficient explanatory figures, and vague claims. **All ten weeks below require revision or regeneration against the supplied reference packet. They are not approved finished backfill.** The previous files were built and pushed in week order. Each folder contains `handout.tex`, `handout.pdf`, `solutions.tex`, and `solutions.pdf`. Total: **20 PDFs, 151 pages** (131 handout pages and 20 solution pages).

| Week | Start | Topics | Handout pages | Solutions pages |
|---|---|---|---:|---:|
| 1 | [2026-08-31](semesters/2026-fall/math110/handouts/2026-08-31-sets-fields-subspaces/) | Sets, fields, vector spaces, subspaces | 10 | 2 |
| 2 | [2026-09-07](semesters/2026-fall/math110/handouts/2026-09-07-bases-dimension/) | Linear independence, span, bases, dimension | 10 | 2 |
| 3 | [2026-09-14](semesters/2026-fall/math110/handouts/2026-09-14-linear-maps-matrices/) | Linear maps, null spaces, ranges, matrices | 13 | 2 |
| 4 | [2026-09-21](semesters/2026-fall/math110/handouts/2026-09-21-isomorphisms-products-quotients/) | Isomorphisms, inverses, products, quotient spaces | 13 | 2 |
| 5 | [2026-09-28](semesters/2026-fall/math110/handouts/2026-09-28-quotients-duality/) | Quotient spaces, isomorphism theorems, duality | 14 | 2 |
| 6 | [2026-10-05](semesters/2026-fall/math110/handouts/2026-10-05-eigenvalues-pagerank/) | Invariant subspaces and eigenvalues | 14 | 2 |
| 7 | [2026-10-12](semesters/2026-fall/math110/handouts/2026-10-12-diagonalization-minimal-polynomial/) | Diagonalizability and the minimal polynomial | 16 | 2 |
| 8 | [2026-10-19](semesters/2026-fall/math110/handouts/2026-10-19-generalized-eigenvectors-jordan/) | Generalized eigenvectors and Jordan form | 14 | 2 |
| 9 | [2026-10-26](semesters/2026-fall/math110/handouts/2026-10-26-trace-inner-products/) | Trace and inner products | 12 | 2 |
| 10 | [2026-11-02](semesters/2026-fall/math110/handouts/2026-11-02-orthogonality-projections/) | Orthogonality, Gram-Schmidt, projections | 15 | 2 |

The previous process reported exact computation checks, a source/content audit, and page inspection. Those checks did not establish the teaching quality Aaron requested. A new teaching-quality review is required for every week. Builds have no overfull boxes. Verification scripts are in `scripts/checks/math110_week01.py` through `math110_week10.py`; activate the tools with `source /workspace/.berkeley-tools/activate.sh`. Each completed week was logged, committed, pulled with rebase, and pushed to `main` before the next week.

Coverage includes all numbered lecture-note definitions, results and examples, matching textbook results/examples, all assigned problems including optional problems, and appropriately sourced extra practice. Extra problems use real saved exams where their coverage applies; later topics without applicable saved exam problems use explicitly identified textbook exercises. No invented exam provenance is used.

Source caveats are identified explicitly in the packets: missing linearity hypotheses in some homework statements, finite-field qualifications, the zero-dimensional minimal-polynomial exception, trace interpreted as a field scalar, orthogonal versus orthonormal formulas, and analytic ingredients that need citation. These corrections leave the original source materials intact.

## Cleanup and preservation

- Removed exactly the requested MATH 110 `handouts/archive/` and `handouts/2026-11-06-ch13-18-review/` directories and their obsolete log lines.
- Preserved every pre-existing materials file. The original Weak spots section is byte-for-byte unchanged.
- Fixed `scripts/build.sh`: an explicitly requested source now takes precedence over a template with the same basename, and LaTeX failures propagate. Verified both source selection and failure handling.
- No handouts starting on or after 2026-11-09 were created. MATH 110's future weeks remain in `course.toml` for the separate scheduled job.

## Remaining: CS 61A, STAT 20, MATH 54

Network access is now restored: all five supplied course pages returned HTTP 200 in the newly published environment. Source collection has begun, but no new course packets have been produced or committed. Their source caches are preserved locally. This restart first revises MATH 110 weeks 1–10, then proceeds through CS 61A, STAT 20 and MATH 54. The reference packet and explicit release criteria are in `standards/reference/` and `standards/teaching-quality.md`.

The exact source URLs are:

- https://math.berkeley.edu/~kwohm/Syllabus54-FA26.html
- https://math.berkeley.edu/~kwohm/Calendar54-FA26.html
- https://math.berkeley.edu/~kwohm/Homework54-FA26.html
- https://cs61a.org/fa26/
- https://stat20.berkeley.edu/fall-2026/

No lecture topics, week starts, homework exercise lists or inaccessible course materials were invented. The existing CS 61A and MATH 54 final dates were retained. MATH 54's supplied midterm dates, textbook name and Wednesday quiz convention were recorded. Its midterm 2 start is 8 a.m. on November 4 from Aaron's screenshot; the end time is unconfirmed. Only relevant academic details were transcribed. All supplied MATH 54 homework due dates are preserved in `semesters/2026-fall/math54/materials/request-schedule.txt`; due dates alone do not determine lecture coverage.

## Source collection since internet access was restored

The three remaining courses now have full-term schedules transcribed from their official pages: 15 Monday-based weeks each, with 11 historical weeks from August 24 through November 2. A separate source reviewer checked the dates, assignments, source identities and cached content. This source review does **not** approve any handout or teaching quality. No packets for these courses have been built.

- CS 61A: the Fall 2026 curriculum uses Gleam in the later historical weeks. Official lectures, readings, assignments, starter code, and real exams are cached with provenance. Legacy exam filenames were checked against PDF titles rather than assumed to identify the exam. HW8 and both Project4 specifications for the week starting November2 are not yet published, so that week cannot be claimed to have complete assignment coverage. The optional Hog Strategy Contest is preserved in the schedule.
- STAT 20: all historical public notes, worksheets, labs, tutorials, embedded R code and relevant source figures are cached. The final is December16, 7–10p.m. The homepage and syllabus disagree about the Quiz4-retake closing date; both dates are retained in the source index. Week2's class-survey CSV and question PDF are private Ed resources; Week10 Arbuthnot Lab questions1–3 require an image only on bCourses. Numerical answers dependent on those missing inputs must not be invented.
- MATH54: the official calendar, syllabus, HW1–11 section/exercise lists and lecture-week overlap are saved. Assignments spanning weeks are mapped by actual lecture sections, without inventing an exercise-level split. HW12–13 lists, lecture notes, practice exams and the exact custom textbook are unavailable publicly. An authoritative Lay4th-edition contents list gives a provisional topic map, with the custom-edition limitation explicit. Exact Nagle section headings still need authoritative confirmation. Section numbers from the linear-algebra and differential-equation texts are distinguished.

Workspace-local R and Gleam tools have been prepared and functionally checked for later examples; enable with `source /workspace/.berkeley-tools/activate-courses.sh`. No environment settings were changed or published. Official starter archives remain on disk; the versioned materials will include text/PDF, selected authentic code and source manifests, with redundant archive caches excluded locally from Git.

## Questions and prerequisites for continuation

1. Re-review and revise/regenerate every previously produced MATH 110 handout and solutions file against Aaron's reference packet; correctness and teaching quality both need fresh approval.
2. MATH 54 still needs `semesters/2026-fall/math54/materials/textbook.pdf` for exact assigned exercise statements. Without it, concept-only packets are still possible after the official section/topic and exercise lists become accessible; their problems must list section/exercise numbers without inventing statements.
3. STAT 20's homepage and syllabus now confirm the final on December 16, 2026, 7–10 p.m.; source collection must preserve the published details and flag conflicting quiz windows rather than silently choosing one.

Collect and validate the schedules and relevant materials, then continue handout production after the MATH 110 revision in the requested order: CS 61A, STAT 20, MATH 54. Continue one week at a time, with the same checks and per-week commit/rebase/push process. Include later weeks in the schedules but do not backfill packets starting on or after November 9.

Additional missing inputs to supply when available: STAT20's `class_survey_f26.csv` and `class_survey_questions_f26.pdf`, and the Week10 Arbuthnot parish-record image; CS61A's unpublished HW8 and Project4 specifications; the exact MATH54 custom textbook or its authoritative table of contents, particularly differential-equation sections4.2 and4.3 needed for the last historical week. These are recorded here instead of interrupting the work with questions.
