"""Tests for CS 61A Week 3 exercises: python3 tests.py [folder]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
sys.path.insert(0, TARGET_DIR)
import week03  # noqa: E402


def check_curry():
    sub = week03.curry_binary(lambda a, b: a - b)
    sub5 = sub(5)
    assert sub5(2) == 3
    assert sub(10)(4) == 6
    assert week03.curry_binary(pow)(2)(5) == 32


def check_compose_n():
    inc = lambda x: x + 1
    assert week03.compose_n(inc, 0)(7) == 7
    assert week03.compose_n(inc, 1)(7) == 8
    assert week03.compose_n(lambda x: x * 2, 4)(3) == 48


def check_alternator():
    h = week03.make_alternator(lambda n: n * 10, lambda n: -n)
    assert h(0) == 0
    assert h(3) == -3
    assert h(4) == 40
    assert h(-1) == 1


def check_max_over_range():
    assert week03.max_over_range(lambda k: -(k * k) + 4 * k, 0, 5) == 4
    # Must work even when every value in the range is strictly negative
    assert week03.max_over_range(lambda k: -abs(k) - 5, -3, 3) == -5
    assert week03.max_over_range(lambda k: 2 * k, 4, 4) == 8


def main():
    checks = [
        ("curry_binary", check_curry),
        ("compose_n", check_compose_n),
        ("make_alternator", check_alternator),
        ("max_over_range", check_max_over_range),
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
