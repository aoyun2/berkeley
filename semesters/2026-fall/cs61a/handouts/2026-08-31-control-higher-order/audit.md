# Independent CS61A Week2 packet audit

Reviewer: `/root/audit_cs61a_sources`. Date: 2026-11-07. Root authored the packet and code; this reviewer did not author or edit repository files. This report separates correctness/source coverage from teaching/reference quality and final-page inspection. **Final correctness/source-coverage verdict: PASS. Final teaching/reference/layout verdict: PASS. These verdicts apply only to the exact PDF hashes below.** Earlier source-only inventories approve no packet.

## Sources and reference

Read the actual supplied reference PDF, including its rendered pages5,13,14,20, again for this packet review. The comparison uses its short result statements, concise motivations, explicit numbered reasoning, concrete calculations and compact static diagrams connected to the nearby argument. It does not demand full-page staged illustrations or an interactive supplement.

The source baseline was independently established in `/tmp/cs61a-week02-source-audit.md`. It includes genuine Lectures3/4/5 PDFs,03.py/04.py; full CP1.4–1.6 including Newton/currying/lambda/decorators; all Lab1Q1–Q9, Discussion1Q1–Q7, HW2Q1–Q5 and complete HogP0–P12, its UI interlude and authentic starters. Fall2022 MT1 questions are attributed as lecture reproductions; the actual Fall2026 MT1 PDF pages4–5 were re-read against the added exam questions.

The administrative Syllabus Quiz link was separately fetched read-only: actual URL returnedHTTP401 sign-in/cookie gate, no anonymous question data. Raw response/link/hash evidence is in `/tmp/cs61a-week02-source-supplement/`; the repository's additive source note is not a replacement for unrecovered form questions. No form was submitted or answers fabricated.

## Review 1: correctness and substantive coverage

The complete TeX/problem/solutions sources and all six printed Python modules were read. Source-line ranges were examined as printed dependencies, rather than treating a successful full-module import as proof that the PDF contains necessary setup. This caught the missing add/mul import described below.

