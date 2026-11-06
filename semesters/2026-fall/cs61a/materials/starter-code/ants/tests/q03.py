from pytest_grader import points


@points(0)
def problem_03_check():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> # Testing nearest_bee
    >>> near_bee = Bee(2) # A Bee with 2 health
    >>> far_bee = Bee(3)  # A Bee with 3 health
    >>> hive_bee = Bee(4) # A Bee with 4 health
    >>> hive_place = gamestate.beehive
    >>> hive_place.is_hive # Check if this place is the Hive
    LOCKED: e413f1e7c616d1a6
    >>> hive_place.add_insect(hive_bee)
    >>> thrower.nearest_bee() is hive_bee # Bees in the Hive can never be attacked
    LOCKED: cb1964f6eb45470f
    >>> near_place = gamestate.places['tunnel_0_3']
    >>> far_place = gamestate.places['tunnel_0_6']
    >>> near_place.is_hive # Check if this place is the Hive
    LOCKED: da5f9f30b0708aba
    >>> near_place.add_insect(near_bee)
    >>> far_place.add_insect(far_bee)
    >>> nearest_bee = thrower.nearest_bee()
    >>> thrower.place is ant_place    # Don't change self.place!
    LOCKED: 9c42880ee8eab1e1
    >>> nearest_bee is far_bee
    LOCKED: 890f24cce244d18d
    >>> nearest_bee is near_bee
    LOCKED: eab609f83f59a5eb
    >>> nearest_bee.health
    LOCKED: 31bd1661d64432a9
    >>> thrower.action(gamestate)    # Attack! ThrowerAnts do 1 damage
    >>> near_bee.health
    LOCKED: ee2da95f1e735c0e
    >>> far_bee.health
    LOCKED: d0edc2baa2a8f621
    >>> thrower.place is ant_place    # Don't change self.place!
    LOCKED: adc2904a32d0f99e
    """


@points(2)
def problem_03():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> # Testing Nearest bee not in the beehive
    >>> beehive = gamestate.beehive
    >>> bee = Bee(2)
    >>> beehive.add_insect(bee)      # Adding a bee to the beehive
    >>> thrower.nearest_bee() is bee
    False
    >>> thrower.action(gamestate)    # Attempt to attack
    >>> bee.health                 # Bee health should not change
    2
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> # Test that ThrowerAnt attacks bees on its own square
    >>> near_bee = Bee(2)
    >>> ant_place.add_insect(near_bee)
    >>> thrower.nearest_bee() is near_bee
    True
    >>> thrower.action(gamestate)   # Attack!
    >>> near_bee.health           # should do 1 damage
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> # Test that ThrowerAnt attacks bees at end of tunnel
    >>> near_bee = Bee(2)
    >>> gamestate.places["tunnel_0_8"].add_insect(near_bee)
    >>> thrower.nearest_bee() is near_bee
    True
    >>> thrower.action(gamestate)   # Attack!
    >>> near_bee.health           # should do 1 damage
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> # Test that ThrowerAnt attacks bees 4 places away
    >>> near_bee = Bee(2)
    >>> gamestate.places["tunnel_0_4"].add_insect(near_bee)
    >>> thrower.nearest_bee() is near_bee
    True
    >>> thrower.action(gamestate)   # Attack!
    >>> near_bee.health           # should do 1 damage
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> # Testing ThrowerAnt chooses a random target
    >>> bee1 = Bee(1001)
    >>> bee2 = Bee(1001)
    >>> gamestate.places["tunnel_0_3"].add_insect(bee1)
    >>> gamestate.places["tunnel_0_3"].add_insect(bee2)
    >>> # Throw 1000 times. The first bee should take ~1000*1/2 = ~500 damage,
    >>> # and have ~501 remaining.
    >>> for _ in range(1000):
    ...     thrower.action(gamestate)
    >>> # Test if damage to bee1 is within 6 standard deviations (~95 damage)
    >>> # If bees are chosen uniformly, this is true 99.9999998% of the time.
    >>> def dmg_within_tolerance():
    ...     return abs(bee1.health-501) < 95
    >>> dmg_within_tolerance()
    True
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> thrower = ThrowerAnt()
    >>> ant_place = gamestate.places["tunnel_0_0"]
    >>> ant_place.add_insect(thrower)
    >>> #
    >>> from ants import *
    >>> ThrowerAnt.implemented
    True
    """
