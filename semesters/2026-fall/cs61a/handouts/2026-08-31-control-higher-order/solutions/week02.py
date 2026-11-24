"""CS 61A Week 2 reference solutions."""


def safe_ratio(num, den):
    """Divide safely without ZeroDivisionError."""
    if den == 0:
        return 0
    return num / den


def count_matches(n, d):
    """Count occurrences of digit d in nonnegative integer n."""
    if n == 0:
        return 1 if d == 0 else 0
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n //= 10
    return count


def make_bounded_scaler(scale, cap):
    """Closure capping scaled input at cap."""
    def apply(x):
        return min(scale * x, cap)
    return apply


def first_threshold(fn, start, limit):
    """Smallest integer k >= start where fn(k) >= limit."""
    k = start
    while fn(k) < limit:
        k += 1
    return k
