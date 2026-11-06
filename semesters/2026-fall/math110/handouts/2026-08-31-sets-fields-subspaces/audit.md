# Week 1 revised packet — review record

Current files: **19-page handout and 4-page solutions**. Aaron rejected the previous figures; all five have now been replaced. The visual reviewer examined the prototypes and the integrated packet, withheld approval for specific explanatory/layout problems, and approved the corrected final render. Root independently inspected all 19 handout pages and all 4 solutions pages. This records the review of this revision; it does not assert parity with 3Blue1Brown or approval from Aaron.

## Current visual revision

- **Page 3, images/preimages:** one fixed function, with changing selections. Pink branches show the extra inputs introduced by taking the preimage of an image; the unattained output changes from selected gold to dashed gray when it cannot return. All function arrows remain directed from inputs to outputs.
- **Page 6, reciprocal:** the failed multiplier 1/3 misses the target 1. The equation `3d+4c=0` determines `d=-4` after choosing `c=3`. The multiplication table and contribution diagram expose the cancelling imaginary terms. Dividing all contributions by 25 produces 1; the enlarged unit scale is stated explicitly.
- **Page 13, union/sum:** translating the same gold vector shows addition; both nonzero coordinates place the resulting vector on neither axis. A separate construction reaches an arbitrary target, including the illustrated negative second coordinate.
- **Page 16, direct sum:** the target remains (4,2) while the first summand changes. Two failed residuals have nonzero coordinate sum. The successful residual lies in W, and the single intersection of `x+y=6` with U explains why the first summand must be (3,3).
- **Page 18, three lines:** the same target (1,1) is reached by three changing triples. The diagonal summand increases from zero to half to the entire target while the axis summands decrease. This visibly disproves uniqueness despite pairwise zero intersections.
- The TikZ sources are in `figures/`. Prose, source coverage, assigned problems and solutions from the prior corrected revision are retained; layout changes keep the full-page diagrams intact and group the related text.
- Added `vector-explorer.html`, a self-contained offline supplement using the direct-sum example and the same colour meanings. Initial trials conceal the solved decomposition; reaching t=3 or requesting uniqueness reveals it. Instructions stay outside the plot, and the endpoint line is labelled directly.

## Corrections required by the visual review

The reviewer required a visual uniqueness argument rather than a repeated final decomposition, direct labels on the translated endpoint lines, explicit tests for failed residuals, a concrete recovery question for the function example, the calculation selecting the conjugate, and an explicit change-of-scale annotation. Final integration exposed a proof-only page and a caption touching an axis label; both were corrected and rechecked. Pale vertical lines in the three-line diagram were shortened to clear the headings. No remaining overlap, clipping, legibility or definitions-before-use issue was reported.

## Executed verification and final inspection

- `python3 scripts/checks/math110_week01.py` passes with the local SymPy environment. Added exact checks for the failed multiplier, cancellation/normalization, all three direct-sum trials, and the three-line family `(1-t,0)+(0,1-t)+(t,t)=(1,1)`.
- Both PDFs built with `scripts/build.sh`: no LaTeX errors, zero overfull boxes.
- The explorer's mathematical model passes all 81 parameter states. `python3 scripts/checks/math110_week01_visual.py` passes actual Chromium checks for those states, arrow colours/endpoints, trial controls, keyboard, point dragging, exact playback landing at t=3, both answer-reveal routes, uniqueness and a narrow viewport. No JavaScript errors. The harness loads the exact repository HTML into an offline browser context; managed Chromium blocks direct `file://` navigation.
- Final handout renders: `/tmp/week1-visual-final2/handout-01.png` through `handout-19.png`. Root inspected pages 1–14 from the preceding render, then verified those final images byte-identical; root inspected final pages 15–19 directly. Solutions: `/tmp/week1-visual-final/solutions-1.png` through `solutions-4.png`, all inspected directly. The independent reviewer inspected the entire integrated packet and rechecked the corrected final pages.
- Final handout SHA-256: `2159375d019c1bd7b4ee217667ff917f940548476f1b97804b4e2a610f3c0bf1`.
- Final solutions SHA-256: `71226599b9a6112468cbd847facc33e93fed90a6d957834f3d56d9f443dd6110`.
- The original materials and Weak spots section are unchanged. Weeks 2–10 still require their own revision and review.

