"""Lab1 solutions. Only while/if/arithmetic are used for numeric algorithms."""

# BEGIN lab_print
def welcome():
    print('Go')
    return 'hello'


def cal():
    print('Bears')
    return 'world'

# END lab_print

# BEGIN lab_if
def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
# END lab_if

# BEGIN pick_digit
def pick_digit(n, k):
    """Return digit k from the right (positions start at zero)."""
    return (n // pow(10, k)) % 10
# END pick_digit

# BEGIN middle
def middle(a, b, c):
    """Return the middle of three distinct integers."""
    return a + b + c - min(a, b, c) - max(a, b, c)
# END middle

# BEGIN falling
def falling(n, k):
    product = 1
    while k > 0:
        product = product * n
        n, k = n - 1, k - 1
    return product
# END falling

# BEGIN divisible
def divisible_by_k(n, k):
    current, count = k, 0
    while current <= n:
        print(current)
        current, count = current + k, count + 1
    return count
# END divisible

# BEGIN double_eights
def double_eights(n):
    while n >= 10:
        if n % 100 == 88:
            return True
        n = n // 10
    return False
# END double_eights

# BEGIN sum_digits
def sum_digits(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
# END sum_digits
