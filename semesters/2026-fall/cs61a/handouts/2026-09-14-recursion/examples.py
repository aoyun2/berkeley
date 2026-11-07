"""Week4 executable lecture and CP1.7 examples."""

# BEGIN reverse_curry
def reverse(f):
    return lambda x, y: f(y, x)

def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

square = curry(reverse(pow))(2)
cube = curry(reverse(pow))(3)
# END reverse_curry

# BEGIN exp_parent
def exp(x):
    def base(b):
        return pow(b, x)
    return base
# END exp_parent

# BEGIN sum_digits
def sum_digits(n):
    if n < 10:
        return n
    all_but_last, last = n // 10, n % 10
    return sum_digits(all_but_last) + last
# END sum_digits

# BEGIN fact
def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n - 1) * n
# END fact

# BEGIN fact_iter
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total
# END fact_iter

# BEGIN fact_k
def fact_k(n, k):
    if n == 0 or n == 1:
        return k
    return fact_k(n - 1, k * n)

def fact_tail(n):
    def f(n, k):
        if n == 0 or n == 1:
            return k
        return f(n - 1, k * n)
    return f(n, 1)
# END fact_k

# BEGIN play
def play(strategy0, strategy1, goal=21):
    def f(n, who):
        if n >= goal:
            return who
        if who == 0:
            n, who = n + strategy0(n), 1
        else:
            n, who = n + strategy1(n), 0
        return f(n, who)
    return f(0, 0)
# END play

# BEGIN parity
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
# END parity

# BEGIN cascade
def cascade(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)
# END cascade

# BEGIN alice_bob
def play_alice(n):
    if n == 0:
        print('Bob wins!')
    else:
        play_bob(n - 1)

def play_bob(n):
    if n == 0:
        print('Alice wins!')
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1)
# END alice_bob

# BEGIN unique_factors
def smallest_factor(n):
    def smallest_divisor(k):
        if n % k == 0:
            return k
        return smallest_divisor(k + 1)
    return smallest_divisor(2)

def unique_prime_factors(n):
    k = smallest_factor(n)
    def no_k(n):
        if n == 1:
            return 0
        if n % k != 0:
            return unique_prime_factors(n)
        return no_k(n // k)
    return 1 + no_k(n)
# END unique_factors

# BEGIN fib
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)
# END fib

# BEGIN partitions
def count_partitions(n, m):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m == 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)
# END partitions

# BEGIN parking
def count_park(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return 2 * count_park(n - 1) + count_park(n - 2)
# END parking

# BEGIN streak
def streak(n):
    return (n >= 1 and n <= 6) or (n >= 10 and
        n % 10 == n // 10 % 10 and streak(n // 10))
# END streak