## Prior source/prose review — historical 14-page revision

The following records the independent source and prose review of the preceding 14-page handout and 4-page solutions. Its original figures were subsequently rejected. Its source/prose checks remain relevant to the retained text; its former visual approval does not approve the current figures.

### Sources and scope

- Read the full Notes Chapters 1–2 in `materials/lecture-notes.txt` (the Chapter 1 heading is at line 451; the Chapter 3 heading is at line 919). Definitions 1–6, Examples 1–9 and Propositions 3–7 are retained. Propositions 1–2 are in the preceding proof-writing introduction, outside these assigned chapters.
- Retained the unnumbered finite-set assertion, field identities/inverses/cancellation, the notes' cubic calculation, complex-field verification, conjugation and reciprocal formulas, the F2 tables and field laws, unique vector zero/inverses/cancellation, function and sequence spaces, the scalar-field distinction, subspace test, recurrence uniqueness, failure of union closure, the smallest-subspace assertion for sums, and the three-line counterexamples to pairwise directness and distribution over sum.
- `materials/homework.txt`, HW1 P1–7, supplies the week's original assignment. Retained the recovered LADR 4e statements for 1A.7, 1B.2, 1C.4 and 1C.5; the glyph-damaged original `materials/ladr4.txt` is preserved. No exercise statements were guessed or substituted. Extra practice remains the real `materials/exams/midterm1-review.pdf`, Section II, Exercise 7.
- Sources: Alan Hammond, Math 110 Fall 2026 lecture notes; HW1; Sheldon Axler, *Linear Algebra Done Right*, 4th ed., matching portions of §§1A–1C. LADR is CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/). Source identifiers remain attached to the rewritten explanations.
- Read `standards/handout-standard.md`, `standards/teaching-quality.md`, and Aaron's positive reference `standards/reference/math110-quiz-minpoly-geneig.pdf`, including the actual rendered pages 5, 13 and 14. The reference supplied explanation and figure quality examples, not later-week mathematical content.

### Substantive revisions

- Replaced vague section questions and proof motivations with concrete tasks, available equations, the obstruction to an immediate attempt, and the reason for choosing the next operation.
- Images/preimages: computed both composites on one four-input function; added the corresponding element-and-arrow diagram, including repeated inputs and an unattained output. Solutions prove fixed-subset equality conditions separately from the conditions for every subset, with nontrivial equality and strictness examples.
- Complex arithmetic: displayed every multiplication and collection step for the original numeric examples and cubic. Explained the conjugate choice by requiring imaginary part `ad+bc=0`, then dividing by `a²+b²`. Added a reflection plot plus an enlarged reciprocal plot with actual fractional coordinates.
- Vector spaces: split Examples 5–7, added concrete tuple and evaluated-function calculations, and showed the coordinate/input equations proving the axioms. Expanded the zero-scaling motivation without assuming the facts being proved.
- Subspaces and sums: showed substitution in defining equations, the recurrence's successive symbolic entries and uniqueness argument, and the regrouping proving sum closure for two or more subspaces. Added useful union-versus-sum and three-line nonuniqueness diagrams.
- Direct sums: subtracted two representations explicitly, explained both intersection memberships, and used the largest differing index to give a complete uniqueness argument. Solved both coordinate equations for the diagonal-line example, with the actual summands labelled in its diagram.
- Rewrote every homework/exam solution with a choice-of-argument Idea line and explicit numbered steps. No later-week terminology or results are required. Elementary calculus continuity, derivative and integral rules are explicitly cited where used.

### Executed checks and page inspection

