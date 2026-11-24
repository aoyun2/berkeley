"""CS 61A Week 4 reference solutions."""


def sum_digits(n):
    """Sum of digits of nonnegative integer n."""
    if n < 10:
        return n
    return sum_digits(n // 10) + n % 10


def has_adjacent_equal_digits(n):
    """Recursively check whether two adjacent base-10 digits are equal."""
    if n < 10:
        return False
    if n % 10 == (n // 10) % 10:
        return True
    return has_adjacent_equal_digits(n // 10)


def count_stairs(n, step_a, step_b):
    """Count ordered ways to climb n stairs using step_a or step_b."""
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_stairs(n - step_a, step_a, step_b) + count_stairs(n - step_b, step_a, step_b)


def digital_root_steps(n):
    """Return (single_digit_root, reduction_steps) recursively."""
    if n < 10:
        return (n, 0)
    root, steps = digital_root_steps(sum_digits(n))
    return (root, steps + 1)
