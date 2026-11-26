"""Tests for CS 61A Week 4 exercises: python3 tests.py [folder]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
sys.path.insert(0, TARGET_DIR)
import week04  # noqa: E402


def check_digit_product():
    assert week04.digit_product(0) == 0, "0 is a single digit: its product is 0"
    assert week04.digit_product(7) == 7, "a single digit is its own product"
    assert week04.digit_product(23) == 6
    assert week04.digit_product(234) == 24
    assert week04.digit_product(105) == 0, "a 0 digit inside the number makes the product 0"
    assert week04.digit_product(1111) == 1, "the base case must not return 0 or skip the leading digit"


def check_adjacent():
    assert week04.has_adjacent_equal_digits(7) is False
    assert week04.has_adjacent_equal_digits(112) is True
    assert week04.has_adjacent_equal_digits(100) is True
    assert week04.has_adjacent_equal_digits(121) is False
    assert week04.has_adjacent_equal_digits(123445) is True


def check_stairs():
    assert week04.count_stairs(0, 1, 3) == 1
    assert week04.count_stairs(4, 1, 3) == 3
    assert week04.count_stairs(5, 1, 3) == 4
    # Changed step sizes (catches hardcoded 1 and 3)
    assert week04.count_stairs(6, 2, 3) == 2
    assert week04.count_stairs(5, 2, 4) == 0


def check_persistence():
    assert week04.persistence(0) == (0, 0), "a single digit needs zero replacements"
    assert week04.persistence(9) == (9, 0)
    assert week04.persistence(39) == (4, 3), "39 -> 27 -> 14 -> 4"
    assert week04.persistence(77) == (8, 4), "77 -> 49 -> 36 -> 18 -> 8"
    assert week04.persistence(105) == (0, 1), "105 -> 0"


def main():
    checks = [
        ("digit_product", check_digit_product),
        ("has_adjacent_equal_digits", check_adjacent),
        ("count_stairs", check_stairs),
        ("persistence", check_persistence),
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
