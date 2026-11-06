# Week 3 revised packet — independent review

Current version: 14 handout pages and 2 solutions pages. Earlier approval of the rejected version is superseded. This revision follows the supplied 22-page reference PDF directly.

## Sources and coverage

Read original Notes Chapters 5–6, Definitions 11–20, Propositions 18–27 and Examples 21–33, including recurrence shifts, Fourier-coefficient linearity, prescribed maps on sums/bases, rank–nullity, all coordinate/matrix calculations, representation-as-data context and stochastic conventions. Matching LADR 3A–3C (3.1–3.58) and the explicitly matched 3.65, 3.71–3.73, 3.76 and 3.78 are covered. All HW3 problems and subparts including optional P7 remain, with separate full solutions. Extra practice is the actual saved Practice Midterm 1 Question 2.

## Revisions and independent review

Replaced generic proof motivations with the equations that explain the choice: cancellation for T0, unique direct-sum/basis coefficients, the kernel relation needed for rank–nullity, basis-image columns, and row/column factorization. Restored missing actual textbook examples: polynomial multiplication/composition/integration; the multiplication/differentiation commutator; functional, shift and polynomial kernels/ranges; codomain-dependent surjectivity; rectangular matrices; column combinations; rank and transpose. Expanded derivative coefficients, evaluation images, antiderivative compositions, and Markov arithmetic.

Compact static illustrations show the N chain, the P/N kernel–range contrast, labelled evaluation columns, colored column combinations and the actual three-state transition graph. They use the adjacent examples and short mathematical captions. No staged/full-page or interactive supplement is used.

A fresh independent reviewer read the original notes, matching textbook/homework, saved exams and all 22 reference pages; separately reviewed correctness/coverage and teaching/reference style; then inspected every final PDF page. Earlier weak passages were checked in their actual revised forms. Both final verdicts PASS with no remaining changes. The reviewer corrected its own mistaken basis-citation suggestion; the packet accurately cites the basis criterion following Week 2 Definition 8.

## Verification

`python3 scripts/checks/math110_week03.py` passes exact symbolic, rational, complex, finite-field and probability checks for the old and newly restored examples. The reviewer independently executed the new-example and homework arithmetic checks. Both PDFs compile with no errors and zero overfull boxes. Root and reviewer inspected every final page: /tmp/math110-w03-final2/handout-01.png through handout-14.png, solutions-01.png and solutions-02.png. Handout pages 1–7 were additionally verified pixel-identical to the preceding inspected render.

Shared method-heading spacing now uses immediate Needspace rather than synthetic glue, removing avoidable page gaps while keeping readable text and figures. Original materials and Weak spots remain unchanged.

Handout SHA-256: b2e4e7f2e22b09981cae37d5b41eff7c24598596f69ec98b0b5a420be88fd12c.
Solutions SHA-256: d430eec528288a43cbae0e3f892c58e9af14459b5e0d8cc262980906cdaf64a1.
