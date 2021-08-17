from src.main.boid.boid import Boid


class FlockingBehavior:
    """Class define rules of flocking behavior"""

    def __init__(self, flock: list, limit_values: dict, force_creation_functions: dict):
        self.__flock = flock
        self.__limit_values = limit_values

        self.flock_behavior_force_creator = force_creation_functions

    def flock_behavior(self, boid: Boid):
        # alignment_force = self.flock_behavior_force_creator['alignment'](boid, self.__flock, self.__limit_values)
        # cohesion = self.flock_behavior_force_creator['cohesion'](boid, self.__flock, self.__limit_values)
        separation = self.flock_behavior_force_creator['separation'](boid, self.__flock, self.__limit_values)
        # boid.acceleration.add(alignment_force)
        # boid.acceleration.add(cohesion)
        boid.acceleration.add(separation)
