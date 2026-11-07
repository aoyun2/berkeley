"""Lecture8's authentic Spring2025 exam reproductions."""

# BEGIN all_digits
def all_digits(n, cond):
    while n:
        if not cond(n % 10):
            return False
        n = n // 10
    return True
# END all_digits

# BEGIN prefix_process
def process(n, check):
    while n:
        if check(n):
            return n
        n = n // 10
    return 0

def prefix_digits(n, cond):
    return process(n, lambda k: all_digits(k, cond))
# END prefix_process

# BEGIN prefix_loop
def prefix_digits_loop(n, cond):
    k = 0
    while n >= pow(10, k):
        if cond(n // pow(10, k) % 10):
            k += 1
        else:
            n = n // 10
            k = 0
    return n
# END prefix_loop

# BEGIN numbered_hailstone
def numbered_hailstone(n):
    def f():
        if n % 2 == 1:
            m = 3 * n + 1
        else:
            m = n // 2
        print(k, n, '->', m)
        return m
    k = 1
    while n > 1:
        k, n = k + 1, f()
# END numbered_hailstone

# BEGIN collapse
def collapse(n):
    left, last = n // 10, n % 10
    if left == 0:
        return last
    elif left % 10 == last:
        return collapse(left)
    else:
        return collapse(left) * 10 + last
# END collapse

# BEGIN contains
def contains(a, b):
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)
# END contains
