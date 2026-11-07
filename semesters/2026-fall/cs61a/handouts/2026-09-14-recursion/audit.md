# Independent CS 61A Week 4 packet audit

Packet: `/workspace/berkeley/semesters/2026-fall/cs61a/handouts/2026-09-14-recursion`.
Reviewer: independent source-review agent; read-only in repository, no packet authorship or fixes. Final correctness/coverage verdict: **PASS**. Separate teaching/reference/concision/layout verdict: **PASS**. Both bind only to final6 hashes recorded below. Review2 was inspected completely (14 handout pages and 9 solutions pages) but is superseded and receives no final approval.

## Sources and scope

Fresh source audit: `/tmp/cs61a-week04-source-audit.md`; exact 31-entry manifest `/tmp/cs61a-week04-source-audit/manifest.json`; source page visual record `/tmp/cs61a-week04-source-audit/source-page-inspection.json`; source execution `/tmp/cs61a-week04-source-checks.json`. All 17 Lecture 8, 12 Lecture 9 and 15 Lecture 10 slide pages, including embedded-image questions, were examined in the source review. The two HW-linked authentic exam questions and their official solution pages were also individually viewed. Source HTML, starter code and original lecture code were read, not inferred from prior summary notes.

Scheduled week September 14–20: L8 Midterm 1 Review (Monday), L9 Recursion (Wednesday), L10 Tree Recursion (Friday), full CP 1.7, Discussion 3 Q1–6 including optional Karel, HW3 Q1–7 including both just-for-fun questions, and the actual HW-linked Fa17 MT1 Q4(a) and Fa19 Final Q6(b). No new lab; Hog continues, due September 17. HW3 due September 24 11:59 p.m. The packet keeps the optional/outside-required-scope qualification of Hanoi and anonymous factorial. The L8 Sp25 and L10 Sp24 exercises are correctly qualified as reproduced in those lectures; neighboring later exam problems are not prerequisites.

Coverage checked explicitly:

- CP1.7: recursive contract and induction; all digit-sum examples; positive-only CP factorial versus zero-safe lecture factorial; ascending/downward loops; accumulator/tail recursion; mutual parity and inlined parity alternative; Alice/Bob game; both cascade organizations and exact output; Fibonacci/repeated calls; all partition bases, include/exclude bijection, all nine P(6,4) partitions and four additional source counts.
- L8: reverse/curry square and cube; all_digits; both prefix_digits alternatives with source numeric cases and stable-predicate qualification; numbered hailstone's transition output, old enclosing state and simultaneous assignment; actual slide17 nested-lambda expression evaluating to81. Downloaded08.py's unfilled top-level square binding is explicitly a starter defect, rather than claimed to pass as a complete program.
- L9: retained lexical parent via exp; source New Print recap with five user calls and exact output; both fact versions, fact_k and fact_tail with source cases; exact Twenty-One goal/loser convention and once-per-turn callback behavior.
- L10: recursive correctness versus tracing; term-counting recursive hailstone distinguished from L8 transition printing; actual Streak template/examples and its source identity; iterative/recursive Sevens state rule; least-factor primality and complete removal of multiplicity, both72000 slide and576 code cases; partitions; source-code-only count_park method and its cases.
- Disc3: Swipe, Skip Factorial, recursive Is Prime with minimal-helper-argument/docstring requirement, supplied three-function Hailstone, supplied Sevens state, and optional Karel including every allowed primitive/body restriction. Source prose lacks heading; the authentic default linked UI supplies east-facing initial orientation. Final-west paired-two-forward/one-return algorithm checked independently for widths1–100 and both parities.
- HW3: all seven actual problems, genuine restrictions and examples. Public interleaved_sum AST bans operators individually, stronger than an ambiguous prose reading; num_eights bans all assignment forms in helpers too. Count Coins includes exact denominations/next_smaller_coin and unordered distinction; max_subseq means at most t; Hanoi rod assertion/legal top-disk moves retained; anonymous factorial imports precede use and no global recursive name occurs. Submission/test/checkoff instruction scope preserved without duplicating Week1 setup.
- Authentic exam templates: Collapse's nonnegative domain including0 and all five examples; Contains's exact blanks/restrictions/order and all three examples. Official Contains solution's initial/remaining a=0 empty-pattern convention is stated explicitly and does not claim ordinary decimal0 occurs in7. Rightmost-match reasoning explains the greedy branch. Streak belongs to L10/Sp24, rather than being mislabeled HW-linked practice.

No unacknowledged missing assigned source or algorithm defect found after repairs. Universal hailstone termination is not asserted; least-factor outer function has n>1; partition bound m>=0 is qualified. A source's expected TODO failure is distinguished from completed-solution checks.

## Independent verification

