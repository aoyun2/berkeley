# Independent CS61A Week3 packet audit

Reviewer `/root/audit_cs61a_sources`, 2026-11-07. Root authored all packet sources. Reviewer has not authored or edited repository files. **Final correctness/source-coverage verdict: PASS. Final teaching/reference/layout verdict: PASS. Both apply only to the exact PDF hashes below.**

## Source and reference baseline

Read both standards and the actual supplied reference PDF, including its worked calculations and compact static figures on pages 5,13,14,20. The source-only audit is `/tmp/cs61a-week03-source-audit.md`, with exact URL/hash manifest, all 32 original lecture slides individually inspected, actual exam pages, full HTML and authentic starter/tests. This is a fresh review of the completed packet rather than approval inherited from an earlier inventory.

Read entire handout.tex, problems.tex, solutions.tex; all four printed Python modules; all three printed original WWPD transcripts; range/style definitions and the complete checker. Range definitions were checked against source dependencies and actual printed sections.

## Review 1: correctness and substantive source coverage

No algorithmic error found in the complete source/code read. Later page inspection caught one omitted original funsquare example/undefined triple name and the delayed nearest-prime domain statement, recorded below for repair. Exact coverage after those small source-preserving repairs:

| Source | Substantive content checked |
| --- | --- |
| L6 slides4–6 | Summation's changing function argument versus parameter name; identity/geometric/cube/pi examples; lambda creation/body delay, zero/several arguments, expression versus def binding; actual nested twice/square rewrite81. |
| L6 slide7 and06.py | Both genuinely different examples: direct Global lambda reads current ratio1/5 and gives781/3125; get_term parameter retained1/3 despite global1/5 and caller-local1/4 gives121/243. No frozen-value or caller-parent claim. |
| L6 slides8–10,12 | Curry parent chain, half-power1/32, genuine3-power sum363; zero-argument die interface; full actual cake/pie session in Lab2; twice/square reused concisely. |
| L6 slide13 | Full image-only authentic Fa22 MT1Q4(a), all six choices with identified suffix adaptation, one-argument outer and returned-function interfaces; D/F correct. |
| L7 slides4,6,7,9 | Actual oski/abs output2, (3 and4)-5=−1, all seven bool cases including print effect, all three binding mechanisms, abs-twice and actual small f(4)=6 demo. |
| L7 slides10–11 | Complete intentional max rebinding bug, first local y3 versus global y1, global max1/y2 at next-call TypeError; proposed rename repair and correct9/10 result. |
| L7 slides13–14,16 | Full nearest-prime offset order and larger-on-tie reason, examples8/11/21, source fills; complete helper domain identified; lambda rewrite not duplicated. |
| Lab2 review | Short-circuit operand-return rule; lambda/def distinction and runtime <lambda> name; scale examples18/20/30; multiply_by returned function and global NameError; all assignment/def/call/lambda frame rules. |
| Lab2 Q1–Q3 | Every original locked WWPD input faithfully printed with output blanks (45 session entries including definitions); solutions distinguish side effects, prompt repr, FUNCTION, ERROR and None. |
| Lab2 Q4–Q5 | Delayed branch selection including boundary; fresh count per call, (n,i) order, all generalized original examples, source direct-loop primes6/13 examples, supplied helper domains. |
| Lab2 Q6 | Full actual code and four real user-defined calls; first f never called, second f resolves old g/n, h retains x14, final global n7/fh/g15; parent links distinguished from call order. |
| Lab2 Q7–Q8 | Authentic survey link/closed-form limitation; no invented token. Optional cycle captures functions/n separately, fresh progress per input, operation order and all actual examples including0 applications. |
| Discussion2 Q1–Q2 | Inner/outer lambda x separation giving30; complete Teamwork code/actual diagram, global abs versus dream's local tFalse and final teamabs. |
| Discussion2 Q3–Q5 | Keeper retains bound/prints/returnsNone, source even/all/none tests; one-based digit formula/assert/no text conversion/all4cases; MatchMaker original skeleton, meaningful positive digit domains, all7 source examples, complete-pair stopping rule/vacuous success. |
| Discussion2 Q6–Q8 optional | WhichOne retained localone3 and unreachable returns/assignment; every full original skeleton and two source cases; count_if/count_at_least complete skeleton, source5threes/9threshold result; original exam provenance and optional status. |
| Fa26 MT1 Q2 | Exact original new_print function/call setup, three output lines, retained distinct wrappers and meaningful compact figure; preserved source behavior. |
| Fa26 MT1 Q4.3 | Explicit optional zero-point A+ status; at least two selected indices; actual helper and blank restrictions (provided if allowed); gap interface restated; count/select uses helper twice, stable use qualification, actual odd/mod5 example3. |
| Administrative scope | No newly assigned homework/readings; genuine dates/continuing HW2/Hog and Lab2 due date; Quiz1 only title/date with no invented questions; actual pytest/unlock and submission instructions. |

