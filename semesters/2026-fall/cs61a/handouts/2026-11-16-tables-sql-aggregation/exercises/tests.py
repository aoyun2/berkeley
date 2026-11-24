"""Check the Week 13 SQL exercises:  python3 tests.py   (or python3 tests.py ../solutions)"""
import json
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = sys.argv[1] if len(sys.argv) > 1 else HERE


def canonical_key(row):
    return tuple(
        ("null" if v is None else type(v).__name__, "" if v is None else str(v))
        for v in row
    )


def load_fixtures():
    fixtures_path = os.path.join(HERE, "fixtures.json")
    with open(fixtures_path, encoding="utf-8") as f:
        return json.load(f)


def check_fixture(fixture, script):
    name = fixture["name"]
    setup_sql = fixture["sql"]
    expected = fixture["expected"]

    ref = sqlite3.connect(":memory:")
    db = sqlite3.connect(":memory:")
    try:
        ref.executescript(setup_sql)
        db.executescript(setup_sql)
        try:
            db.executescript(script)
        except sqlite3.Error as e:
            print(f"[{name}] SQL error in week13.sql: {e}")
            return len(expected)

        # Verify source tables were not modified
        for tbl in ("books", "loans"):
            ref_rows = sorted(ref.execute(f"select * from {tbl}").fetchall(), key=canonical_key)
            got_rows = sorted(db.execute(f"select * from {tbl}").fetchall(), key=canonical_key)
            if ref_rows != got_rows:
                print(f"[{name}] FAIL: source table '{tbl}' was modified")
                return len(expected)

        failed = 0
        for qname, spec in expected.items():
            exp_cols = [c.lower() for c in spec["columns"]]
            exp_rows = [tuple(r) for r in spec["rows"]]
            ordered = spec["ordered"]
            try:
                cur = db.execute(f"select * from {qname}")
            except sqlite3.Error as e:
                failed += 1
                print(f"[{name}] {qname}: FAIL ({e})")
                continue

            got_cols = [d[0].lower() for d in cur.description] if cur.description else []
            got_rows = cur.fetchall()

            if got_cols != exp_cols:
                failed += 1
                print(f"[{name}] {qname}: FAIL (columns)")
                print(f"   expected columns: {exp_cols}")
                print(f"   got columns:      {got_cols}")
                continue

            ok = (got_rows == exp_rows) if ordered else (
                sorted(got_rows, key=canonical_key) == sorted(exp_rows, key=canonical_key)
            )
            if ok:
                print(f"[{name}] {qname}: ok")
            else:
                failed += 1
                print(f"[{name}] {qname}: FAIL")
                print(f"   expected {exp_rows}" + (" (in this order)" if ordered else " (any order)"))
                print(f"   got      {got_rows}")
        return failed
    finally:
        ref.close()
        db.close()


def main():
    script_path = os.path.join(FOLDER, "week13.sql")
    with open(script_path, encoding="utf-8") as f:
        script = f.read()

    fixtures = load_fixtures()
    total_failed = 0
    for fx in fixtures:
        total_failed += check_fixture(fx, script)

    if total_failed == 0:
        print(f"all passed ({len(fixtures)} fixtures, 8 exercises)")
        return 0
    print(f"{total_failed} check(s) failed across {len(fixtures)} fixtures")
    return 1


if __name__ == "__main__":
    sys.exit(main())
