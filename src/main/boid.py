import random

import pygame.draw

from src.main.tools.vector import Vector


class Boid:
    """Class represents boid (bird) object in simulation"""

    def __init__(self, x=0, y=0, radius=3, color=(0, 0, 0)):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
        self.radius = radius
        self.color = color

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), self.radius)