Executed `PYTHONDONTWRITEBYTECODE=1 python3 scripts/checks/cs61a_week04.py` successfully at review start. Read the checker in full: it checks all marked printed line ranges against exact code, checks every range is used, loads printed implementations, runs original HW3/Discussion doctests in fresh scratch source with original signatures/docstrings, runs unchanged09.py/10.py doctests, and separately isolates08.py complete definitions after confirming its expected placeholder NameError. Counts:73 unmodified HW3/Discussion examples;38 original lecture examples, plus independent oracles/properties.

Additional genuine checks include decimal-string digit/count/distance oracles, exhaustive bounded subsequence enumeration, DP coin/partition counts and all actual partition forms, prime-factor set oracles, exact print output, parity/factorial/Fibonacci state cases, once-per-turn strategy calls, 100 Karel worlds, legal Hanoi execution for all ordered rod pairs through six disks, lambda factorial through14, Collapse across10000 inputs, Contains across251² input pairs, both prefix methods against independently enumerated prefixes, and AST source restrictions. String/DP oracles belong only to verification and do not violate student implementation restrictions.

## Separate teaching/reference review

Standards read: handout-standard.md and teaching-quality.md; actual supplied PDF viewed afresh, including reference pages13 and20 (prior full relevant reference review also covered5 and14). The packet follows its compact result/motivation/numbered-reason organization. One central digit-recursion argument supports factorial/distance/Swipe rather than separate repeated long proofs; loop-state contracts support factorial/game/Sevens; partition bijection supports coin counts and optimization. Local solution Idea lines explain the choice of recurrence; numbered steps supply the missing combination and progress arguments.

Concrete static figures show actual calls/returns, Sevens order, repeated fib(2), nine partitions, Karel columns and Hanoi disk clearance. They explain examples rather than occupy decorative pages. Source qualifications stay brief. No need to expand routine consequences or repeat Week3's full lambda translation: the authentic81 expression and fresh-def/same-defining-frame rule suffice. Concision is compatible with all actual examples and constraints. Moving clearly attributed Streak beside Sevens is appropriate shared digit-recursion practice and removes the otherwise quarter-page terminal solution page without shrinking type or omitting content.

## Findings and closure log

1. Digit-sum caption originally said three functions, but it depicts three calls of one function. Corrected to three call frames.
2. Parity trace used odd/even although printed functions are is_odd/is_even. Corrected to exact names.
3. Partition caption introduced undefined a in 'Presence of a=4'. Corrected to 'a part equal to4'.
4. Actual L8 slide17 nested-lambda81 example absent. Added exact expression/result and concise frame-preserving translation rule; checker asserts expression.
5. Attribution literal cache path had erroneous space in `week 04-exam-practice`. Parent replaces student cache detail with actual public exam links; full cache/provenance remains in audit/source-addenda.
6. Karel text referred to linked UI without a hyperlink. Parent adds authentic Stanford IDE link; source heading caveat remains.
7. HW3 Q5 solution's '2012,t2' cleanup became '2012,t 2'. Parent makes n=2012,t=2 and n=20125,t=3 explicit.
8. Review2 h7 orange cascade labels touched/overlapped ('line7second print...'). Parent shortens to line7/line6/line5; caption already defines second prints.
9. Review2 h11 prose joined 'exponent2'. Requested ordinary space before2.
10. Review2 terminal solution page contains Streak alone (~quarter page). Parent relocates clearly attributed practice beside Sevens in both problem set and solutions; source identity remains explicit.

Final repaired PDF page-by-page inspection, final checker execution, exact file hashes and both final verdicts will be appended below. Earlier review of superseded pages is not final approval.

## Final4 inspection (superseded only for one paragraph layout repair)

Individually viewed all final4 renders `/tmp/cs61a-w04-final4/handout01.png` through `handout14.png` and `solutions01.png` through `solutions08.png`. Confirmed exact repairs1–10: call-frame caption/name corrections, authentic81 expression, safe caption wording, short cascade labels, exponent2 spacing, Karel hyperlink, public exam links, explicit max-subsequence parameters and attributed Streak relocation. No missing or cut-off listing, unresolved figure overlap, split result box, broken heading, or mathematical/source error found. Both example figures and all seven HW tasks remain intact. Solutions no longer has the sparse terminal Streak page.

Final4 hashes: handout14pages `6d04d5968aff860931465a232f3cd7fcc1edd4292426d9ce1ded04c4112f9eaa`; solutions8pages `a79395e7c1f48328bd81bb4e9b62cabd8605531610ef7564795b11af9d24045b`.

One new minor layout finding blocks final teaching/layout approval of this handout version: the short submission/checkoff paragraph splits h13–14 inside the phrase 'The official assignment also requires a / checkoff interview'. Requested that short paragraph stay atomic, or at least a sentence-level break. No content change requested. All22 final4 pages have actually been viewed; this is not approval of a superseded or merely anticipated layout. Final checker again passed73+38 with all independent properties and printed-range checks.


