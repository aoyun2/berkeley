"""Actual Fa26MT1 Q3/Q4 and L5 reproduction of Fa22MT1 Q3(a)."""

# BEGIN classify
def classify(n):
    total, k = 0, 1
    while k < n:
        if n % k == 0:
            total = total + k
        k = k + 1
    if total == n:
        return 'perfect'
    elif total < n:
        return 'deficient'
    else:
        return 'abundant'
# END classify

# BEGIN long_groups
def num_long_groups(n, k):
    assert n > 0 and k > 0
    group_size, count = 0, 0
    while n:
        group_size += 1
        if group_size == k:
            count += 1
        if n % 2 != (n // 10) % 2:
            group_size = 0
        n = n // 10
    return count
# END long_groups

# BEGIN gap
def gap(n, term):
    k, largest = 1, 0
    while k < n:
        largest = max(largest, abs(term(k + 1) - term(k)))
        k = k + 1
    return largest


def odd_gap(n, term):
    return gap((n + 1) // 2, lambda k: term(2 * k - 1))
# END gap