| Source component | Substantive content reviewed |
| --- | --- |
| L3 Control | Four print/return variants; one versus two evaluations of a non-pure function; independent if versus chain; truth values/comparisons; complete-body while semantics; prime-factor search and858 trace, multiplicity and n1 boundary. |
| L4 HOF/design | Short-circuit operand-return rules; domain/range/behavior; one job/generality/DRY; rounding result types; get_name and positive-integer same_length; summation/identity/cube/pi_term; function-valued argument binding; modular interfaces; complete Twenty-One rules and retained strategy wrapper. |
| L5 Environments | Actual Knock/Who's There print/or and classify exam reproductions; apply_twice; parent frame at definition versus call; escaping closure; allA–F make_adder variants and global-adder NameError case; no caller-frame lookup or frozen-value claim. |
| CP1.4 | Pressure example/units/model citation, docs/comments/help, default value recorded at definition, optional and keyword arguments. |
| CP1.5 | Statements/suites/local assignment; percent_difference and absolute_value; full Boolean rules; Fibonacci state and simultaneous update; assert/test/doctest including programmatic APIs and boundary cases. |
| CP1.6 summation/general methods | Shared summation invariant and finite pi examples; improve/update/close and defaults; golden ratio equation/iteration/exact convergence and float stopping limits; captured a in square-root helpers; composition/returned functions. |
| CP1.6 later subsections | Newton tangent derivation and actual plot; cited power derivative; square/nth roots64; no general convergence guarantee; currying/uncurrying/map_to_range; lambda creation/def equivalence; first-class functions; trace decorator and decorator-expression evaluation order. |
| Lab1 | Both actual WWPD groups and ordinary/returned string display; PickDigit one return; Middle distinct integers one return; Falling including zero-depth; DivisibleByK stdout plus count/empty case; adjacent8s; administrative Q8 limitation; optional SumDigits including0. |
| Discussion1 | Race deliberate defective function, wrong-return/infinite examples and strict/equality source ambiguity; Fizzbuzz precedence; prime1 boundary; required has_digit helper/unique_digits; Bottles frames/bindings; Double Trouble aliases and requested diagram; optional Repeating with explicit source correction. |
| HW2 | Product positive index bounds; Accumulate/start/n0 and one-line calling wrappers; repeat reusable returned function; pointwise composition predicate; all Church basic/conversion/arithmetic tasks with direct one/two restriction, explicitly just-for-fun/out of required course scope. |
| HogP0–P5 | Stateful supplied die; all requested rolls despite SowSad; exact BoarBrawl digits including scores>99; supplied helpers/assertions and dependency reuse; divisor count/strict next prime on total; strategy/update/die interfaces, one strategy call/turn, fixed player-order result and custom initial states/goal. |
| HogP6–P12/interlude | Returned constant strategies; full finite score-pair domain/determinism caveat; positive sample counts/*args and same die; ascending roll-count comparison/strict tie update; threshold award versus full-update gain; optional valid final strategy without optimality claim; printing/input/GUI interface reuse. |
| Authentic extra exams | Fall2022 MT1Q1(c),Q3(a) accurately identified as reproduced in L5; actual Fa26 MT1Q3 LongOdds andQ4.1–4.2 gap/odd_gap constraints, maximal groups and exact source examples. |

Administrative identities/deadlines and optional status match the actual sources: Lab1Q9 optional; Discussion1Q7 optional/slight Sp2023 exam variant; Church explicitly out of course scope; HogP0 is zero-point but not an omitted task, P1–P11 required, P12 optional0pt. Week2 fully handles the CP1.4–1.5 material explicitly carried from Week1. No later Scheme/Gleam content is substituted.

Source corrections are explicitly distinguished from original exercise content: L3 slide5's B/C typo; L4 round1.0; positive-only same_length; natural Repeating fill's missing block-width check; Race's deliberately defective equality loop and contradictory strict prose; bounded Newton stagnation evidence rather than a claim all iterations halt. The source's original positive-domain Hog primality helper remains qualified and is distinguished from the general Discussion1 helper.

## Actual execution and verification

I inspected and independently ran `scripts/checks/cs61a_week02.py` with `PYTHONDONTWRITEBYTECODE=1` under Python3.12.14. A transient indentation error in a newly expanded UI-check branch was reported; the corrected checker ran successfully. Its current report is **1116 unmodified official doctest examples**, alongside printed-module calculations/WWPD,16 original lecture examples with explicitly supplied global f context for03.py, and extra properties.

The test approach was reviewed, not accepted only by count: original modules are copied to temporary directories; printed function bodies are inserted while retaining original signatures/docstrings/tests; fresh module loads isolate official monkeypatch tests. Locked WWPD input/output is executed with independently specified stdout/return expectations instead of guessing locked hashes. Source originals remain unchanged. The supplied-context03.py test is not mislabeled a standalone untouched03.py pass.

Relevant checks include25,000 Repeating cases against an independent decimal reference;10,000 adjacent-eight/digit-sum cases; Church operation grids including arbitrary supplied function behavior; LongOdds against a grouping oracle; exact gap/odd_gap source cases; code syntax restrictions; positive-domain factor cases; Hog callback counts/argument order, stateful dice continuation, arbitrary-score digits, initial game-over boundaries, strategy validity and actual supplied UI examples. The checker deliberately uses bounded probes for known nontermination and tests the missing-global NameError case.

Code reasoning independently checked: factorization's least divisor is prime and division preserves the original product; Fibonacci old-pair update; accumulator's left combination and zero-term behavior; closure binding lookup not copied values; Repeating's end-width guard excludes partial leading blocks; Race crossing can skip equality; Hog update returns a total rather than a gain and P9 preserves earlier count on tied mean; Church power is N(M), consistent with m**n. No algorithmic error was found in the completed modules during this read.

## Review 2: teaching, reference and concision

The organization uses a few reusable ideas rather than a separate long proof/motivation for every small consequence: choose a control path; state a loop invariant; extract decimal digits; replace the changing term/operation by a function parameter; retain the defining frame; separate an iteration from its update; separate game rules from supplied decisions. This matches the reference's emphasis on the argument that produces related results.

Specific strong explanations, subject to final-page inspection:

- The short-circuit0-and-division-by-zero example identifies exactly which expression is skipped and why eager function calls differ. It teaches the evaluation rule, not just a truth table.
- The summation motivation identifies the unchanged index/test/total and the one varying term; code and a concrete term→cube call show why a function-valued parameter is chosen. Product and accumulate reuse that argument with changed identity/combination.
- The closure explanation labels both function parent and call-frame parent and uses make_adder variantE to distinguish a retained binding from a frozen value. It also explains why an unrelated caller frame does not participate.
- Fibonacci and factorization show actual state changes; the supplied dice example makes exact call counts observable through the next outcome. These are meaningful computations, not answer lists.
- The square-root and Newton material connects the numerical update to its equation. The tangent plot uses actual f(10)=36,df(10)=20 and intercept8.2; its caption explains what the picture proves. Numeric success is separated from generic convergence and residual from input error.
- Church is optional but explained through counts of an arbitrary function's applications, with explicit2→4→8 count growth. It is not disguised as mandatory exam content.

The written core is concise enough for its unusually large genuine scope: three full reading sections, three lectures, complete lab/discussion/HW and an entire project. Some content repeats between the notes and separate solutions because those serve different roles; the repeated portions generally give the local invariant/contract in short steps rather than redoing a long argument. I found no reason for broad prose expansion or indiscriminate removal of source content. Necessary repairs below add definitions, concrete source inputs or small diagrams, not generic narration.

## Precise findings and requested/checked repairs

1. **Printed imports were incomplete.** The original full hw_solutions.py imported add/mul, but the printed hw_helpers range began after that import. Accumulator wrappers therefore depended on setup the student PDF omitted. The handout also used accumulate(add,...) before introducing those names. Requested: include the arithmetic-function import/meaning before first use and in the printed HW setup. This was checked in updated source: BEGIN hw_helpers now includes the import and its generated line range starts there.
2. **Prime/composite forward reference.** Original section2: “The smallest divisor ... is prime: a composite divisor would have a smaller divisor.” Prime's definition originally appeared only in the later Hog section. Requested: define prime/composite/divisibility before this argument. Source repair must be verified in the final printed page.
3. **An omitted actual structural answer.** Discussion1Q6 asks “Draw the environment diagram,” while its original solution only narrated alias assignments. A description of what to draw does not show the requested structure. Requested: actual compact Global frame, two distinct intrinsic function values and hat/double/triple arrows, with no call frame before the additional calls. Check diagram against the code, not a decorative arrow.
4. **Five exam examples reduced to unexplained outputs.** Original gap/odd_gap solution said “The source's gap results are9,3,1; odd-gap results16,3” without supplying those five actual inputs. Requested: restore gap(5,square),gap(6,lambda x:x%4),gap(4,lambda x:-x),odd_gap(5,square),odd_gap(8,lambda x:x%5), and show concrete sequence/adjacent differences. Otherwise the reader cannot reconstruct what the numbers mean.
5. **Unprinted supplied loop.** Exam problem referred to “the supplied loop” without showing a blank skeleton; the original gap paraphrase did not state its provided k-increment/return. Requested: compact original blank skeletons for gap/LongOdds or a fully explicit statement of all provided steps/fill locations. Token restrictions must be distinguished from the supplied if statements.
6. **Orphan multiple-choice references.** Bottles was rewritten as prose without options, while solutions retained “choice(d)/(a)/(c).” Requested: remove these orphan letters or include the options. The substantive returned value1 is used in computing remaining98, not directly assigned as98.
7. **Convergence reason compressed.** Original square-root step concluded decreasing guesses reach r because a positive limit satisfies the update equation, silently using existence of a limit. The displayed identity already yields the simpler explicit estimate error_new=(x−r)^2/(2x)<=error/2 once x>=r. Requested and seen in revised TeX: use this bound to obtain geometric convergence directly.
8. **Missing meaning of df.** The Newton formula used derivative before explaining its geometric role. Requested and seen in revised TeX: define df(x) as tangent slope before the line formula; retain cited calculus derivative rules.
9. **Invalid-looking leading-zero code.** Original trap: “Numeric `01` becomes1.” Python3 literal01 actually raisesSyntaxError. Requested: describe the final decimal block01 having remainder1, not an accepted Python literal.
10. **Administrative metadata in the student problem.** Original Q8 discussed cached worksheet/HTTP401/no invention without actually supplying a clickable form link. Requested: actual authentic form link and short sign-in limitation; retain HTTP/cache/hash recovery details in audit/source addendum. This preserves the honest gap while giving the student the available action.
11. **Counting domains and literal wording.** Requested: nonnegative integer k for Falling/power's nonnegative exponent and positive root degree where used; replace Fizzbuzz's “not claimed by a case” with literal “not handled by”; avoid an unexplained “Cartesian set” when “all pairs” suffices. These are short qualifications, not new algorithms.
12. **Expanded checker indentation.** Independently reproduced IndentationError at its then-lines251–252. Fixed before the successful rerun1116; no final claim rests on the earlier failed version. Count16 lecture cases includes the explicitly supplied f context, and the1116 count includes6 official HogUI examples.

## Individual review4 page inspection

I opened every image individually in `/tmp/cs61a-w02-review4/`: all21 handout pages and all14 solutions pages. The pixel-hash inspection record is `/tmp/cs61a-week02-review4-page-record.json`. No contact-sheet-only approval was used.

- Handout1–4: whole Boolean table, code and frame/state computations readable; Fibonacci diagram and prime table correct. Found the unqualified “A call gets a new local frame” (must say user-defined call), and default-argument question's “omitting a parameter” (should say argument).
- Handout5–8: printed pressure/basic functions and imports legible; summation call/state figure and closure-parent diagram meaningful, allA–F results match sources. Short summation proof has only step1 at bottom6 and steps2–3 on7: keep this small argument together.
- Handout9–12: lambda/curry/decorator code intact; improve, sqrt proof and Newton rule/motivation/plot readable; root degree/exponent domains now stated. The Newton graph's nearby8/8.2 labels are distinct and its caption identifies actual point/slope/intercept. Optional polish: only the first line of the decorator explanatory paragraph is at bottom9; keep that paragraph together when regrouping.
- Handout13–16: Twenty-One loses-on-goal rule and complete code correct; actual Hog rule examples/turn-flow figure, callback contracts, real UI examples and means/threshold reasoning readable. Church application counts correct and optional status explicit; no invented optimality claim.
- Handout17–21: all Lab/Discussion/HW/Hog problems and hints intact, authentic form link works as a PDF hyperlink, optional labels correct, actual exam blank skeletons and5gap inputs now present. Last page21 is a complete substantial exam problem/code plus attribution; normal final-page space is acceptable and does not warrant filler or smaller type.
- Solutions1–4: actual WWPD/algorithm code and numbered explanations readable. Found a false primality Idea: “One proper divisor proves compositeness”;1 is proper even for a prime, so require a divisor strictly between1andn. Other prime loop reasoning/code already uses2..n−1 correctly.
- Solutions5–8: actual alias diagram has only Global frame and correct function identities/arrows; source correction to Repeating explicit; arithmetic imports now printed with HW helpers; Church code/results and convention correct. Homework heading/one bridge sentence ends5 while helpers are on6; optional grouping polish. Initial concern that HogP1 continued onto9 was checked and withdrawn after viewing9: it actually ends on8, close to the footer. Removing adjacent P0's repeated all-rolls warning would be a concise optional improvement, not a missing-source repair.
- Solutions9–12: long Hog signatures/returns fit; all supplied helpers/assumptions, Sus Fuss totals, callbacks, finite domain, stateful mean and threshold/final-strategy code readable and consistent with verified modules.
- Solutions13–14: actual source attribution/output exact; proper-factor sum and LongOdds/gap explanations/code/source traces intact and legible.

The remaining important page issues are local grouping/wording repairs, not a failure of the compact static reference style. No oversized decorative figures, illegible smallest labels, split code-listing borders, clipped tables or empty pages were found in review4.

## Final2 individual inspection and execution

Individually viewed all 34 final2 page images in `/tmp/cs61a-w02-final2/`: handout01–20 and solutions01–14. The complete per-page SHA256 record is `/tmp/cs61a-week02-final2-page-record.json`. No contact sheet substituted for opening a page. All theory statements, code, problem statements, source restrictions, source-case traces, headings and compact diagrams remain intact. Long Hog derivation lists and signatures fit. The last HogP1 hint word `calls.` is present on handout18, independently confirmed with PDF text bounds; there is no missing continuation. No clipped body text, split code border, empty page or illegible label was found.

Final2 repairs are visible: user-defined-call qualification, argument terminology, correct primality criterion, whole three-step summation argument, whole decorator explanation, Homework heading with printed helper imports, no repeated P0 warning, and normal-size listings with at most one consecutive empty line. Handout12 gives a concrete residual/input-error distinction: f(x)=10^-6 x at x=1 has residual10^-6 and input error1 from its zero0. This is correct and makes no false promise for the source tolerance. The Q8 sign-in limitation and authentic clickable link remain honest and useful.

Independently reran the exact current checker: PASS1116 unmodified official examples, with the16 original lecture examples and additional properties documented above. Independently verified final2 handout SHA256 `a8ee709e5a5ef050d994cb07ff93fa2c6af93e7bbc54ccc0d3beb9f5c60ad458` and solutions SHA256 `14d8689dcca49c54982b61f4e40a342ed419bcde5ce9159d9f95176440993138`.

Two final prose repairs are complete: HW2Q3 now states its iteration invariant in plain words, avoiding notation defined only in optional Church theory; the Race explanation now separates minute/minutes from following numerals. Neither affects executable code or algorithms. No findings remain.

## Final verification and verdicts

**Correctness and source coverage: PASS.** The complete scheduled source scope in the table above is substantively covered, all actual tasks and optional tasks are included with accurate status, authentic exams/restrictions are preserved, supplied-source defects are explained, and printed completed code passes the independently rerun checker. Lab1Q8 is an explicit administrative source limitation, with its authentic link; the packet does not fabricate the unavailable form questions or an answer key.

**Teaching, reference and final-page layout: PASS.** The packet develops the small number of reusable ideas with concise numbered reasons, authentic computations and compact static illustrations. No further repetition, unsupported important conclusion, unexplained essential notation, unreadable code/figure, clipped body text or malformed page was found. All 20 handout pages and 14 solutions pages were individually viewed in final2. Every final4 page was then compared pixel-for-pixel against that viewed baseline: only solutions03 and solutions07 changed, and both were directly viewed again in final4. The remaining32 pages are pixel-identical. This is an approval of the final pages, not a conditional approval of a previous draft.

Exact approved repository PDFs:

- `handout.pdf`,20 pages, SHA256 `a8ee709e5a5ef050d994cb07ff93fa2c6af93e7bbc54ccc0d3beb9f5c60ad458`.
- `solutions.pdf`,14 pages, SHA256 `8f5a3dd0b7aa6dc1aa7dcef5270729359bbc0a8a94937f87710bd9cd4f3025a5`.

Both were independently rehashed from `semesters/2026-fall/cs61a/handouts/2026-08-31-control-higher-order/`. Matching final renders are `/tmp/cs61a-w02-final4/`. Full PDF/TeX/code/range/style/checker hashes and per-page inspection evidence are in `/tmp/cs61a-week02-final-audit-record.json`; the34 direct final2 page views are separately recorded in `/tmp/cs61a-week02-final2-page-record.json`. The final executable check passes1116 original official doctest examples plus16 original lecture examples and the independently specified properties described above. All required wording/layout repairs are closed. No repository file was authored or edited by this reviewer.


## Author's final release record

Root individually inspected all 20 final handout pages and all 14 final solutions pages in /tmp/cs61a-w02-final4/ (handout pages1–12 were individually viewed in final2, whose handout PDF and pixels are unchanged). The independent reviewer inspected all34 final2 pages individually and compared every final4 page; only solutions03 and07 differed and both were individually re-viewed. Both final PDFs build with zero overfull boxes. No remaining review findings. Final handout20 pages; solutions14 pages.

The source/algorithm review repairs, not page count, establish completion: concrete loop-state/parent-frame/alias diagrams, Newton's actual tangent plot, explicit source inputs and intermediate results, proof choices and shared invariants. Short proofs, code blocks and problems remain intact without shrinking code. The final two small repairs replace undefined iteration notation in HW2Q3 with plain language and restore spaces in minute references.

All original materials remain unchanged. An additive source note materials/source-addenda/2026-11-07-lab01-syllabus-quiz.txt records the authentic form URL, read-only HTTP401/sign-in response and recovery limitation. Lab1Q8 question text was not recovered; its answers are not fabricated. This explicit administrative gap prevents any claim of possessing a complete syllabus-quiz answer key. CP1.4–1.5 coverage carried from Week1 is fully included this week. No later scheduled week was backfilled here.

Code and final line ranges were checked by scripts/checks/cs61a_week02.py:1116 original public doctest examples plus16 lecture examples, exact WWPD/printing/errors, constraints, independent oracles and Hog callback-count/state cases. Official monkeypatches are isolated with fresh modules per test function; lecture03's missing global f is explicitly supplied. Incomplete exam skeletons are defined, not executed as completed algorithms. No unresolved test failures.

Final approved PDF SHA-256:
- handout.pdf: a8ee709e5a5ef050d994cb07ff93fa2c6af93e7bbc54ccc0d3beb9f5c60ad458
- solutions.pdf: 8f5a3dd0b7aa6dc1aa7dcef5270729359bbc0a8a94937f87710bd9cd4f3025a5
