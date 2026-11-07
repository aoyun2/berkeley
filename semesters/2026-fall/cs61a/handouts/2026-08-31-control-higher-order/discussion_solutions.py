"""Discussion1: corrected repeating guard is explicit in the packet."""

# BEGIN race_source
def race(x, y):
    assert y > x and y <= 2 * x
    tortoise, hare, minutes = 0, 0, 0
    while (minutes == 0) or (tortoise - hare):
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes
# END race_source

# BEGIN fizzbuzz
def fizzbuzz(n):
    i = 1
    while i <= n:
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        i = i + 1
# END fizzbuzz

# BEGIN prime
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True
# END prime

# BEGIN unique
def has_digit(n, k):
    assert k >= 0 and k < 10
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False


def unique_digits(n):
    k, count = 0, 0
    while k < 10:
        if has_digit(n, k):
            count = count + 1
        k = k + 1
    return count
# END unique

# BEGIN bottles
bottles = 99
take = 1

def pass_it(around):
    bottles = 98
    return take

remaining = bottles - pass_it(bottles)
bottles = remaining
# END bottles

# BEGIN double_trouble
def double(x):
    return x * 2

def triple(x):
    return x * 3

hat = double
double = triple
# END double_trouble

# BEGIN repeating
def repeating(t, n):
    if pow(10, t - 1) > n:
        return False
    end = n % pow(10, t)
    if end < pow(10, t - 1):  # Added guard: block must have t digits.
        return False
    while n:
        if n % pow(10, t) != end:
            return False
        n = n // pow(10, t)
    return True
# END repeating
