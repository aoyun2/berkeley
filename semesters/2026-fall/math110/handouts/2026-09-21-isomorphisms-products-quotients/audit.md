# Week 4 revised packet — independent review

Current version: 14 handout pages and 3 solutions pages. Previous approval of the rejected packet is superseded. The revision follows the supplied reference PDF directly, with short motivations, explicit worked mathematics and compact static illustrations.

## Sources and scope

Read original Notes Chapters 7–8, printed pp.57–67: Definitions 21–24, Propositions 28–39, Examples 34–42 and the unnumbered inverse/product/quotient arguments. Matching textbook coverage is all LADR 3D (3.59–3.86) and 3E through 3.103. Earlier coordinate tools are restated with their equations and reasons. All HW4 problems/subparts including optional P7 are preserved with separate full solutions. Extra practice is actual saved Practice Midterm 1 Questions 2 and 3, plus Midterm 1 Review Section II Exercises 9 and 10.

No quotient map, quotient dimension, first isomorphism theorem or duality is introduced early. Preserved source corrections: Notes Proposition 36 matches LADR 3.92, not the notes' 3.76; infinitely many right inverses requires an infinite field; HW4 P7 lacks the necessary linearity hypothesis. The typed practice Q3 controls its map: the saved scanned solution changes that map and its identity-matrix answer must not be copied.

## Revisions and independent review

Replaced all 19 old generic motivations with actual equations explaining the choice. Elimination produces the adjugate entries; differences prove inverse linearity and coset equality; rank–nullity gives the equal-dimension criterion; restricting the intermediate range gives invertible factors; two coordinate routes give QA=DQ. Separated transition/inverse identities from the change-of-basis theorem. Expanded coefficient calculations for multiplication by x² and derivative-zero polynomials, and wrote both matrix inverse equations with aligned bases.

Restored actual textbook examples 3.74 (polynomial coordinates), 3.88 (product arithmetic), 3.96/3.98 (parallel lines and planes) and 3.100 (quotient elements). Compact figures show the actual interpolation points and 1+x² curve, the two numerical basis vectors and coordinate transition, independent product components, and labelled cosets including the whole zero coset. Root found two small label collisions in the coset picture; both were corrected and visually rechecked.

A fresh separate reviewer read the original notes/homework, matching textbook, saved exams, and the full reference. The reviewer read the revised sources and inspected every rendered handout and solutions page, then rechecked the final corrected figure. Correctness/coverage and teaching/reference style/layout received separate PASS verdicts with no unresolved findings. Minor source/wording findings (Eij definition, restricted-factor wording, concrete section question, capitalized solution sentence) were corrected before final review.

## Verification

`python3 scripts/checks/math110_week04.py` passes exact inverse, coordinate, polynomial, finite-field, interpolation, tuple and coset calculations, including all new numerical examples. Independent SymPy verification also passes. Both PDFs built without errors and with zero overfull boxes.

Root and reviewer inspected all 14+3 final pages at readable scale. Handout renders: /tmp/math110-w04-final3/handout-01.png through handout-14.png; solutions: /tmp/math110-w04-final/solutions-01.png through solutions-03.png. All handout pages except page 13 were verified pixel-identical after the final label corrections; page 13 was explicitly re-inspected. Original materials and Weak spots are unchanged.

Handout SHA-256: 71a58ddcb331c1b8d5d8825b45eb434dc714281d4b152022ba5e8c3a7ba14494.
Solutions SHA-256: 57e7ed7016e4b5e1d40d92da956be9e484ad40f3641a723d21de89eb5a6d8335.
