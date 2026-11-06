# Week 2 — ideas and reconstruction revision

Current version: 11 handout pages and 2 unchanged solutions pages. This supersedes the earlier 13-page presentation after Aaron clarified that the goal is to understand ideas, intuition and motivations and reconstruct every LADR result from memory. Page count alone is not the quality criterion.

## Organizing arguments and coverage

The packet explains four reusable arguments: subtract two representations to test uniqueness; solve a nontrivial relation for an entry to delete it; replace entries in a spanning list to bound independent-list length; choose an intersection basis first and count it once. Immediate consequences now use concise derivations instead of repeating a green motivation and the same full argument. Related basis/subspace/complement tests share one statement and proof. Actual source examples remain, with their equations and field restrictions.

Coverage remains Notes Chapters 3–4, Definitions 7–10, Propositions 8–17, Examples 10–20 and optional cited infinite-set assertions; matching LADR 2A–2C results and standard examples; all six HW2 problems and subparts; and the actual saved Practice Midterm 1 Question 1. Formal polynomial versus function distinctions, degree of zero, nonzero-generator qualification, finite-dimensional hypotheses and R/C restrictions on numerical divisions remain explicit. No rank–nullity or later linear-map theory is introduced.

## Two-of-three criterion

The previous packet only stated one implication in Shortcuts. The complete organizing criterion is now a prominent boxed statement on page 9: for subspaces U,W of finite-dimensional V, any two of dimU+dimW=dimV, U intersection W={0}, and U+W=V imply the third. All three implications are derived explicitly from the dimension formula, using the full-dimension subspace test where needed. The statement and its proof stay on one page.

The compact array on page 10 distinguishes the common basis, the U-only and W-only extensions, and directions missing from U+W. Its caption derives (r+k)+(r+l)=r+k+l+s iff r=s; zero intersection means r=0, and full sum means s=0. This supplies an explanation of why any two conditions force the third, beyond merely memorizing a test. HW2 P5 now points at the full criterion. Dimension is introduced in Week 2 in this schedule, which explains its placement here rather than in Week 1 before its prerequisites.

## Separate independent reviews

The reviewer reread the updated standards and original notes, then the entire revised source and all final rendered pages. Correctness/coverage PASS: all original claims, examples, field safeguards, homework/exam parts remain; the grouped proofs and full criterion are valid. Ideas/reconstruction and direct-reference style/layout PASS: the shared arguments produce the short consequences, the common/missing basis figure explains the criterion, and the compact figures/labels/pages are readable. Four unnumbered proof paragraphs were converted to concise numbered steps as requested; no extra motive boxes were restored. Further grouping of the dimension tests and shorter deletion/span calculations was reread and approved.

Every final page was inspected by root and reviewer. Final3 handout pages 1–8 are pixel-identical to inspected final2; pages 9–11 were re-inspected after the atomic statement/proof grouping. That layout correction avoids guessed space reservations and keeps the entire problem set on page 11. Handout renders: /tmp/math110-w02-ideas-final3/handout-01.png through handout-11.png. Solutions: /tmp/math110-w02-ideas-final2/solutions-01.png and solutions-02.png; the PDF is byte-identical to the prior reviewed version.

## Verification

`python3 scripts/checks/math110_week02.py` passes all exact numeric/symbolic textbook, homework and exam calculations; the reviewer independently ran it. The revised handout builds with no errors and zero overfull boxes. Source coverage accounting and field checks were independent of compilation. Original materials and Weak spots remain unchanged.

Handout SHA-256: 1d9b913ad3d72bed7606b499f4103fef9b0926235fda291fdcaafac675834f03.
Solutions SHA-256: 8fbe478c142f2dea5c49577fa907ef8dc7979a2af1b4815c8ada8f87ad64d0e7.
