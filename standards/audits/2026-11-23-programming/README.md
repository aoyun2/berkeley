# Programming and course-specification audit — 2026-11-23

Scope: the five existing CS 61A packets and two existing STAT 20 packets in this checkout, including three browser exercise pages and their downloadable archives. This is an audit and specification revision, not an implementation repair. No exercise artifact was changed. Official course-policy currency and full syllabus coverage were not reverified against external sources.

## Assessment

The exercises have useful subject matter and a generally sensible progression. The main weaknesses are missing deliverables, insufficient correctness checks, and several mismatches between the instruction and actual behavior. More explanation would not resolve those defects. Existing specifications were detailed about appearance but did not provide sufficient behavioral acceptance criteria.

| Area | Evidence | Required follow-up |
| --- | --- | --- |
| CS 61A Python availability | Four packets refer to absent executable exercise packages | Deliver the promised original practice and tests, or correct the promises and inventory |
| CS 61A SQL checking | All seven reference answers pass; two plausible wrong answers also pass | Add discriminating fixtures and mutation checks |
| CS 61A browser/download parity | A browser-accepted bare SELECT fails the offline checker | Use a consistent export/submission contract and test the exported file |
| CS 61A debugging explanation | Three-digit `sum_b` raises TypeError, contrary to the solution's general None claim | Correct the explanation and verify both call depths |
| STAT 20 feedback | Reference code runs, but no answer-checking tests exist in either ZIP | Add result checks and distinguish execution from correctness |
| STAT 20 interpretation | Simulation resolution and an overfitting claim need revision | Match the explanation to the computation and its limitations |
| STAT 20 causal reasoning | Balance checks and adjusted regression are given stronger causal interpretations than the evidence supports | Separate design assumptions, balance diagnostics, conditional associations, and causal claims |
| Coverage and publication evidence | No local course profiles, source materials, or explicit publication configuration found | Record source scope and authorization; inspect deployed files before adding solutions |

See [CS 61A findings](cs61a.md) and [STAT 20 findings](stat20.md) for references, reproductions, strengths, and limits. Existing public solution content was observed; absent authorization records do not prove that it was unauthorized.

## Specification revisions

- Added a general course standard for source-backed scope, objectives, independent practice, course profiles, publication settings, and review evidence.
- Added a programming standard for prompt contracts, starters/data/tests, realistic wrong-answer checks, runtime isolation, browser/download parity, course-specific semantics, and acceptance records.
- Replaced conflicting duplicated requirements in CLAUDE.md with a short routing document, including the current approved figure style.
- Updated the handout standard to preserve substantive detail while removing repeated explanations, fixed-length proof requirements, mandatory filler boxes, and repeated syntax guides.

## Validation limits

CS 61A SQL was executed with Python SQLite, including reference answers, starter failures, and targeted incorrect variants. Selected Python definitions were executed; every paper trace was not independently certified. STAT 20 runtime evidence and browser limitations are documented in its report. Full live-page interaction, accessibility, theme, and CDN checks remain open; source inspection is not a substitute for them. The new standards define future acceptance gates and do not retroactively mark these packets compliant.
