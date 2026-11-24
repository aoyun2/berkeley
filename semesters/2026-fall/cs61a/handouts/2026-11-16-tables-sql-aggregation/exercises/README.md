# Week 13 exercises (CS 61A)

Original SQL exercises (E1--E8) on tables, `SELECT`, joins, and aggregation. Write them yourself without AI help.

## Files
- `data.sql`: creates the base example tables `books` and `loans` (shown in the handout).
- `fixtures.json`: defines all three independent test datasets (`example`, `boundary-and-repeated-members`, and `empty`).
- `week13.sql`: starter file defining tables `e1` through `e8`; replace each `select 'YOUR QUERY HERE' as unfinished;` with your query.
- `tests.py`: offline SQLite test suite that runs every query independently on all three datasets, checking column names, ordering where required, multiplicity, and untouched source tables.

## Contracts
- `e1(title)`: books with `pages > 260`, ordered by `pages desc, title`.
- `e2(author, n, total)`: authors with at least 2 books, ordered by `author`.
- `e3(member, title, author)`: one row per loan (any order; preserve duplicates).
- `e4(first, second)`: distinct pairs `(first < second)` of books by the same author (any order).
- `e5(member, total)`: member with maximum total loan days (break ties alphabetically by `member`; empty for empty `loans`).
- `e6(author)`: authors whose books were borrowed by at least 2 distinct members (any order).
- `e7(decade, n)`: `(year/10)*10` decade and book count, ordered by `decade`.
- `e8(title)`: titles never borrowed, ordered by `title`; must handle `NULL` values in `loans.title`.

## Running checks
From this folder (uses Python's built-in `sqlite3`, no install required):

    python3 tests.py
    python3 tests.py ../solutions
