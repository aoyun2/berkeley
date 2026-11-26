"""CS 61A Week 3 reference solutions."""


def curry_binary(f):
    """Curried wrapper for a two-argument function."""
    return lambda x: lambda y: f(x, y)


def repeat_until(f, stop):
    """Apply f to x until the current value satisfies stop; x itself is checked first."""
    def h(x):
        while not stop(x):
            x = f(x)
        return x
    return h


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
