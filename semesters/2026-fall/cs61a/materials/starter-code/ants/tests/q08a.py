from pytest_grader import points


@points(0)
def problem_08a_check():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> container = ContainerAnt(1)
    >>> container2 = ContainerAnt(2)
    >>> container3 = ContainerAnt(3)
    >>> throw_long = LongThrower(1)
    >>> container.can_contain(container2)
    LOCKED: 8ced25cd14db7d8a
    >>> container3.can_contain(throw_long)
    LOCKED: 78e620dd7746848e
    >>> container = ContainerAnt(2)
    >>> friend = HungryAnt()
    >>> container.ant_contained is None
    LOCKED: 43b97b179a65f2b0
    >>> container.store_ant(friend)
    >>> container.ant_contained is friend
    LOCKED: 4a3049a646b16b0b
    >>> container = ContainerAnt(2)
    >>> container.ant_contained is not None
    LOCKED: 701822d74d0a79f4
    >>> friend = HungryAnt()
    >>> container.store_ant(friend)
    >>> container.ant_contained is friend
    LOCKED: a60b0a4b4ae9c1e5
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(container)
    >>> friend.place = place
    >>> bee = Bee(3)
    >>> place.add_insect(bee)
    >>> container.action(gamestate)  # Container holds a HungryAnt that loves to eat!
    >>> bee.health
    LOCKED: eb29baf773a105a1
    >>> container.can_contain(FireAnt()) # Container already holds another ant!
    LOCKED: 9b9d3b209b34bd4f
    """


@points(1)
def problem_08a():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> container = ContainerAnt(1)
    >>> container.action(gamestate) # ContainerAnt does not have an ant contained, should not have any action taken!
    """