L7 title-only slides and qualitative study-encouragement line plot supply no additional published programming exercise. No invented ternary question is attributed as recovered source; the simple conditional-expression example illustrates the scheduled title topic. Original source code and dates are preserved. No recursion or later Gleam/Scheme material is imported.

## Actual executable checks

Independently ran `PYTHONDONTWRITEBYTECODE=1 python3 scripts/checks/cs61a_week03.py` under Python3.12.14: PASS52 original lab/discussion doctest examples;45 exact WWPD session entries; genuine06.py's two printed outputs and original summation doctest; all printed module/range freshness checks; digit-position/pair oracles, predicate argument/call counts, fresh cycle use, nearest-prime oracle/tie behavior, actual exam outputs/error states and syntax restrictions.

Read the verification approach: original Lab docstrings/signatures are retained in filled scratch modules; actual on-page Discussion doctests run against completed functions; original locked input sessions execute sequentially with independent specified displays, without decoding hashes. Printed transcripts are byte-compared against original docstrings with only locked answers replaced by blanks and doctest flags omitted. Exact ranges and every used region are validated. Known intentional max failure runs in its own namespace. Source originals are unchanged. This is distinct from untouched starter TODO and unavailable survey-token grader failures.

The checks support, but do not replace, manual reasoning about definitions and frame lookup. I independently checked the finite scan invariants, geometric sums, name rebinding state, positive/negative offset order, wrapper call results and make_gap's count/kth-index translation.

## Review 2: teaching, reference and concision

The central organization is sound: defer a rule until input arrives; use the recorded defining frame; trace a rebinding before the next loop iteration; choose a candidate order that proves the result. Routine lambda/keeper/counter/digit/cycle consequences reuse these ideas briefly. Code and authentic full WWPD/problem statements account for the length; motivations do not repeatedly restate complete proofs.

Specific explanations that teach the mechanism:

- Lambda motivation identifies the index that arrives later and explains why term itself, rather than term(k), is supplied.
- Both authentic ratio examples show the exact binding sought and actual sums, avoiding a misleading universal “captured initial value” rule.
- Currying locates y, x and f in successive parents rather than merely stating the nested-lambda answer.
- The max example tracks a whole first iteration, then checks the next operator with changed bindings; it identifies the actual failing lookup.
- Nearest-prime search order explains both distance minimality and positive-offset tie preference. Digit pair stopping explains why no-existing-pair inputs pass.
- NewPrint assigns different names to wrapper objects and traces the returned2 and 'What?' separately from effects.
- MakeGap explains why one helper invocation counts and another locates, with actual selected indices/values and differences.

### Precise findings and verified replacements

1. **Call-order shortcut:** “Read parentheses from the inside outward” can contradict Python's operator-first/left-to-right evaluation rule for general calls. The multiply_by example itself is correct. Requested local replacement with the actual rule for chained calls; the replacement was verified in final4 pixels.
2. **Outer integer counter:** “Keeping the counter in the outer function would make independent uses share progress” is false for the shown ordinary integer loop without nonlocal. Moving only i=0 outside while retaining i+=1 raises UnboundLocalError. Requested a precise fresh-progress statement or qualification; the precise local-binding explanation was verified in final4.
3. **Compressed prose notation:** examples “With b0…h6,” “g14,” “abs2−1,” and “local x14,n9” omit whether a numeral is an argument, binding or suffix. Requested ordinary spaces and actual h(6),g(14),abs(2),x=14 forms. Ordinary prose joins, call notation and compact node bindings were corrected and directly checked in final4.

