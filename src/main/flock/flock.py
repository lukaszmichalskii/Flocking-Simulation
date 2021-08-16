from src.main.flock.flock_creator import FlockCreator


class Flock:
    """Class stores flock of simulation"""

    def __init__(self, flock_size: int, boid_radius: float, boid_color: tuple, screen_dimensions: tuple, boid_max_speed: float):
        self.__flock_creator = FlockCreator(flock_size, boid_radius, boid_color, screen_dimensions, boid_max_speed)
        self.flock = self.__flock_creator.create_flock()
