# Packet Audit: CS 61A Week 13 — Tables, SQL & Aggregation (`2026-11-16-tables-sql-aggregation`)

- **Scope:** Week 13 (Lectures 34--36); `handout.tex`, `exercises.html`, `exercises/{README.md,data.sql,fixtures.json,tests.py,week13.sql}`, `solutions/week13.sql`, `exercises.zip`.
- **Objectives:** Write `SELECT`, join, self-join, `GROUP BY`/`HAVING`, tie-broken `ORDER BY`/`LIMIT`, and `NULL`-safe anti-join (`E8`) queries; export offline-compatible scripts.
- **Provenance & Publication:** Original SQL tasks. Pre-existing public links on `cs61a/index.html` preserved; `solutions.pdf` without `.tex` source remains noted as a pre-existing limitation.
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction + SQLite (`python tests.py`): starter fails cleanly (`24 check(s) failed across 3 fixtures`, zero unhandled tracebacks); reference (`../solutions`) passes all 3 fixtures (`example`, `boundary-and-repeated-members`, `empty`) x 8 exercises.
  - Misconception checks: `E1 pages >= 260`, `E5 max(days)`, `E6 count(member)`, and `E8 b.title NOT IN (select title from loans)` with `NULL` row all fail (`rc=1`).
  - Browser/download parity: `assembleFullScript()` wraps bare `SELECT`s as `create table eN as ...`; verified bare-`SELECT` export passes offline `tests.py`. HTML UTF-8 clean; JS syntax checked via `node --check`.
  - Limits: Live browser session / `sql.js 1.12.0` CDN / CodeMirror / Highlight.js UI interactions `not tested`.

## Revision 2026-11-25 (sweep: teach every procedure, revisit, meta commentary, proofs of facts used)
- Method boxes (new): build a small table by hand; join two tables; write a SELECT query from a description; write a grouped query; find rows with no match (anti-join with NOT EXISTS or LEFT JOIN ... IS NULL); write a recursive WITH table.
- New subsection "Rows with no match: NULL and anti-joins" (question box, NULL comparison semantics, COUNT(*) vs COUNT(col), NOT EXISTS / LEFT JOIN traces, the NOT IN with NULL trap, revisit). This teaches exercise task e8, which the handout previously did not cover.
- Facts used: W1 (string order) and W2 (counting pairs) are now derived in place, because no Week 2 or Week 5 handout proves them; W3 links to Week 1. The five-stage evaluation rule is now shown by a traced example on `cities`; the self-join "each pair once" claim is argued; the HAVING-on-a-row trap states the actual SQLite result (`4|40`), verified with Python's sqlite3.
- Edge cases added: aggregates on empty input (one row `0||` without GROUP BY, no rows with it), UNION vs UNION ALL duplicates, UPDATE/DELETE with no or no matching WHERE, ties with LIMIT, ties for a bare-column MAX, `-7 % 2` in SQLite, the recursive bound tested on the old row.
- Every question box now has a `\revisit` (aggregation and local tables had none). Examples are one per box. Meta removed (academic-integrity note). Figures: gray unmatched-row text replaced by red haloed text; pale dotted join pairs now bold dotted dark gray; gray arrow and stage labels made black; captions shortened.
- Problem statements E1 and E5 now state the tie-breaks of the exercise contracts; new E9 is the exercise file's task e8 (the handout states the correspondence). Exercises unchanged; tests rerun: starter fails, reference passes on all three fixtures.
- Known limitation: `solutions.pdf` has no `.tex` source in this folder and was not changed, so E9's answer is only in `solutions/week13.sql`.
- Pages: handout 10 -> 14. `check_handout.py`: 0 findings.
