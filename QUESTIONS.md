# Backfill summary and questions

## Completed: MATH 110 weeks 1–10

Built and pushed all ten homework weeks starting on or before 2026-11-02, in week order. Each folder contains `handout.tex`, `handout.pdf`, `solutions.tex`, and `solutions.pdf`. Total: **20 PDFs, 151 pages** (131 handout pages and 20 solution pages).

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

All packets passed exact computation checks, a separate independent source/content audit, and visual inspection of every final PDF page. Builds have no overfull boxes. Verification scripts are in `scripts/checks/math110_week01.py` through `math110_week10.py`; activate the tools with `source /workspace/.berkeley-tools/activate.sh`. Each completed week was logged, committed, pulled with rebase, and pushed to `main` before the next week.

Coverage includes all numbered lecture-note definitions, results and examples, matching textbook results/examples, all assigned problems including optional problems, and appropriately sourced extra practice. Extra problems use real saved exams where their coverage applies; later topics without applicable saved exam problems use explicitly identified textbook exercises. No invented exam provenance is used.

Source caveats are identified explicitly in the packets: missing linearity hypotheses in some homework statements, finite-field qualifications, the zero-dimensional minimal-polynomial exception, trace interpreted as a field scalar, orthogonal versus orthonormal formulas, and analytic ingredients that need citation. These corrections leave the original source materials intact.

## Cleanup and preservation

- Removed exactly the requested MATH 110 `handouts/archive/` and `handouts/2026-11-06-ch13-18-review/` directories and their obsolete log lines.
- Preserved every pre-existing materials file. The original Weak spots section is byte-for-byte unchanged.
- Fixed `scripts/build.sh`: an explicitly requested source now takes precedence over a template with the same basename, and LaTeX failures propagate. Verified both source selection and failure handling.
- No handouts starting on or after 2026-11-09 were created. MATH 110's future weeks remain in `course.toml` for the separate scheduled job.

## Remaining: CS 61A, STAT 20, MATH 54

These three courses' weekly schedules, source collection and handout backfills are **not complete**. Requests to their supplied websites are rejected by the cloud environment's proxy before reaching the sites (`Tunnel connection failed: 403 Forbidden`). This is an environment access blocker, not evidence that the pages are missing or need website credentials.

The most recent runtime check still reports the original **restricted, enforced policy, revision 1, with no custom allowed hosts**. Aaron showed an editor screenshot with all public internet access enabled, but that setting has not reached this running task. Required domain additions were saved in the environment draft:

- `math.berkeley.edu`
- `cs61a.org`
- `stat20.berkeley.edu`
- `composingprograms.com`
- `www.composingprograms.com`

The exact source URLs are:

- https://math.berkeley.edu/~kwohm/Syllabus54-FA26.html
- https://math.berkeley.edu/~kwohm/Calendar54-FA26.html
- https://math.berkeley.edu/~kwohm/Homework54-FA26.html
- https://cs61a.org/fa26/
- https://stat20.berkeley.edu/fall-2026/

No lecture topics, week starts, homework exercise lists or inaccessible course materials were invented. The existing CS 61A and MATH 54 final dates were retained. MATH 54's supplied midterm dates, textbook name and Wednesday quiz convention were recorded. Its midterm 2 start is 8 a.m. on November 4 from Aaron's screenshot; the end time is unconfirmed. Only relevant academic details were transcribed. All supplied MATH 54 homework due dates are preserved in `semesters/2026-fall/math54/materials/request-schedule.txt`; due dates alone do not determine lecture coverage.

## Questions and prerequisites for continuation

1. Apply the saved public-internet setting or domain additions to this task's running environment. Save and publish the updated environment settings; if already done, the remaining issue is policy propagation to this instance. Retry the actual pages after the runtime policy changes.
2. MATH 54 still needs `semesters/2026-fall/math54/materials/textbook.pdf` for exact assigned exercise statements. Without it, concept-only packets are still possible after the official section/topic and exercise lists become accessible; their problems must list section/exercise numbers without inventing statements.
3. STAT 20's final date remains TBD until its official schedule can be checked.

Once access works, collect and save the schedules and relevant materials, then continue handout production in the requested order: CS 61A, STAT 20, MATH 54. Continue one week at a time, with the same checks and per-week commit/rebase/push process. Include later weeks in the schedules but do not backfill packets starting on or after November 9.
