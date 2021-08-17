import pygame

from src.main.boid.boid import Boid
from src.main.tools.flocking_behavior.look_around import look_around
from src.main.tools.vector import Vector


def separation(boid: Boid, flock: pygame.sprite.Group, limitations: dict) -> Vector:
    observation = look_around(boid, flock, is_separation=True)
    separation_force = observation['steering force']
    flock_mates = observation['flock mates']

    if flock_mates > 0:
        separation_force.divide(flock_mates)
        separation_force.set_magnitude(limitations['max speed'])
        separation_force.subtract(boid.velocity)
        separation_force.limit(limitations['max force'])

    return separation_force
