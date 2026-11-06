# Week 1 — review against the supplied PDF

Current files: 15-page handout and 4-page solutions. The previous 14-page and 19-page revisions are superseded. Aaron explicitly rejected the staged figures and requested compact illustrative figures following his supplied PDF. The current review uses that actual PDF as the standard.

## Sources and coverage

Read Notes Chapters 1–2, HW1, matching LADR 4e §§1A–1C, and the saved Midterm 1 review II.7. The packet retains Notes Definitions 1–6, Propositions 3–7, Examples 1–9 and the unnumbered assertions on finite sets, field identities, F2, recurrence uniqueness, unions/sums and directness. Propositions 1–2 belong to the preceding proof-writing introduction, outside the assigned chapters.

Matching textbook examples include LADR 1.35(a–e), 1.37–1.39 and 1.42–1.44. The original source files remain intact; source identifiers are preserved, including the notes' older textbook-number citations. All HW1 P1–7 statements and solutions remain, including fixed-subset versus all-subset equality conditions. The extra problem is the actual Midterm 1 review II.7.

## Presentation

Read all 22 pages of `standards/reference/math110-quiz-minpoly-geneig.pdf`, including its actual rendered figures. Followed its blue result boxes, concise green proof motivations, numbered proofs, red examples, grouped Shortcuts/Traps and small static illustrations with short mathematical captions. Week 1 uses only its assigned subject matter.

The five compact figures illustrate function images/preimages, conjugation, union closure failure, a direct-sum decomposition, and nonunique three-line decompositions. They are integrated with the corresponding examples. Removed the full-page staged sequences and the unrequested interactive HTML/browser test. Their prior version is recoverable in Git; no original course materials were deleted.

## Independent audit and corrections

A fresh reviewer independently read the entire reference, original notes/homework, matching textbook sections, the revised handout and solutions, and every final rendered page. Correctness/coverage and reference-style presentation were judged separately. The reviewer requested exact textbook domains for continuous functions on [0,1] and differentiable functions on R, explicit complex-addition commutativity, and repair of sparse section-transition pages. These changes were made and rechecked. Final review reported no remaining blocking finding.

The local section wrapper now uses `Needspace` to keep a heading with its opening text without creating large artificial gaps after framed boxes. The problem set starts on its own final page, as a separate section in the supplied reference.

## Verification

- `python3 scripts/checks/math110_week01.py` passes with the local SymPy environment. It checks the displayed numerical/symbolic examples and answers, small finite-set identities, and the added coordinate-space textbook examples. The independent reviewer also recomputed the complex, F2, integral and vector examples.
- Both PDFs built with `scripts/build.sh`: no errors, zero overfull boxes.
- Root and the independent reviewer inspected all 15 handout and 4 solutions pages. Final renders are `/tmp/reference-week1-final/handout-01.png` through `handout-15.png` and `solutions-1.png` through `solutions-4.png`. Labels are readable and no box or solution is split; headings stay with their opening text.
- Handout SHA-256: `b50aea91f6ddd4acb416b8e1ab01fdc94cd9d266cdfd96acc38fbb410eb51ad7`.
- Solutions SHA-256: `1598158669de4ae4ad9eac6d12a2f43ae35beb1a8bd7c806c490e969ae70c5ee`.
- Original materials and the Weak spots section are unchanged. This review applies to Week 1 only; Weeks 2–10 still require revision.
