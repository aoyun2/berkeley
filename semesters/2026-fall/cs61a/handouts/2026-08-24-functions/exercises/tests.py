"""Tests for CS 61A Week 1 exercises: python3 tests.py [folder]"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
sys.path.insert(0, TARGET_DIR)
import week01  # noqa: E402


def check_ring():
    assert week01.ring_area_units(5, 3) == 16
    assert week01.ring_area_units(4, 4) == 0
    assert week01.ring_area_units(2.5, 1.5) == 4.0


def check_trace():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        val = week01.trace_step(10)
    assert buf.getvalue().strip() == "step 10", f"printed {buf.getvalue()!r}"
    assert val == 11, f"expected return 11, got {val!r}"
    buf2 = io.StringIO()
    with contextlib.redirect_stdout(buf2):
        val2 = week01.trace_step(-3)
    assert buf2.getvalue().strip() == "step -3"
    assert val2 == -2


def check_clamp_value():
    # inside, below, above, at both ends, a one-point interval, negative bounds
    assert week01.clamp_value(5, 1, 10) == 5, "x inside [low, high] must be returned unchanged"
    assert week01.clamp_value(-3, 1, 10) == 1, "x below low must give low"
    assert week01.clamp_value(14, 1, 10) == 10, "x above high must give high"
    assert week01.clamp_value(1, 1, 10) == 1 and week01.clamp_value(10, 1, 10) == 10, "endpoints are inside"
    assert week01.clamp_value(8, 4, 4) == 4, "a one-point interval [4, 4] always gives 4"
    assert week01.clamp_value(-9, -5, -2) == -5 and week01.clamp_value(0, -5, -2) == -2, "negative bounds"


def check_clamp():
    assert week01.clamp_distance(5, 1, 10) == 0
    assert week01.clamp_distance(1, 1, 10) == 0
    assert week01.clamp_distance(10, 1, 10) == 0
    assert week01.clamp_distance(-3, 1, 10) == 4
    assert week01.clamp_distance(14, 1, 10) == 4
    assert week01.clamp_distance(-8, -5, -2) == 3


def main():
    checks = [
        ("ring_area_units", check_ring),
        ("trace_step", check_trace),
        ("clamp_value", check_clamp_value),
        ("clamp_distance", check_clamp),
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
