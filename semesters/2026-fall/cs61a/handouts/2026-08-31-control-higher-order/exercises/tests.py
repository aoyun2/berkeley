"""Tests for CS 61A Week 2 exercises: python3 tests.py [folder]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
sys.path.insert(0, TARGET_DIR)
import week02  # noqa: E402


def check_safe_ratio():
    assert week02.safe_ratio(10, 4) == 2.5
    assert week02.safe_ratio(9, 0) == 0
    assert week02.safe_ratio(0, 0) == 0


def check_count_matches():
    assert week02.count_matches(12202, 2) == 3
    assert week02.count_matches(0, 0) == 1
    assert week02.count_matches(0, 7) == 0
    assert week02.count_matches(909, 0) == 1


def check_scaler():
    f = week02.make_bounded_scaler(3, 10)
    g = week02.make_bounded_scaler(2, 5)
    assert f(2) == 6
    assert f(4) == 10
    assert f(10) == 10
    assert g(3) == 5
    assert f(2) == 6  # g did not overwrite f


def check_threshold():
    assert week02.first_threshold(lambda k: k * k, 0, 20) == 5
    assert week02.first_threshold(lambda k: k * k, 5, 20) == 5
    assert week02.first_threshold(lambda k: 2 * k + 1, -3, 0) == 0


def main():
    checks = [
        ("safe_ratio", check_safe_ratio),
        ("count_matches", check_count_matches),
        ("make_bounded_scaler", check_scaler),
        ("first_threshold", check_threshold),
    ]
    failed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"{name}: ok")
        except Exception as e:
            failed += 1
            print(f"{name}: FAIL ({type(e).__name__}: {e})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
