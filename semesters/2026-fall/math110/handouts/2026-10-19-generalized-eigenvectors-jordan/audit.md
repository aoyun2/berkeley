# Week 8 audit

Scope: Notes Chapters 14–15; LADR 8A–8C through Jordan form; Homework 8 P1–P7, including all optional problems; midterm2-review.pdf Problem 5. All materials preserved.

Coverage: Notes Definitions 37–40, Propositions 69–77 and Examples 61–63, plus every unnumbered example, Jordan power calculation and additive/multiplicative decomposition. Matching textbook coverage includes stabilized kernel/range decomposition, uniqueness of generalized eigenvalues, nilpotence tests and examples, multiplicities and characteristic polynomials, triangular diagonal counts, block forms, square roots of identity plus nilpotent and of invertible complex operators, and every matching textbook example. Trace starts in Week 9, following the notes' lecture order. The characteristic polynomial is defined intrinsically by generalized-eigenspace dimensions; no general determinant or later adjoint machinery is used.

Source clarifications: On the zero space the minimal polynomial and characteristic polynomial are 1; nilpotence/eigenvalue statements explicitly handle nonzero-space hypotheses. Cayley–Hamilton uses the nilpotence exponent bound on each generalized eigenspace of dimension d, justifying its factor exponent d. Jordan powers use j <= min(k,r-1), so zero eigenvalues never require negative powers. HW8 P4(b) explicitly retains dimension 5: without it, the three initial nullities alone do not force the requested block sizes.

Independent audit: a fresh agent `audit8`, with no drafting history, checked notes, textbook, HW8 and actual exam wording. Corrected nonzero-generalized-vector wording, the k >= 1 domain in the block-count formula, the dimension caveat, and added motivation explaining why arbitrary basis extension fails to construct chains. Final source/math/coverage approval received; independent SymPy spot checks passed.

Computation: `python scripts/checks/math110_week08.py` passed. Exact arithmetic verifies every displayed source matrix and power, shifted kernel, actual Jordan basis, block count and minimal polynomial, differentiation normalization, commuting binomial powers including zero eigenvalues, recursive square-root coefficients and matrices, all homework and exam computations.

Build/layout: both files built with `bash scripts/build.sh`, two passes, zero overfull boxes. Every final page was independently rendered and visually inspected: 14 handout pages and 2 solutions pages; no split boxes, unreadable figures or overflowing lines remain.
