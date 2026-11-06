from pytest_grader import points


@points(0)
def problem_11_check():
    r"""
    >>> from ants import *
    >>> # Testing ScubaThrower parameters
    >>> scuba = ScubaThrower()
    >>> ScubaThrower.food_cost
    LOCKED: c0cf088d4eaf0ecb
    >>> scuba.health
    LOCKED: 695b2927c5a2b9ed
    >>> scuba.name
    LOCKED: 08e8974fbe536908
    >>> scuba.is_waterproof
    LOCKED: 752902797fb2c9a4
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), wet_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing if ScubaThrower is waterproof
    >>> water = gamestate.places["water_0_2"]
    >>> ant = ScubaThrower()
    >>> water.add_insect(ant)
    >>> ant.place is water
    LOCKED: 4e7f67c1d4ff542a
    >>> ant.health
    LOCKED: 9db811b8020536cd
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), wet_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing that ThrowerAnt is not waterproof
    >>> water = gamestate.places["water_0_2"]
    >>> ant = ThrowerAnt()
    >>> ant.is_waterproof
    LOCKED: c7f51932e23fe38a
    >>> water.add_insect(ant)
    >>> ant.place is water
    LOCKED: 851d40259b2d16e6
    >>> ant.health
    LOCKED: 43a1462ec0b587c1
    """


@points(2)
def problem_11():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), wet_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing ScubaThrower on land
    >>> place1 = gamestate.places["tunnel_0_0"]
    >>> place2 = gamestate.places["tunnel_0_4"]
    >>> ant = ScubaThrower()
    >>> bee = Bee(3)
    >>> place1.add_insect(ant)
    >>> place2.add_insect(bee)
    >>> ant.action(gamestate)
    >>> bee.health
    2
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), wet_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing ScubaThrower in the water
    >>> place1 = gamestate.places["water_0_2"]
    >>> place2 = gamestate.places["tunnel_0_4"]
    >>> ant = ScubaThrower()
    >>> bee = Bee(3)
    >>> place1.add_insect(ant)
    >>> place2.add_insect(bee)
    >>> ant.action(gamestate)
    >>> bee.health
    2
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), wet_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> old_thrower_action = ThrowerAnt.action
    >>> old_throw_at = ThrowerAnt.throw_at
    >>> # Testing ScubaThrower Inheritance from ThrowerAnt
    >>> def new_action(self, gamestate):
    ...     raise NotImplementedError()
    >>> def new_throw_at(self, target):
    ...     raise NotImplementedError()
    >>> ThrowerAnt.action = new_action
    >>> test_scuba = ScubaThrower()
    >>> try:
    ...     test_scuba.action(gamestate)
    ... except NotImplementedError:
    ...     print('inherits action!')
    inherits action!
    >>> ThrowerAnt.action = old_thrower_action
    >>> ThrowerAnt.throw_at = new_throw_at
    >>> test_scuba = ScubaThrower()
    >>> try:
    ...     test_scuba.throw_at(Bee(1))
    ... except NotImplementedError:
    ...     print('inherits throw_at!')
    inherits throw_at!
    >>> from ants import *
    >>> ScubaThrower.implemented
    True
    """
