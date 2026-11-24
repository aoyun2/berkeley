"""Tests for CS 61A Week 4 exercises: python3 tests.py [folder]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
sys.path.insert(0, TARGET_DIR)
import week04  # noqa: E402


def check_sum_digits():
    assert week04.sum_digits(0) == 0
    assert week04.sum_digits(7) == 7
    assert week04.sum_digits(12) == 3
    assert week04.sum_digits(123) == 6
    assert week04.sum_digits(9081) == 18


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


def check_digital_root():
    assert week04.digital_root_steps(0) == (0, 0)
    assert week04.digital_root_steps(9) == (9, 0)
    assert week04.digital_root_steps(19) == (1, 2)
    assert week04.digital_root_steps(999) == (9, 2)
    assert week04.digital_root_steps(199) == (1, 3)


def main():
    checks = [
        ("sum_digits", check_sum_digits),
        ("has_adjacent_equal_digits", check_adjacent),
        ("count_stairs", check_stairs),
        ("digital_root_steps", check_digital_root),
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
