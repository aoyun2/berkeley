# Week 8: independent new-reference review

Reviewer: review_math110_w08_explanation. Read-only repository review; scratch report only. Date: 2026-11-07. This review does not inherit any earlier approval.

## Material actually read

- standards/handout-standard.md and standards/teaching-quality.md, including the November 7 correction.
- New primary reference standards/reference/math110-quiz-minpoly-geneig_1.pdf: all 23 pages read as extracted text. Individually rendered and viewed reference pages 3, 4, 5, 13, 14, 15, 16, 17, 18, 19, 20 and 21 at 1350-pixel page height. The 23-page source, rather than the superseded 22-page PDF, governs this assessment.
- Original lecture-notes.txt Chapters 14–15 in full: Definitions 37–40, Propositions 69–77, Examples 61–63, displayed introductory/nilpotent/Jordan examples, powers and both Jordan–Chevalley decompositions.
- Original ladr4.txt and its verified Latin decoding aid /tmp/math110-restart-source/ladr-verified-latin.txt: 8A–8C numbered definitions/results and examples, explanatory body, chain-independence Exercise 8A.2, and positive integer roots after 8.41. Original extraction contains damaged font glyphs; the aid translates the prose while retaining recognizable mathematical glyphs.
- Original homework.txt HW8 P1–P7, including optional problems; saved actual midterm2-review.pdf P5 and final two assertions of P8.
- Entire current Week 8 handout.tex and solutions.tex; old rejected /tmp/math110-w08-before.tex.
- Executed scripts/checks/math110_week08.py independently: both reported groups passed (source matrices, kernels, bases, counts, powers, square roots, HW/exam answers, positive characteristic coefficients, integer roots).

## Specific old weakness and replacement

The rejected green box said: “In sum a_j N^j v=0, choose the smallest h with a_h nonzero. Applying N^(r-1-h) makes every later term zero and leaves a_h N^(r-1)v, a contradiction. The power is chosen to reach the last nonzero iterate exactly.” The following proof repeated precisely these instructions.

That omitted the discovery: applying N changes every term of a relation simultaneously; later terms reach zero before the first term does. Neither the smallest index nor the exponent was made visible to a reader learning the trick.

The replacement starts with the actual relation av+bNv+cN²v=0 and writes the two resulting equations aNv+bN²v=0 and aN²v=0. Since N²v is nonzero, back substitution gives a=b=c=0. Its labelled chain figure identifies the same a,b,c at their starting vectors. This adds mathematical information: the reader can see what changes after each application, why two applications isolate a, and why fewer applications leave another unknown. The general proof then handles arbitrary length by removing the coefficients in order. It avoids the old unexplained choice of the first nonzero coefficient. The formula r-1-h can be derived by requiring N^h v to reach N^(r-1)v; a short equation h+q=r-1 would make that last translation maximally explicit, but the small case and current proof already provide the underlying reasoning.

## Source/correctness verdict

Current source coverage and substantive mathematics: PASS, subject to the small field-condition correction below and final review of any subsequent edits. All weekly Notes numbered content, LADR main results/actual examples and useful body consequence, HW8 including optional questions, and accurately attributed real exam additions are present. Correct distinctions are made between geometric multiplicity, algebraic multiplicity, and minimal-polynomial exponent. Zero-dimensional exceptions, non-complex obstructions, characteristic-2 binomial coefficients, and HW4's ambient dimension are handled. Root construction does not assume convergence. No new omitted theorem or major proof gap found.

Action C1: the nilpotent shortcuts currently say “To turn derivatives into unit chain steps, use 1,x,x²/2!,...,x^m/m!” under the packet's general field F convention. Add “over R or C” to this shortcut (or another explicit characteristic-zero condition). The nearby example is real, but the shortcut itself lacks its necessary condition.

## Teaching/reference/concision verdict

Specific chain-independence replacement: PASS. It meets the November 7 correction by calculation before indices, rather than colouring the same proof twice.

The other rewritten motives mostly explain a choice: why Av fits the known adjacent-kernel equality; why first-power kernel/range dimensions are insufficient; why a selected generalized vector is first converted to an ordinary eigenvector; why the invariant remainder has smaller dimension; why separate upper bounds become equalities by comparing their totals; and why square-root coefficients are chosen one at a time. The root small case displays R² and its two coefficient equations. These match the concise task/operation/obstruction standard of the actual reference pp. 13–20.

The new lifting figure carries explanatory content: the old image-space chain is marked, the added preimage edge is coloured, and the caption distinguishes lifting from adding length-1 kernel chains. The actual Example 62 chain gives numerical vectors and basis order; the nullity figures show growth, stabilization, and first differences; the displayed partitioned source matrices identify coordinate groups and zero blocks. These use the reference's compact static style rather than decorative space arrows.

