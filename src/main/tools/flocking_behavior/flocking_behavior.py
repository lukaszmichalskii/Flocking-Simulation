from src.main.boid.boid import Boid


class FlockingBehavior:
    """Class define rules of flocking behavior"""

    def __init__(self, flock: list, limit_values: dict, force_creation_functions: dict, perception_radius: float):
        self.__flock = flock
        self.__limit_values = limit_values
        self.__perception_radius = perception_radius

        self.flock_behavior_force_creator = force_creation_functions

    def flock_behavior(self, boid: Boid):
        alignment = self.flock_behavior_force_creator['alignment'](boid,
                                                                   self.__flock,
                                                                   self.__limit_values,
                                                                   self.__perception_radius)
        cohesion = self.flock_behavior_force_creator['cohesion'](boid,
                                                                 self.__flock,
                                                                 self.__limit_values,
                                                                 self.__perception_radius)
        separation = self.flock_behavior_force_creator['separation'](boid,
                                                                     self.__flock,
                                                                     self.__limit_values,
                                                                     self.__perception_radius)

        alignment.multiply(2)
        cohesion.multiply(0.8)
        separation.multiply(1)

        boid.acceleration.add(alignment)
        boid.acceleration.add(cohesion)
        boid.acceleration.add(separation)
