"""Original exam fill-in skeletons, docstrings omitted; intentionally incomplete."""

# BEGIN long_groups_stub
def num_long_groups(n, k):
    assert n > 0 and k > 0, 'n and k must be positive.'
    group_size, count = 0, 0
    while n:
        group_size += 1
        if _____:  # (a)
            count += 1
        if _____:  # (b)
            group_size = 0
        n = n // 10
    return count
# END long_groups_stub

# BEGIN gap_stub
def gap(n, term):
    k, largest = 1, 0
    while _____:  # (a)
        largest = _____  # (b)
        k = k + 1
    return largest


def odd_gap(n, term):
    return gap((n + 1) // 2, _____)  # (c)
# END gap_stub
