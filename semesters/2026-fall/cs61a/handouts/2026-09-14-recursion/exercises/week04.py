"""CS 61A Week 4 exercises: recursion, helper state, and tree recursion (no loops)."""


def digit_product(n):
    """Return the product of all base-10 digits of integer n >= 0, recursively and without
    loops. A single-digit n is its own product: digit_product(0) == 0, digit_product(7) == 7."""
    raise NotImplementedError("TODO: implement digit_product")


def has_adjacent_equal_digits(n):
    """Return True iff integer n >= 0 has two identical adjacent base-10 digits (use recursion, no loops)."""
    raise NotImplementedError("TODO: implement has_adjacent_equal_digits")


def count_stairs(n, step_a, step_b):
    """Tree recursion: for n >= 0 and integers 0 < step_a < step_b, count ordered climbs of sizes step_a or step_b summing to n."""
    raise NotImplementedError("TODO: implement count_stairs")


def persistence(n):
    """Independent transfer: for integer n >= 0, repeatedly replace n by digit_product(n) until
    n < 10. Return the pair (final single digit, number of replacements made)."""
    raise NotImplementedError("TODO: implement persistence")