Action T1 before final approval: Proposition 75 proof steps 3–4 still contain the old compression “the old basis ... forces all coefficients except ...” and “by applying N to the old chain basis.” The lifting motive explains why range/preimages/kernel are natural, but the multi-chain independence mechanism should show one compact actual relation before/after applying N (one or two short chains suffice), identifying which endpoint coefficients remain. This is the same standard as the user's chain-independence criticism, applied to a second central argument. Avoid duplicating an entire general proof in a new box.

No request for more pages, more figures by count, or duplicated motivation for immediate consequences. Final-page layout and exact PDF approval remain PENDING; parent will provide final PDFs/renders. Every final page must be viewed individually, then the final approval must name the PDF SHA-256 values.

## Final candidate re-review and release verdict

Both findings are RESOLVED in the frozen candidate. C1 now explicitly says “Over R or C” before the factorial shortcut. T1 now writes a relation sum c_j u_j + u = 0 with u in U, applies N to get sum c_j v_j + Nu = 0, and explains that Nu uses only old chain positions below the tops. The top coefficients therefore vanish separately. This also supplies the stated calculation for L intersect ker N = U intersect ker N; extending the kernel basis and matching Nv then establish independence and spanning. This is a short explicit derivation rather than a repeated labelled instruction.

I re-read the final Proposition 75, final Jordan-data proof (including explicit polynomial division and nilpotence of K), all changed solution Idea lines and the full final solutions. The improved differentiation Idea explains why dividing by j! produces unit coefficients; optional HW5 connects the repeated nullity to the dimension and decreases of first differences to chain endings; HW6 distinguishes counting all directions from reaching the longest chain. No new correctness or prerequisite gap found.

I individually viewed EVERY final page, using /tmp/math110-w08-newref-v3/handout-01.png through handout-14.png and solutions-01.png through solutions-02.png. This was a fresh all-page inspection, not reliance on unchanged-page comparison. Page-by-page: 1 tools/generalized chain/equality choice; 2 stabilization plot and kernel/range split; 3 actual kernels and distinct-eigenvalue argument; 4 nilpotence tests/examples; 5 three-vector relation and lifting motivation; 6 explicit lifting proof/figure/examples; 7 decomposition/multiplicities; 8 triangular-count argument/determinant comparison; 9 actual invariant block matrices/Jordan definition; 10 Jordan existence/data/count motivation; 11 nullity plot/numerical Jordan chain/Examples 62–63/nonsimilarity; 12 powers and decomposition; 13 square-root coefficient calculation and proofs; 14 all homework and real exam problems; solutions 1 HW1–4; solutions 2 optional HW5–7 and both exam questions.

All mathematical labels, numerical matrices and arrow labels are readable. Figures are placed with the relevant calculation, the coloured preimage edge and marked old chain are clear, the nonzero endpoint in the three-vector figure agrees with the calculation, and the plotted differences match the numerical data. Boxes, headings, problems and solutions are intact. No overlap, clipping, blank page, or disproportionate unexplained gap found. Logs contain no overfull or underfull warnings. The numerical checker was run again on the frozen candidate and both groups passed.

**Final source/correctness/full weekly coverage verdict: PASS.**

**Final teaching/new-reference/ideas/reconstruction/concision/figures/layout verdict: PASS.** The central rejected argument is now reconstructible from its small calculation. Other central motives identify the needed choice and its reason; routine consequences use short derivations. No unresolved findings.

Approval binds only to these final PDF bytes, independently recomputed after the page inspection:

- handout.pdf: 14 pages, SHA-256 0c0ed0c835aca5c335eb727ec10e83629eabaec52fb6cbe8bf31677b74840264
- solutions.pdf: 2 pages, SHA-256 1635c331614232c99d3a7612fb9499c180775c658cf7315aa6138e3561c84e16


## Author final verification

Root read the newly attached 23-page reference itself and the full revised handout/solutions. Root individually viewed all 16 v1 pages, then individually viewed final h6, h10, s1 and s2; exact PNG comparisons show the other 12 final pages are identical to those viewed v1 pages. Final renders: /tmp/math110-w08-newref-v3/. No overfull boxes. The full original Week8 numeric verifier passes. This revision remains 14 handout pages + 2 solutions pages.

This new review supersedes the earlier teaching-quality approval rejected by the user. In particular the former smallest-index shortcut has been replaced by a three-vector calculation and a coefficient-by-coefficient general proof; lifted-chain independence now shows the actual relations. All original materials and the exact Weak spots section are unchanged.
