# Week 1 — ideas and reconstruction revision

Current version: 14 handout pages and 4 unchanged solutions pages. This supersedes the preceding 15-page presentation after Aaron clarified the goal: understand the ideas, intuition and motivations and reconstruct every LADR result from memory. The review evaluates the organization of the reasoning, not merely page count.

## Shared arguments and explicit criteria

- Membership determines set identities and image/preimage formulas. The main packet now states both exact image/preimage identities and their equality conditions, distinguishing a fixed subset from every subset. The existing function picture illustrates attained/missing outputs and shared outputs.
- Undo a common operation using its inverse. Vector zero/inverse uniqueness reuses the earlier additive proof; distributivity plus cancellation gives scalar-zero identities; av=0 iff a=0 or v=0 is explicit and follows by applying a nonzero scalar inverse. No division by a vector is used.
- Check one input. A joint proof verifies the tuple/function/sequence vector-space axioms using field identities at each input. Each source example retains its own operations, zero, negatives and numerical examples. The list definition explicitly distinguishes ordered/repeated entries from sets.
- Test what can fail in a subset. The subspace test includes its nonempty/two-scalar formulation. Coordinate, derivative and integral zero conditions share a fully specified rule L(au+v)=aL(u)+L(v); L0=0 and closure at zero are derived once. Each actual source rule is checked, with calculus facts cited. No undefined linear-map/kernel terminology is imported.
- Subtract decompositions. Directness first becomes the trivial-zero-sum criterion; uniqueness follows by subtracting two representations. The ordered intersection criterion and both converse directions are explicit. Coordinate decompositions and the three-line counterexample instantiate that argument.

Meaningful organizing criteria previously implicit are now explicit: union is a subspace iff one subspace contains the other; a finite sum is the least subspace containing every summand; and the image/preimage equality criteria above. Added the actual LADR 1.2 product (2+3i)(4+5i)=-7+22i. The full dimension two-of-three criterion is in Week 2, where dimension is introduced and proved; no undefined dimension/basis theorem was inserted into Week 1.

## Coverage and independent review

Fresh reviewer read original Notes Chapters 1–2 (printed pp.13–25), Definitions 1–6, Propositions 3–7, Examples 1–9 and unnumbered arguments; matching LADR 1.1–1.46; HW1 P1–P7 with all parts; actual saved Midterm 1 Review Section II Exercise 7; and the supplied 22-page reference. Original complex/F2 calculations, real cubic example, null-sequence example, recurrence, all textbook subspace/sum/direct-sum examples and field restrictions remain. Every original material file and Weak spots is preserved.

The reviewer separately APPROVED mathematical correctness/coverage and ideas/intuition/motivations/reference style/layout. It checked the actual replacement arguments, not just source identifiers or compilation. Findings corrected before final approval: move the list definition before its first use; remove a premature vector-addition sentence in the field section; state precise derivative-interval reuse. All five compact static illustrations remain tied to the actual adjacent examples. No staged or interactive supplement was added.

## Verification

`python3 scripts/checks/math110_week01.py` passes exact complex arithmetic, polynomial/F2, finite-set and source-example checks, including the newly restored textbook product. The reviewer independently checked the products/powers, homework cube root and F2 expansion. The handout builds with no errors and zero overfull boxes; solutions are byte-identical to the reviewed preceding version.

Root inspected all 14 handout and 4 solutions final pages individually. The reviewer inspected all pages and rechecked each changed final2 page. Handout pages 2, 13, 14 and all solutions pages were independently verified pixel-identical after final source-order corrections. Final renders: /tmp/math110-w01-ideas-final2/handout-01.png through handout-14.png and solutions-01.png through solutions-04.png. No unresolved finding, clipped label, split box/problem/solution or empty internal page remains.

Handout SHA-256: 513ede52922736d30ea51e55cf79a54a0af14bfd75eccd7a6d33c1be12ccc67b.
Solutions SHA-256: 1598158669de4ae4ad9eac6d12a2f43ae35beb1a8bd7c806c490e969ae70c5ee.
