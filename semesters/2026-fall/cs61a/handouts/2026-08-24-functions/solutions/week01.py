"""CS 61A Week 1 reference solutions."""


def ring_area_units(outer_r, inner_r):
    """Return outer_r^2 - inner_r^2."""
    return outer_r * outer_r - inner_r * inner_r


def trace_step(n):
    """Print 'step <n>' and return n + 1."""
    print("step", n)
    return n + 1


def clamp_value(x, low, high):
    """Move x into [low, high]: raise it to at least low, then lower it to at most high."""
    return min(max(x, low), high)


def clamp_distance(x, low, high):
    """Distance from x to the closed interval [low, high]."""
    return max(low - x, 0, x - high)
