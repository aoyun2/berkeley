"""HW3 solutions obeying actual published syntax restrictions."""

# BEGIN num_eights
def num_eights(n):
    if n < 10:
        return 1 if n == 8 else 0
    if n % 10 == 8:
        return 1 + num_eights(n // 10)
    return num_eights(n // 10)
# END num_eights

# BEGIN distance
def digit_distance(n):
    if n < 10:
        return 0
    return abs(n % 10 - n // 10 % 10) + digit_distance(n // 10)
# END distance

# BEGIN interleaved
def interleaved_sum(n, f_odd, f_even):
    def odd(k):
        if k > n:
            return 0
        return f_odd(k) + even(k + 1)
    def even(k):
        if k > n:
            return 0
        return f_even(k) + odd(k + 1)
    return odd(1)
# END interleaved

# BEGIN coins
def next_smaller_coin(coin):
    if coin == 25:
        return 10
    if coin == 10:
        return 5
    if coin == 5:
        return 1

def count_coins(total):
    def count(remaining, coin):
        if remaining == 0:
            return 1
        if remaining < 0 or coin is None:
            return 0
        return (count(remaining - coin, coin) +
                count(remaining, next_smaller_coin(coin)))
    return count(total, 25)
# END coins

# BEGIN max_subseq
def max_subseq(n, t):
    if n == 0 or t == 0:
        return 0
    with_last = max_subseq(n // 10, t - 1) * 10 + n % 10
    without_last = max_subseq(n // 10, t)
    return max(with_last, without_last)
# END max_subseq

# BEGIN hanoi
def print_move(origin, destination):
    print('Move the top disk from rod', origin, 'to rod', destination)

def move_stack(n, start, end):
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, 'Bad start/end'
    if n == 1:
        print_move(start, end)
    else:
        spare = 6 - start - end
        move_stack(n - 1, start, spare)
        print_move(start, end)
        move_stack(n - 1, spare, end)
# END hanoi

# BEGIN anonymous
from operator import sub, mul

def make_anonymous_factorial():
    return (lambda f: lambda n: f(f, n))(
        lambda f, n: 1 if n == 0 else mul(n, f(f, sub(n, 1))))
# END anonymous
