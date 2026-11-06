# Week 2 revised packet — independent review

Current version: 13 handout pages and 2 solutions pages. Earlier release approval is superseded. The revised version follows Aaron's supplied reference PDF directly: concise motivations, explicit calculations and compact illustrative figures.

## Sources and scope

Read Notes Chapters 3–4, Definitions 7–10, Propositions 8–17, Examples 10–20, including the optional infinite-set assertions (cited with choice), combination-map criterion, single-vector summands and the nonzero-generator qualification. Matching LADR 2A–2C definitions, results and examples are included: span/minimal subspace; dependence lemma, basis extraction, replacement/extension; basis existence and complements; polynomial spaces; dimension tests; sum/intersection formula and the general dimension bound with its directness equality criterion. Actual textbook vectors and shifted-polynomial examples are used.

All six HW2 problems and their parts remain. Extra practice is the actual saved practice-midterm1.pdf Q1, with the four original generators and target (2,1,3,0). No rank–nullity, determinants or later linear-map theory is used in teaching the Week 2 methods. Determinants in computational checks only verify arithmetic independently. Numeric textbook examples using divisions retain their R/C field restrictions.

## Revisions and review findings

- Replaced generic motivations with the actual coefficient equations and reasons for deleting/replacing/extending vectors. Worked basis extraction, parameter dependence, extension, coordinate tests, polynomial coefficients and intersection calculations are explicit.
- Compact illustrations show vector coordinates, a short basis-replacement chain, the finite-support versus all-ones sequence array, and a common basis counted once in a sum. All align with the adjacent examples.
- A fresh independent reviewer read all 22 reference pages, original notes/homework and matching textbook, then all revised source and rendered pages. Correctness/coverage and reference-style teaching/layout were judged separately.
- Added the missing general inequality dim(sum Ui)<=sum dim Ui and its equality iff direct converse; retained the notes' induction explanation. Added source identifiers and the three-lines consequence. Corrected the distinct-degree shortcut to require nonzero polynomials, because deg0 is defined as minus infinity.
- Clarified the P5/P6 solution Ideas. Removed an unnecessary later-topic aside. Repaired an isolated final Traps page by allowing the problem set to follow it. Reviewer rechecked these corrections and approved both verdicts with no remaining blocker.

## Verification

`python3 scripts/checks/math110_week02.py` passes with the local SymPy environment. Checks cover the actual numeric and symbolic textbook examples, parameter dependence, basis extraction and extension, polynomial derivatives/coordinates, all-field intersection/sum arithmetic and the exam decomposition. The independent reviewer separately verified the main arithmetic.

Both PDFs built with scripts/build.sh: no errors, zero overfull boxes. Root inspected every final page; the reviewer also inspected every page and rechecked final changes. Final handout renders are /tmp/math110-w02-final/handout-01.png through handout-13.png; solutions renders are /tmp/math110-w02-review/solutions-1.png and solutions-2.png. Unchanged candidate pages were verified byte-identical after the final two fixes.

Handout SHA-256: 59ddd3f4cd6bc9fddd73bde95e5f462781a88bf431e93042992019dc93d63808.
Solutions SHA-256: 8fbe478c142f2dea5c49577fa907ef8dc7979a2af1b4815c8ada8f87ad64d0e7.

Shared layout correction: figures and captions remain in one minipage; heading space uses immediate Needspace checks instead of reserving large synthetic glue. This carries the Week 1 layout repair into later packets without changing the reference's typography. Original materials and Weak spots are preserved.
