"""CS 61A Week 4 exercises: recursion, helpers, mutual and tree recursion.
Do not write while or for anywhere in this file."""


def digit_product(n):
    """Return the product of the digits of the non-negative integer n.

    >>> digit_product(234)
    24
    >>> digit_product(7)
    7
    >>> digit_product(1203)
    0
    """
    if n < 10:
        return n
    return digit_product(n // 10) * (n % 10)


def power(base, exp):
    """Return base ** exp for a non-negative integer exp, using only * and
    recursion. Use the fact that base ** exp == (base ** (exp // 2)) ** 2 when exp
    is even, so the number of calls grows only with the number of digits of exp in base 2.

    >>> power(2, 10)
    1024
    >>> power(3, 0)
    1
    >>> power(5, 3)
    125
    """
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


def is_palindrome(n):
    """Return whether the digits of the positive integer n read the same backward.
    Write a recursive helper inside this function that reverses n (carry the reversed
    part as an argument), then compare. Zeros inside n must work: 10201 is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(1221)
    True
    >>> is_palindrome(1231)
    False
    >>> is_palindrome(10201)
    True
    >>> is_palindrome(7)
    True
    """
    def reverse(n, done):
        if n == 0:
            return done
        return reverse(n // 10, done * 10 + n % 10)
    return reverse(n, 0) == n


def count_down_up(n):
    """Print n, n-1, ..., 1, 0, 1, ..., n-1, n (each on its own line) using recursion.

    >>> count_down_up(2)
    2
    1
    0
    1
    2
    """
    print(n)
    if n > 0:
        count_down_up(n - 1)
        print(n)


def first_true(f, start):
    """Return the smallest integer k >= start for which f(k) is a true value.
    Assume such a k exists.

    >>> first_true(lambda k: k * k > 50, 0)
    8
    >>> first_true(lambda k: k % 7 == 0, 15)
    21
    """
    if f(start):
        return start
    return first_true(f, start + 1)


def collatz_max(n):
    """Starting from n, repeatedly apply: n // 2 if n is even, else 3 * n + 1, until
    reaching 1. Return the largest value reached (including n itself). Use a helper
    that carries the largest value so far.

    >>> collatz_max(6)      # 6 3 10 5 16 8 4 2 1
    16
    >>> collatz_max(1)
    1
    """
    def helper(n, largest):
        largest = max(largest, n)
        if n == 1:
            return largest
        if n % 2 == 0:
            return helper(n // 2, largest)
        return helper(3 * n + 1, largest)
    return helper(n, n)


def is_even(n):
    """Return whether the non-negative integer n is even, using only is_odd, n == 0
    and n - 1 (mutual recursion; no % or //).

    >>> is_even(10), is_even(7), is_even(0)
    (True, False, True)
    """
    if n == 0:
        return True
    return is_odd(n - 1)


def is_odd(n):
    """Return whether the non-negative integer n is odd, using only is_even, n == 0
    and n - 1.

    >>> is_odd(10), is_odd(7), is_odd(0)
    (False, True, False)
    """
    if n == 0:
        return False
    return is_even(n - 1)


def count_paths(rows, cols):
    """Return the number of paths from the top-left to the bottom-right square of a
    grid with the given numbers of rows and columns, moving only right or down.

    >>> count_paths(1, 5)
    1
    >>> count_paths(2, 2)
    2
    >>> count_paths(3, 3)
    6
    >>> count_paths(3, 7)
    28
    """
    if rows == 1 or cols == 1:
        return 1
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)


def count_tilings(n):
    """Return the number of ways to tile a 1-by-n strip with tiles of length 1, 2 and 3.

    >>> count_tilings(1)
    1
    >>> count_tilings(3)    # 1+1+1, 1+2, 2+1, 3
    4
    >>> count_tilings(5)
    13
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_tilings(n - 1) + count_tilings(n - 2) + count_tilings(n - 3)


def count_subset_sums(n, total):
    """Return the number of ways to choose distinct integers from 1, 2, ..., n
    (each used at most once, order does not matter) whose sum is exactly total.

    >>> count_subset_sums(4, 5)     # 1+4, 2+3
    2
    >>> count_subset_sums(5, 0)     # choose nothing
    1
    >>> count_subset_sums(3, 7)     # 1+2+3 is only 6
    0
    >>> count_subset_sums(6, 6)     # 6, 1+5, 2+4, 1+2+3
    4
    """
    if total == 0:
        return 1
    if total < 0 or n == 0:
        return 0
    return count_subset_sums(n - 1, total - n) + count_subset_sums(n - 1, total)


def max_digit_path(n):
    """Choose digits of the positive integer n from left to right, never choosing two
    neighbouring digits. Return the largest possible sum of the chosen digits.

    >>> max_digit_path(1923)    # 9 + 3
    12
    >>> max_digit_path(5)
    5
    >>> max_digit_path(515)     # 5 + 5
    10
    >>> max_digit_path(1991)    # 9 + 1 or 1 + 9
    10
    """
    if n < 10:
        return n
    if n < 100:
        return max(n % 10, n // 10)
    take = n % 10 + max_digit_path(n // 100)
    skip = max_digit_path(n // 10)
    return max(take, skip)
