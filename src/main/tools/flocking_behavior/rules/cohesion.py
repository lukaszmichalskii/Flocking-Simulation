import pygame

from src.main.boid.boid import Boid
from src.main.tools.flocking_behavior.look_around import look_around
from src.main.tools.vector import Vector


def cohesion(boid: Boid, flock: pygame.sprite.Group, limitations: dict) -> Vector:
    observation = look_around(boid, flock)
    cohesion_force = observation['steering force']
    flock_mates = observation['flock mates']

    if flock_mates > 0:
        cohesion_force.divide(flock_mates)
        cohesion_force.subtract(boid.position)
        cohesion_force.set_magnitude(limitations['max speed'])
        cohesion_force.subtract(boid.velocity)
        cohesion_force.limit(limitations['max force'])

    return cohesion_force