4. **Nearest-prime contract delayed:** actual “integer n > 5, nearest prime, larger on ties” hypothesis was not stated together before the listing; n > 5 first appeared in the termination step. Requested the exact contract before its motivation/listing. The contract is now present before the listing, verified on final4 handout5.
5. **Original funsquare example / undefined triple:** choices were complete, but hint and solution used triple without the original slide's definition `triple = lambda x: 3*x` and example `funsquare(triple)(5) = 45`. Requested that actual source example before the choices; it is restored before the choices, directly verified on final4 handout12.
6. **Inline math spacing:** handout11/13 rendered “integerk”, “thekth”, and “takesn” from missing spaces outside math delimiters. Requested explicit prose/math boundaries; the corrected boundaries are visible in final4 while code/URLs/TikZ remain intact.
7. **Boolean token spacing:** Teamwork solution said `notFalse=True`; requested actual `not False` rather than a joined identifier.
8. **Review2 visual repairs:** curry arrow labels overlapped neighboring box edges; remove labels already supplied by box parents/caption. The three-step max argument split after step1 at handout4 footer; keep this short list together. WhichOne's middle and right diagram boxes overlapped on solutions5; separate them or shorten the redundant parent annotation at normal type size.
9. **Repeated setup comments:** max loop was commented and required an instruction to reinterpret it as code; new_print printed commented run-lines immediately before the same actual run-lines. Root is replacing max with its authentic complete executable text listing and removing the repeated new_print comments. These repairs clarify the actual source without adding narration.

All nine findings above are closed against final4: the call-order/counter statements are precise, source contract/example restored, math and Boolean spacing correct, curry labels removed, max steps kept together, WhichOne boxes separated at normal type, and the authentic executable max listing/repeated new_print setup repaired. No added long proof was needed for these local repairs. Do not expand the routine consequences or reduce normal code size to meet a page target.

## Final page inspection and verdicts

Individually viewed every review2 image in `/tmp/cs61a-w03-review2/`: handout01–13 and solutions01–07. Exact page hashes and direct-view evidence: `/tmp/cs61a-week03-review2-page-record.json`. All code/transcripts, tables, actual problem skeletons, source restrictions, administrative limitations and terminal pages were checked. Source-sized code remains readable; no clipped problem text or split listing border was found. The normal tail space on solutions3 occurs because the next complete Cycle problem is slightly too tall for the remaining area; it is not an empty page or omitted content. NewPrint/MakeGap diagrams/code and numeric traces are correct.

### Final4 all-page inspection

Individually opened and inspected **all20 final4 images** in `/tmp/cs61a-w03-final4/`: handout01–13 and solutions01–07. This is a direct final-page review, not an inherited or contact-sheet approval. Independently compared final4 pixels to final2 as an additional check: handout1–4 and all7 solutions are identical; changed handout5–13 were all directly viewed. Every final4 page was directly opened, including the unchanged ones. Exact per-page SHA256 evidence is `/tmp/cs61a-week03-final4-page-record.json`.

- Handout1–4: whole boxes/code and actual sums readable; defining-frame versus caller figure and curry chain correct; curry arrow text no longer touches box borders; complete authentic executable max example and table intact.
- Handout5–6: max's three steps together, exact nearest-prime contract before use, source-assumed helper accurately described for positive inputs. Its complete divisor procedure and reason replace repeated Week2 code; nearest loop remains executable with the helper in examples.py. The short loop and condensed helper explanation restore13 pages without smaller type or dropped source content. Candidate/digit figures and all reasons/shortcuts/traps fit. No prior large unexplained theory tail remains.
- Handout7–10: all45 original WWPD session entries, full lines/comments/blanks, source examples, Lab diagram code, authentic closed-survey link, optional cycle and actual test/submission instructions readable; Discussion heading and initial questions intact. Long comment wrapping does not clip source text.
- Handout11–13: math/prose spacing repaired; full actual Discussion skeletons/constraints and optional statuses correct; original triple example restored before all6 funsquare choices. NewPrint actual setup appears once. MakeGap's helper, blank, gap interface, at-least-two/stable-use assumptions, restrictions, source case and terminal attribution/continuing dates all intact. Terminal page is substantial, not a near-empty orphan.
- Solutions1–4: all tables and explanations readable; actual Lab four-frame diagram and Teamwork global/local diagram correct; cycle actual traces and `not False` syntax intact. Source-survey limitation honest.
- Solutions5–7: digit cases/invariants correct; WhichOne boxes now separate with explicit f1/f2 parents at normal size; no labels/borders intersect. Optional source problems, all funsquare answers, wrapper graph/output and complete constrained make_gap solution/reasons fit. No clipped text, split listing border or unreadable smallest label found.

