import random

import pygame.draw
from pygame.sprite import Sprite

from src.main.tools.vector import Vector


class Boid(Sprite):
    """Class represents boid (bird) object in simulation"""

    def __init__(self, position: Vector, velocity: Vector, acceleration: Vector,
                 boid_parameters: dict, max_speed_limit: float):

        super().__init__()
        self.position = position
        self.velocity = velocity
        self.__speed_interval = (boid_parameters['speed interval'][0], boid_parameters['speed interval'][1])
        self.velocity.set_magnitude(random.uniform(self.__speed_interval[0], self.__speed_interval[1]))
        self.acceleration = acceleration

        self.__radius_interval = (boid_parameters['radius'][0], boid_parameters['radius'][1])
        self.__radius = random.uniform(self.__radius_interval[0], self.__radius_interval[1])
        self.__color = boid_parameters['color']
        self.__max_speed = max_speed_limit

    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.__max_speed)
        self.acceleration.multiply(0)

    def render(self, surface):
        pygame.draw.circle(surface, self.__color, (self.position.x, self.position.y), self.__radius)
