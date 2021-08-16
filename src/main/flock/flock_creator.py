import random

from src.main.boid.boid import Boid
from src.main.tools.vector import Vector


class FlockCreator:
    """Class responsible for creating a flock to take part in the simulation"""

    def __init__(self, flock_size: int, boid_radius: int, boid_color: tuple, screen_dimensions: tuple, boid_max_speed: float):
        self.flock_size = flock_size
        self.radius = boid_radius
        self.boid_color = boid_color

        self.area = screen_dimensions
        self.max_speed = boid_max_speed

    def create_flock(self) -> list:
        flock = []
        for i in range(self.flock_size):
            flock.append(Boid(Vector(x=random.randint(0, self.area[0]), y=random.randint(0, self.area[1])),
                              radius=self.radius,
                              color=self.boid_color,
                              velocity=Vector(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))))

        return flock
