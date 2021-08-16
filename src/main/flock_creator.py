import random

from src.main.boid import Boid


class FlockCreator:
    """Class responsible for creating a flock to take part in the simulation"""

    def __init__(self, flock_size: int, boid_radius: int, boid_color: tuple):
        self.flock_size = flock_size
        self.radius = boid_radius
        self.boid_color = boid_color

    def create_flock(self) -> list:
        flock = []
        for i in range(self.flock_size):
            flock.append(Boid(random.randint(0, 1200), random.randint(0, 800), self.radius, self.boid_color))
        return flock
