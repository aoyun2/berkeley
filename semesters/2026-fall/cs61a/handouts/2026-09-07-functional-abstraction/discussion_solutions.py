"""Discussion2 completed functions and authentic diagram inputs."""

# BEGIN teamwork
def team(work):
    return t(work) - 1

def dream(work, s):
    if work(s-2):
        t = not s
    return not t

work, t = 3, abs
team = dream(team, work + 1) and t
# END teamwork

# BEGIN keeper
def make_keeper(n):
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return f
# END keeper

# BEGIN find_digit
def find_digit(k):
    assert k > 0
    return lambda x: (x // 10**(k - 1)) % 10
# END find_digit

# BEGIN match_k
def match_k(k):
    def check(x):
        while x // (10**k) > 0:
            if x % 10 != (x // (10**k)) % 10:
                return False
            x //= 10
        return True
    return check
# END match_k

# BEGIN which
one = 1

def which():
    one = 3
    def this():
        return one
        return one + 1
    return this
    one = 4
# END which

# BEGIN every
def every(t):
    def digit(n):
        assert n > 0
        while n:
            if not t(n % 10):
                return False
            n = n // 10
        return True
    return digit
# END every

# BEGIN count_if
def count_if(f):
    def g(n):
        count = 0
        while n:
            if f(n % 10):
                count += 1
            n = n // 10
        return count
    return g

def count_at_least(k):
    return count_if(lambda d: d >= k)
# END count_if
