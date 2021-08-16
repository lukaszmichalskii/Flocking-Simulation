import pygame.draw

from src.main.tools.vector import Vector


class Boid:
    """Class represents boid (bird) object in simulation"""

    def __init__(self, position: Vector, velocity: Vector, radius: float, color: tuple):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), self.radius)
