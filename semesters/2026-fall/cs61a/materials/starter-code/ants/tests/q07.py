from pytest_grader import points


@points(0)
def problem_07_check():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt parameters
    >>> hungry = HungryAnt()
    >>> HungryAnt.food_cost
    LOCKED: 2998f6261651dfd4
    >>> hungry.health
    LOCKED: 4a9a499e7efb36c9
    >>> hungry.chew_cooldown
    LOCKED: c8c78d1d212d7c42
    >>> hungry.cooldown
    LOCKED: 026cc4aa7631e934
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt eats and chews
    >>> hungry = HungryAnt()
    >>> super_bee, wimpy_bee = Bee(1000), Bee(1)
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> place.add_insect(super_bee)
    >>> hungry.action(gamestate)         # super_bee is no match for HungryAnt!
    >>> super_bee.health
    LOCKED: c4b9498c1c236c3d
    >>> place.add_insect(wimpy_bee)
    >>> for _ in range(3):
    ...     hungry.action(gamestate)     # chewing...not eating
    >>> wimpy_bee.health
    LOCKED: 4efe23e5a576cb4d
    >>> hungry.action(gamestate)         # back to eating!
    >>> wimpy_bee.health
    LOCKED: 84f1edbf16b9df13
    """


@points(3)
def problem_07():
    r"""
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Abstraction tests
    >>> original = Ant.__init__
    >>> Ant.__init__ = lambda self, health: print("init")  # If this errors, you are not calling the parent constructor correctly.
    >>> hungry = HungryAnt()
    init
    >>> Ant.__init__ = original
    >>> hungry = HungryAnt()
    >>> # Class vs Instance attributes
    >>> hasattr(HungryAnt, 'cooldown')  # cooldown should be an instance attribute
    False
    >>> hungry.cooldown  # HungryAnt is ready to eat a bee
    0
    >>> HungryAnt.chew_cooldown
    3
    >>> original_chew_cooldown = HungryAnt.chew_cooldown
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt eats and chews
    >>> hungry = HungryAnt()
    >>> bee1 = Bee(1000)              # A Bee with 1000 health
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
    >>> hungry.action(gamestate)
    >>> bee1.health
    0
    >>> bee2 = Bee(1)                 # A Bee with 1 health
    >>> place.add_insect(bee2)
    >>> for _ in range(3):
    ...     hungry.action(gamestate)     # Digesting...not eating
    >>> bee2.health
    1
    >>> hungry.action(gamestate)
    >>> bee2.health
    0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt eats and chews for allotted time
    >>> hungry = HungryAnt()
    >>> bee1 = Bee(1000)              # A Bee with 1000 health
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
    >>> hungry.action(gamestate)
    >>> bee1.health
    0
    >>> bee2 = Bee(1)                 # A Bee with 1 health
    >>> place.add_insect(bee2)
    >>> for _ in range(2):
    ...     hungry.action(gamestate)     # Digesting...not eating, should not finish eating!
    >>> bee2.health
    1
    >>> hungry.action(gamestate)
    >>> bee2.health
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt only waits when chewing
    >>> hungry = HungryAnt()
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> # Wait a few turns before adding Bee
    >>> for _ in range(5):
    ...     hungry.action(gamestate)  # shouldn't be chewing
    >>> bee = Bee(3)
    >>> place.add_insect(bee)
    >>> hungry.action(gamestate)  # Eating time!
    >>> bee.health
    0
    >>> bee = Bee(3)
    >>> place.add_insect(bee)
    >>> for _ in range(3):
    ...     hungry.action(gamestate)     # Should be chewing
    >>> bee.health
    3
    >>> hungry.action(gamestate)
    >>> bee.health
    0
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt chew duration looked up on instance
    >>> very_hungry = HungryAnt()  # Add very hungry caterpi- um, ant
    >>> HungryAnt.chew_cooldown = 0
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(very_hungry)
    >>> for _ in range(100):
    ...     place.add_insect(Bee(3))
    >>> for _ in range(100):
    ...     very_hungry.action(gamestate)   # Eat all the bees!
    >>> len(place.bees)
    0
    >>> HungryAnt.chew_cooldown = original_chew_cooldown
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt dies while eating
    >>> hungry = HungryAnt()
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> place.add_insect(Bee(3))
    >>> hungry.action(gamestate)
    >>> len(place.bees)
    0
    >>> bee = Bee(3)
    >>> place.add_insect(bee)
    >>> bee.action(gamestate) # Bee kills chewing ant
    >>> place.ant is None
    True
    >>> len(place.bees)
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt can't eat a bee at another space
    >>> hungry = HungryAnt()
    >>> gamestate.places["tunnel_0_0"].add_insect(hungry)
    >>> gamestate.places["tunnel_0_1"].add_insect(Bee(3))
    >>> hungry.action(gamestate)
    >>> len(gamestate.places["tunnel_0_1"].bees)
    1
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # test proper call to zero-health callback
    >>> original_zero_health_callback = Insect.zero_health_callback
    >>> Insect.zero_health_callback = lambda x: print("insect died")
    >>> ant = HungryAnt()
    >>> bee = Bee(1000)              # A Bee with 1000 health
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(bee)
    >>> place.add_insect(ant)
    >>> ant.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
    insect died
    >>> Insect.zero_health_callback = original_zero_health_callback
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt removes bee when eating.
    >>> hungry = HungryAnt()
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> place.add_insect(Bee(3))
    >>> place.add_insect(Bee(3))
    >>> hungry.action(gamestate)
    >>> len(place.bees)
    1
    >>> bee = Bee(3)
    >>> place.add_insect(bee)
    >>> bee.action(gamestate) # Bee kills chewing ant
    >>> place.ant is None
    True
    >>> len(place.bees)
    2
    >>> from ants import *
    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
    >>> dimensions = (1, 9)
    >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
    >>> #
    >>> # Testing HungryAnt chooses a random bee in its Place, and that it reduces that bee's health to 0.
    >>> hungry = HungryAnt()
    >>> HungryAnt.chew_cooldown = 0
    >>> place = gamestate.places["tunnel_0_0"]
    >>> place.add_insect(hungry)
    >>> first_bee_chosen_count = 0
    >>> for _ in range(1000):
    ...     place.add_insect(Bee(1)) # Add a bee with 1 health to place
    ...     place.add_insect(Bee(2)) # Add a second bee with 2 health to place
    ...     hungry.action(gamestate) # Eat one of the bees randomly
    ...     assert len(place.bees) == 1, "A bee was not eaten! Make sure you are reducing the bee's health by the correct amount."
    ...     if place.bees[0].health == 2:
    ...             first_bee_chosen_count += 1
    ...     place.remove_insect(place.bees[0])
    >>> first_bee_chosen_count < 1000 # If bees are chosen randomly, HungryAnt should eat the first bee less than 1000 times with high probability
    True
    >>> first_bee_chosen_count > 0 # If bees are chosen randomly, HungryAnt should eat the first bee at least once with high probability
    True
    >>> HungryAnt.chew_cooldown = original_chew_cooldown
    >>> from ants import *
    >>> HungryAnt.implemented
    True
    """
