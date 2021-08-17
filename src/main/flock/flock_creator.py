import random

from src.main.boid.boid import Boid
from src.main.tools.vector import Vector


class FlockCreator:
    """Class responsible for creating a flock to take part in the simulation"""

    def __init__(self, flock_size: int, boid_parameters: dict, screen_dimensions: tuple):
        self.__boid_parameters = boid_parameters
        self.__flock_size = flock_size
        self.__boid_radius = boid_parameters['radius']
        self.__boid_color = boid_parameters['color']

        self.__area = screen_dimensions
        self.__max_speed = boid_parameters['max speed']

    def create_flock(self) -> list:
        flock = []
        for i in range(self.__flock_size):
            flock.append(Boid(Vector(x=random.randint(0, self.__area[0]), y=random.randint(0, self.__area[1])),
                              velocity=Vector(random.uniform(-self.__max_speed, self.__max_speed), random.uniform(-self.__max_speed, self.__max_speed)),
                              acceleration=Vector(),
                              boid_parameters=self.__boid_parameters))

        return flock
