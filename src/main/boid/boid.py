import pygame.draw

from src.main.tools.vector import Vector


class Boid:
    """Class represents boid (bird) object in simulation"""

    def __init__(self, position: Vector, velocity: Vector, acceleration: Vector, boid_parameters: dict):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.__radius = boid_parameters['radius']
        self.__color = boid_parameters['color']

    def update(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit(4)
        self.acceleration.multiply(0)

    def render(self, surface):
        pygame.draw.circle(surface, self.__color, (self.position.x, self.position.y), self.__radius)