## Final6 dual verdict and exact binding

**Correctness/source/coverage: PASS. Teaching/reference/concision/layout: PASS.** No unresolved findings.

Final6 handout:14 pages, SHA256 `ae5ec8f2576dc911065a723675d5e266d7cc95db29eeb12c9594ea4a59c980e6`.
Final6 solutions:8 pages, SHA256 `a79395e7c1f48328bd81bb4e9b62cabd8605531610ef7564795b11af9d24045b`.

Every final page is covered by actual visual inspection: all14+8 final4 pages were individually viewed, and exact byte comparisons of all22 final6 PNGs show only handout04,13,14 changed. Those three final6 pages were then directly viewed individually. The Sevens number/player pairs now align in genuine table columns with exact source values; the complete short submission/checkoff paragraph now stays together on p14. Remaining19 page images, including all8 solutions, are byte-identical to the pages actually viewed. No font reduction, source deletion, new overlap, cut-off code or sparse orphan terminal page was introduced. This comparison is independently executed, not merely the author's claim.

Final independent checker rerun passed73 unmodified HW3/Discussion examples and38 original lecture examples, plus every printed-range check and the independent properties described above. Actual final logs contain zero overfull boxes. Final source files, checker, output, PDFs and all22 final PNG hashes are recorded in `/tmp/cs61a-week04-final-audit-record.json`; exact checker output in `/tmp/cs61a-week04-final-check.txt`. No repository file was edited by the reviewer.

The approval preserves source caveats rather than concealing them: original08.py contains an unfilled blank; initial Karel heading comes from the linked default UI; universal hailstone termination remains unproved; outer distinct-prime count requires n>1; partitions start with m>=0; Contains follows the official zero-sentinel convention. No later exam concepts or unrecovered question statements were invented.


## Author's final release record

Root individually viewed handout1–12 and all8 solutions in /tmp/cs61a-w04-final4/, then individually viewed changed final6 handout4,13,14. Exact PNG comparison of all22 pages establishes that these are the only changed pages; all other pages are byte-identical. The independent reviewer also individually viewed every final4 page, independently compared every final6 page, and directly re-viewed the three changes. Final handout14 pages, solutions8 pages; both build with zero overfull boxes. Source code remains ordinary10pt; short arguments, figures/captions and complete problems/solutions are intact. Root and reviewer have no unresolved findings.

The final Sevens figure uses true table columns so spoken numbers and player indices align. The short submission/checkoff paragraph remains whole. Moving the explicitly attributed L10/Sp24 Streak exercise beside Sevens in both problem set and solutions removed one avoidable sparse solutions page; it did not remove content or shrink type. All necessary source hypotheses, source distinctions and exact restrictions remain visible.

All pre-existing materials remain unchanged. Additive source-addenda/week04-exam-practice contains four genuine public exam/solution PDFs, full text, exact URL/hash/status manifest and recovery provenance: the actual old HW3 links returned CAS login HTML; current official public copies recovered the same identified exams without sign-in. Only assigned Fa17MT1Q4(a),p5 and Fa19FinalQ6(b),p6 are used; source identity and question content were checked. Source-addenda/week04-karel preserves the linked UI/default world/model/constants and exact URL/hash evidence for the bottom-left east-facing start. No unseen survey/exam question is invented, no account signed in, and no work submitted externally.

scripts/checks/cs61a_week04.py passes73 unmodified original HW3/Discussion3 doctest examples and38 original lecture examples: actual09.py7,10.py29, and08's2 working-definition examples isolated explicitly because original08.py has a terminal unfilled blank. It validates exact printed line ranges/modules; independent digit/subsequence/prime/factor/partition/coin oracles; actual output and error cases;100 legal Karel worlds; legal Hanoi moves for1–6 disks and all rod pairs; callbacks and actual public syntax restrictions. Official HW code is filled in scratch while preserving original docstrings/signatures/inspect-based tests. Original source files are not modified. Tests do not claim that raw unfilled starters pass or that arbitrary hailstone starts terminate.

Approved handout SHA-256: ae5ec8f2576dc911065a723675d5e266d7cc95db29eeb12c9594ea4a59c980e6.
Approved solutions SHA-256: a79395e7c1f48328bd81bb4e9b62cabd8605531610ef7564795b11af9d24045b.

The authored-file Git whitespace check excludes materials snapshots: recovered raw HTML/JavaScript and literal PDF text extraction retain upstream trailing spaces. Those source assets are preserved with their recorded original hashes; no whitespace normalization is presented as an unchanged source response. Packet/code/log files pass the scoped whitespace check.
