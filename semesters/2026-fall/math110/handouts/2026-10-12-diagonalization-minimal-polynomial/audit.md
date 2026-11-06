# Week 7 audit

Scope: Notes Chapters 12–13, LADR 5B and 5D, Homework 7 (all seven problems, including optional P4/P7), and midterm2-review.pdf Problem 6.

Coverage: Notes Definitions 33–36, Examples 53–60, Propositions 59–68; matching textbook polynomial/eigenvalue/minimal-polynomial results, all exact textbook examples, cyclic computation, invertibility, quadratic-kernel parity, odd real dimension, diagonalization, and Gershgorin. Includes the notes' unnumbered stochastic powers, spectral gap, PageRank restriction and Fibonacci calculation. Earlier-week prerequisites have reasons and week references. No Jordan form, general determinant, or later characteristic-polynomial machinery is used.

Independent source/content review: fresh agent `audit7`, with no drafting history, checked notes, textbook, homework and the actual exam statement. Corrected the complete-list eigenvalue hypothesis, zero-space conventions, explicit prerequisite definitions, textbook example omissions, result labels, intermediate-degree justification and numbered reasoning. Final review approved with no remaining substantive findings. Reviewer independently ran exact numeric checks.

Computation: `python scripts/checks/math110_week07.py` passed. It checks matrix relations and minimal polynomials, every numerical eigenpair and basis, the high power, Fibonacci, stochastic formulas and errors, quartic factorization/inverse, affine substitutions and interpolation projections using exact SymPy arithmetic.

Build/layout: both files built with `bash scripts/build.sh`, two passes each, zero overfull boxes. Parent independently viewed all 16 final handout pages and both final solutions pages at 1500-pixel render resolution. Corrected a crowded consecutive list on handout page 10 and separated each solutions heading from its Idea line; changed pages were re-rendered and re-viewed. Byte comparison confirmed the other handout page images were unchanged. All 18 final pages approved.
