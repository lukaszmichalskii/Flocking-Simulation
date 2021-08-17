import pygame.sprite

from src.main.boid.boid import Boid
from src.main.tools.flocking_behavior.look_around import look_around
from src.main.tools.flocking_behavior.rules.customize_force import customize_force
from src.main.tools.vector import Vector


def alignment(boid: Boid, flock: pygame.sprite.Group, limitations: dict, perception_radius: float) -> Vector:
    observation = look_around(boid, flock, perception_radius)
    align_force = customize_force(boid, observation, limitations)
    return align_force
