from src.main.flock.flock_creator import FlockCreator


class Flock:
    """Class stores flock of simulation"""

    def __init__(self, flock_size: int, boid_parameters: dict, screen_dimensions: tuple):
        self.__flock_creator = FlockCreator(flock_size, boid_parameters, screen_dimensions)
        self.flock = self.__flock_creator.create_flock()
