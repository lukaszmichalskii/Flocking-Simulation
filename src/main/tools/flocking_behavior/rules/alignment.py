import pygame.sprite

from src.main.boid.boid import Boid
from src.main.tools.flocking_behavior.look_around import look_around
from src.main.tools.vector import Vector


def alignment(boid: Boid, flock: pygame.sprite.Group, limitations: dict) -> Vector:
    observation = look_around(boid, flock)
    align_force = observation['steering force']
    flock_mates = observation['flock mates']

    if flock_mates > 0:
        align_force.divide(flock_mates)
        align_force.set_magnitude(limitations['max speed'])
        align_force.subtract(boid.velocity)
        align_force.limit(limitations['max force'])

    return align_force
