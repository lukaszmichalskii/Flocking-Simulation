from src.main.flock_creator import FlockCreator


class Flock:
    """Class stores flock of simulation"""

    def __init__(self, flock_size, boid_radius, boid_color):
        self.__flock_creator = FlockCreator(flock_size, boid_radius, boid_color)
        self.flock = self.__flock_creator.create_flock()