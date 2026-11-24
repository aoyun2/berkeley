# Packet Audit: CS 61A Week 13 — Tables, SQL & Aggregation (`2026-11-16-tables-sql-aggregation`)

- **Scope:** Week 13 (Lectures 34--36); `handout.tex`, `exercises.html`, `exercises/{README.md,data.sql,fixtures.json,tests.py,week13.sql}`, `solutions/week13.sql`, `exercises.zip`.
- **Objectives:** Write `SELECT`, join, self-join, `GROUP BY`/`HAVING`, tie-broken `ORDER BY`/`LIMIT`, and `NULL`-safe anti-join (`E8`) queries; export offline-compatible scripts.
- **Provenance & Publication:** Original SQL tasks. Pre-existing public links on `cs61a/index.html` preserved; `solutions.pdf` without `.tex` source remains noted as a pre-existing limitation.
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction + SQLite (`python tests.py`): starter fails cleanly (`24 check(s) failed across 3 fixtures`, zero unhandled tracebacks); reference (`../solutions`) passes all 3 fixtures (`example`, `boundary-and-repeated-members`, `empty`) x 8 exercises.
  - Misconception checks: `E1 pages >= 260`, `E5 max(days)`, `E6 count(member)`, and `E8 b.title NOT IN (select title from loans)` with `NULL` row all fail (`rc=1`).
  - Browser/download parity: `assembleFullScript()` wraps bare `SELECT`s as `create table eN as ...`; verified bare-`SELECT` export passes offline `tests.py`. HTML UTF-8 clean; JS syntax checked via `node --check`.
  - Limits: Live browser session / `sql.js 1.12.0` CDN / CodeMirror / Highlight.js UI interactions `not tested`.
