"""CS 61A Week 3 reference solutions."""


def curry_binary(f):
    """Curried wrapper for a two-argument function."""
    return lambda x: lambda y: f(x, y)


def compose_n(f, n):
    """Compose f with itself n times (n >= 0)."""
    def repeated(x):
        val = x
        k = 0
        while k < n:
            val = f(val)
            k += 1
        return val
    return repeated


def make_alternator(f, g):
    """Dispatch f on even integers and g on odd integers."""
    return lambda n: f(n) if n % 2 == 0 else g(n)


def max_over_range(fn, lo, hi):
    """Maximum of fn(k) across integers lo <= k <= hi."""
    best = fn(lo)
    k = lo + 1
    while k <= hi:
        val = fn(k)
        if val > best:
            best = val
        k += 1
    return best
