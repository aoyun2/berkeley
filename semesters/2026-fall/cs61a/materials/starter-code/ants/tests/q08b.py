from pytest_grader import points


@points(1)
def problem_08b():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Container ant added before another ant
    >>> container = ContainerAnt(1)
    >>> other_ant = ThrowerAnt()
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(container)  # ContainerAnt in place first
    >>> place.add_insect(other_ant)
    >>> place.ant is other_ant
    False
    >>> place.ant is container
    True
    >>> container.ant_contained is other_ant
    True
    >>> container.place is place
    True
    >>> other_ant.place is container.place  # ThrowerAnt should have the same place attribute as ContainerAnt
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Any Container Ant can be added after another ant
    >>> container = ContainerAnt(1)
    >>> other_ant = ThrowerAnt()
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(other_ant)  # Other ant in place first
    >>> place.ant is other_ant
    True
    >>> place.add_insect(container)
    >>> place.ant is container
    True
    >>> container.ant_contained is other_ant
    True
    >>> container.place is place
    True
    >>> other_ant.place is container.place  # ThrowerAnt should have the same place attribute as ContainerAnt
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Only one ant can be added to a container
    >>> container = ContainerAnt(1)
    >>> a = ThrowerAnt()
    >>> b = ThrowerAnt()
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(container)
    >>> place.add_insect(a)
    >>> place.add_insect(b)
    Traceback (most recent call last):
    ...
    AssertionError: Too many ants in tunnel_0_0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
    >>> #
    >>> # Combination of add and remove
    >>> container = ContainerAnt(1)
    >>> a = ThrowerAnt()
    >>> b = ThrowerAnt()
    >>> place = gamestate.places['tunnel_0_0']
    >>> place.add_insect(a)
    >>> place.add_insect(container)
    >>> container.remove_from(place)
    >>> place.ant is a
    True
    >>> container = ContainerAnt(1)
    >>> place.add_insect(container)
    >>> a.remove_from(place)
    >>> place.add_insect(b)
    >>> place.ant is container
    True
    >>> b.place is place
    True
    """
