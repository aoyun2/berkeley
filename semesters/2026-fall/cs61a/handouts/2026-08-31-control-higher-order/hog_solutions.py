"""Hog study solutions. Original materials remain unchanged."""
# BEGIN hog_setup
from dice import six_sided, make_test_dice
GOAL = 100
# END hog_setup

# BEGIN roll_dice
def roll_dice(num_rolls, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    total, rolled_one, count = 0, False, 0
    while count < num_rolls:
        outcome = dice()
        total = total + outcome
        if outcome == 1:
            rolled_one = True
        count = count + 1
    if rolled_one:
        return 1
    return total
# END roll_dice

# BEGIN boar
def boar_brawl(player_score, opponent_score):
    own_ones = player_score % 10
    other_tens = (opponent_score // 10) % 10
    return max(3 * abs(other_tens - own_ones), 1)
# END boar

# BEGIN take_turn
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    return roll_dice(num_rolls, dice)
# END take_turn

# BEGIN hog_helpers
def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    return player_score + take_turn(num_rolls, player_score, opponent_score, dice)


def is_prime(n):
    """Provided Hog helper; domain is positive integers."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def always_roll_5(score, opponent_score):
    return 5


def catch_up(score, opponent_score):
    if score < opponent_score:
        return 6
    else:
        return 5
# END hog_helpers

# BEGIN sus
def num_factors(n):
    count, k = 0, 1
    while k <= n:
        if n % k == 0:
            count = count + 1
        k = k + 1
    return count


def sus_points(score):
    factors = num_factors(score)
    if factors == 3 or factors == 4:
        candidate = score + 1
        while not is_prime(candidate):
            candidate = candidate + 1
        return candidate
    return score


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    return sus_points(simple_update(num_rolls, player_score, opponent_score, dice))
# END sus

# BEGIN hog_play
def play(strategy0, strategy1, update, score0=0, score1=0,
         dice=six_sided, goal=GOAL):
    who = 0
    while score0 < goal and score1 < goal:
        if who == 0:
            rolls = strategy0(score0, score1)
            score0 = update(rolls, score0, score1, dice)
        else:
            rolls = strategy1(score1, score0)
            score1 = update(rolls, score1, score0, dice)
        who = 1 - who
    return score0, score1
# END hog_play

# BEGIN always
def always_roll(n):
    assert n >= 0 and n <= 10
    def strategy(score, opponent_score):
        return n
    return strategy
# END always

# BEGIN is_always
def is_always_roll(strategy, goal=GOAL):
    expected = strategy(0, 0)
    score = 0
    while score < goal:
        opponent = 0
        while opponent < goal:
            if strategy(score, opponent) != expected:
                return False
            opponent = opponent + 1
        score = score + 1
    return True
# END is_always

# BEGIN averaged
def make_averaged(func_to_average, iterations=1000):
    def averaged(*args):
        total, count = 0, 0
        while count < iterations:
            total = total + func_to_average(*args)
            count = count + 1
        return total / iterations
    return averaged
# END averaged

# BEGIN max_rolls
def max_scoring_num_rolls(dice=six_sided, iterations=1000):
    average = make_averaged(roll_dice, iterations)
    rolls, best_rolls, best_score = 1, 1, 0
    while rolls <= 10:
        score = average(rolls, dice)
        if score > best_score:
            best_rolls, best_score = rolls, score
        rolls = rolls + 1
    return best_rolls
# END max_rolls

# BEGIN boar_strategy
def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    return num_rolls
# END boar_strategy

# BEGIN sus_strategy
def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    gain = sus_update(0, score, opponent_score) - score
    if gain >= threshold:
        return 0
    return num_rolls
# END sus_strategy

# BEGIN final_strategy
def final_strategy(score, opponent_score):
    """Take a certain win with zero dice; otherwise use the Sus threshold."""
    if sus_update(0, score, opponent_score) >= GOAL:
        return 0
    return sus_strategy(score, opponent_score, threshold=11, num_rolls=6)
# END final_strategy