### Exact final verdicts

**Correctness/source coverage: PASS.** Complete substantive scheduled lecture/Lab/Discussion scope, every required and optional task, authentic applicable exam material, source hypotheses and examples are present. Code and displays are correct. Known source simplifications and missing administrative inputs are handled accurately.

**Teaching/reference/concision/final layout: PASS.** The packet uses a small set of reusable arguments with concise motivations, explicit numbered reasons, actual calculations and compact explanatory figures matching the supplied reference's approach. Routine consequences are not expanded into repeated long proofs. Final repairs were checked in actual page pixels. No unresolved finding remains.

Approved repository PDFs at `semesters/2026-fall/cs61a/handouts/2026-09-07-functional-abstraction/`:

- `handout.pdf`,13 pages, SHA256 `4147bbfd0273956e30fd59ab4cb356382643af2366fbf769dcfad57a8d43af84`.
- `solutions.pdf`,7 pages, SHA256 `e90880757dad95362a68ec37b9998001f32d67dab8e2d35727b7b61e056e1062`.

Both hashes were independently calculated from the final repository PDFs after visual inspection. Independently reran the current exact checker after the final helper/range changes: PASS52 original Lab/Discussion examples,45 exact WWPD entries, original06.py output/doctest, independent oracles/error states/restrictions. Full source/checker/addendum hashes and final-page record are in `/tmp/cs61a-week03-final-audit-record.json`.

Quiz1's title-only status and the closed Lab2 survey remain honest source limitations; neither has an invented answer set. They do not prevent review of the actual published academic content. Reviewer edited only scratch audit files and did not author or edit repository deliverables.


## Author's final release record

Root individually viewed all20 final pages: handout1–4 and all7 solutions in final2, handout5–13 in final4. Byte-identical final2/final4 PNG comparison establishes that those first four handout pages and all seven solutions are unchanged. The independent reviewer directly viewed all20 final4 pages again. Both PDFs build with zero overfull boxes; all small figures/code labels and complete problems/arguments remain readable. Final renders: /tmp/cs61a-w03-final4/. Independent exact file/page record: /tmp/cs61a-week03-final-audit-record.json.

Original source materials remain unchanged. The additive materials/source-addenda/2026-11-07-lab02-survey.txt saves the authentic URL, closed-form text, HTTP200/final URL and response hash. Lab2Q7 questions/completion token and Quiz1 question sheet remain unavailable. This is an explicit gap, not a claim to possess their answer keys. All other assigned source material is covered, including image-only funsquare, both genuinely different ratio examples, optional questions, authentic exam excerpts and continuing HW2/Hog dates. No new textbook section or homework was invented.

The genuine L7 nearest-prime example assumes a primality helper. Its procedure and reason are stated here for positive integers rather than reprinting Week2's duplicate helper listing. The complete local executable helper also rejects0/negative inputs, a harmless extension outside every reached candidate; no claim is made that the original Lab2 positive-only helper handles those values. This regrouping removed one avoidable page without shrinking type or deleting the argument.

Final approved handout13 pages, SHA-256 4147bbfd0273956e30fd59ab4cb356382643af2366fbf769dcfad57a8d43af84.
Final approved solutions7 pages, SHA-256 e90880757dad95362a68ec37b9998001f32d67dab8e2d35727b7b61e056e1062.
