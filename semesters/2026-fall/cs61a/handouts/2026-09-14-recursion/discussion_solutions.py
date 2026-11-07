"""Completed Discussion3 code, including the optional call-only robot."""

# BEGIN swipe
def swipe(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)
# END swipe

# BEGIN skip_fact
def skip_factorial(n):
    if n <= 2:
        return n
    return n * skip_factorial(n - 2)
# END skip_fact

# BEGIN recursive_prime
def is_prime(n):
    def f(i):
        """Return whether n has no positive divisor from i through n-1."""
        if i == n:
            return True
        if n % i == 0:
            return False
        return f(i + 1)
    return f(2)
# END recursive_prime

# BEGIN hailstone
def hailstone(n):
    print(n)
    if n % 2 == 0:
        return even(n)
    return odd(n)

def even(n):
    return hailstone(n // 2) + 1

def odd(n):
    if n == 1:
        return 1
    return hailstone(n * 3 + 1) + 1
# END hailstone

# BEGIN sevens
def sevens(n, k):
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    if n % 10 == 7:
        return True
    return has_seven(n // 10)
# END sevens

# BEGIN karel
def main():
    if front_is_clear():
        move()
        if front_is_clear():
            move()
            main()
            move()
        else:
            turn_left()
            turn_left()
    else:
        turn_left()
        turn_left()
# END karel
