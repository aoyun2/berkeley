from pytest_grader import points


@points(0)
def problem_01_check():
    r"""
    >>> from ants import *
    >>> from ants_plans import *
    >>> Ant.food_cost
    LOCKED: a4319343368884c1
    >>> HarvesterAnt.food_cost
    LOCKED: 8b12b84ba4613d2f
    >>> ThrowerAnt.food_cost
    LOCKED: 6baee01b3b736b49
    >>> # Testing HarvesterAnt action
    >>> # Create a test layout where the colony is a single row with 9 tiles
    >>> beehive = Hive(make_test_assault_plan())
    >>> gamestate = GameState(beehive, ant_types(), dry_layout, (1, 9))
    >>> #
    >>> gamestate.food = 4
    >>> harvester = HarvesterAnt()
    >>> # Note: initializing an Ant doesn't cost food,
    >>> # only deploying an Ant in the game layout does.
    >>> # For this test case, Ants can still take actions
    >>> # without being deployed in the game layout.
    >>> #
    >>> gamestate.food
    LOCKED: 7398979dda433615
    >>> harvester.action(gamestate) # Executing harvester's action method. This symbolizes the ant taking one turn.
    >>> gamestate.food
    LOCKED: 14194b41f6b0e186
    >>> harvester.action(gamestate) # Harvester's action is executed again.
    >>> gamestate.food
    LOCKED: 6de9ddc92249702c
    """


@points(1)
def problem_01():
    r"""
    >>> from ants import *
    >>> from ants_plans import *
    >>> from ants import *
    >>> HarvesterAnt.implemented
    True
    """