- `source /workspace/.berkeley-tools/activate.sh`; `python3 scripts/checks/math110_week01.py` passes. It checks all original/new numeric examples, symbolic complex identities and associativity coordinates, reciprocal coordinates, repeated squaring over F2, the real eighth-power coefficients, tuple/function examples, integral, symbolic recurrence entries, subspace equations/decompositions, and exhaustive small finite-set image/preimage identities.
- Built `handout.tex` and `solutions.tex` with `bash scripts/build.sh`: no LaTeX errors; zero overfull boxes in each log.
- Final second draft: **14 handout pages; 4 solutions pages**. Rendered all final pages at 1400-pixel longest dimension with `pdftoppm` and inspected every page, including the smallest fractional plot labels, arrow endpoints, captions, box boundaries, headings and complete problems/solutions. Fixed the draft caption separation and red-box heading overlap before this final pass.
- Current local review images: `/tmp/week1-revision2b-render/handout-v2b-01.png` through `handout-v2b-14.png`; `/tmp/week1-revision2b-render/solutions-v2b-1.png` through `solutions-v2b-4.png`. Inspected every page of these newly rendered files after the second-draft rebuild. Figures and captions remain together; no boxes or problems/solutions split. Files under the previous `/tmp/week1-render/` prefix are superseded.
- A fresh independent review withheld release of the first draft for specific textbook-coverage omissions and wording issues. The requested second-draft corrections below are complete; the independent recheck has now approved them. No commit, pull/rebase, push, course-log approval, or later-week work was performed by the author; release actions are coordinated by root.

### Second draft: corrections requested by fresh review

- Verified the exact textbook statements against the untouched glyph-encoded original `materials/ladr4.txt` and the reviewer's scratch English decoding `/tmp/week1-review/ladr-decoded.txt`, lines 1518–1645. The decoding is a scratch aid, not a replacement source file. LADR 1.39 is correctly identified as an equation within Example 1.38.
- Added LADR 1.35(d): differentiable real-valued functions on `(0,3)` satisfying `f′(2)=b` form a subspace of `R^(0,3)` exactly for `b=0`. Proved necessity with the zero function and sufficiency with the derivative calculation at 2; included `(x−2)²` to distinguish the derivative constraint from a zero function.
- Added LADR 1.35(e): complex sequences tending to zero form a subspace of `C^infinity`. Defined convergence to zero and cited the elementary real-limit laws before use; displayed both real coordinates of `(a+bi)z_n+w_n` to verify closure for complex scalars.
- Added the actual generic-sum computation from LADR Example 1.38 and equation 1.39: add `(a,a,b,b)` and `(c,c,c,d)` to derive equal first two coordinates, then construct `(x,x,y,z)=(x,x,y,y)+(0,0,0,z−y)` for the reverse inclusion. Explained why matching the first three coordinates is a useful choice and why the first inclusion alone does not prove equality.
- Answered the field section's opening equation task: derived the only possible solution of `ax=b` for nonzero `a`, verified substitution, handled both cases with `a=0`, and worked `2x=1` over the reals.
- Made the complex-inverse first attempt explicit: choosing `(c,d)=(1/a,0)` yields `(a+bi)(1/a)=1+(b/a)i` for `a≠0`, so the remaining imaginary term explains the need for a different choice. If `a=0`, this attempted inverse is unavailable.
- Replaced the ambiguous conjugation trap with the explicit false multiplication claim about real parts, using `w=z=i`. Changed the P3 solution's name for `c0=0` to the multiplication-by-zero identity.
- Expanded and reran `scripts/checks/math110_week01.py` for the added algebra, derivative and complex-coordinate calculations. Both PDFs rebuilt with zero overfull boxes. All 14+4 pages rendered under the new prefix above and visually inspected. Existing improvements and original exercises remain in place.
- Author submitted stable revision 2b without claiming independent approval. The independent reviewer then approved both correctness/coverage and teaching quality after examining all 18 final pages. Root separately inspected the final pages and reran the exact check script.

### Independent release decision

The fresh reviewer read the positive reference, the original notes/homework and matching textbook sections independently of the writing. Approval explicitly covers: the traced input/output selection; the chosen complex coordinates and their cancellation; the two separate inclusions for the F4 sum; the choice to compare the largest differing summand; and the distinction between fixed-subset and all-subset equality in the solutions. The missing textbook examples and ambiguous real-part trap were corrected before approval. No remaining source, mathematics, teaching or layout finding was reported.

Root also verified the new field method answers its opening question, each diagram explains the nearby equations, all 14+4 final pages are readable, the exact checks pass, and the original Weak spots section is unchanged. This approval applies to Week 1 only; Weeks 2–10 of the previous release still require regeneration/review.
