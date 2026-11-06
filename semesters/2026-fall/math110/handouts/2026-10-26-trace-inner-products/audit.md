# Week 9 audit

Scope: Notes Chapters 16–17, matching LADR 8D and 6A, all HW9 P1–P7 including optional P7. Every numbered item appears: Definitions 41–45, Propositions 78–83, Examples 64–69. The entire unnumbered attention application is included: history/context, query/key/value dimensions, softmax and exact toy weights, score scale with explicit probabilistic hypotheses, learned linear maps, causal masking, matrix shapes/transposes, fixed Markov versus input-dependent attention, and explicit failure of linearity.

Textbook coverage includes the exact trace examples, cyclic products, characteristic coefficient and commutator obstruction; coordinate/weighted/function/derivative/exponential-weight inner products; norm and Cauchy–Schwarz forms and equality cases; triangle equality; parallelogram and polarization. Jordan–von Neumann sufficiency is explicitly cited as in the source, while necessity/formulas are proved. General-field projector trace is rank times 1_F; positivity claims are restricted to real/complex inner products.

Lecture-order decisions: LADR 8.55 needs orthonormal bases, taught in Chapter 18, so it is deferred to Week 10. Likewise the Pythagorean theorem and orthogonal decomposition in LADR 6.11–6.13 are developed in Week 10. HW9 P5(c) itself requires orthogonality, so its zero-inner-product definition (LADR 6.10) appears immediately before that problem. Cauchy–Schwarz uses direct expansion and no projection, orthonormal basis or adjoint.

Practice provenance: provided exam/review materials end at Notes Chapter 15 and contain no trace or inner-product problem. The extra problems are actual LADR 8D Exercise 1 and 6A Exercise 12, accurately labelled as textbook practice rather than invented exam questions.

Independent source/content audit: fresh agent `audit9` checked every requested source item, computations, proof order, literal wording and approved deferrals. Corrected early qbox terminology, literal invariance wording, placement of the orthogonality definition, and added the explicit Markov comparison. Final source/math/writing-order approval received; independent SymPy spot checks passed.

Computation: `python scripts/checks/math110_week09.py` passed. Exact checks cover traces, eigenpairs, characteristic coefficients, inner products and integrals/moments, symbolic complex polarization, attention scores/weights/transposes/causal normalization and nonlinear example, and every HW/practice computation. Reported decimal values are checked against exact expressions.

Build/layout: both TeX files built twice via `bash scripts/build.sh`, with zero overfull boxes. Parent independently inspected every final rendered page at original detail: 12 handout pages and 2 solutions pages. Unique final render paths avoided stale image artifacts; all 14 pages approved.
