import pygame.sprite

from src.main.boid.boid import Boid
from src.main.tools.vector import Vector


def look_around(boid: Boid, flock: pygame.sprite.Group, perception_radius: float,
                is_separation: bool = False, is_cohesion: bool = False) -> dict:

    steering_force = Vector()
    local_flock_mates = 0

    if is_cohesion:
        eyeshot_radius = perception_radius * 2
    else:
        eyeshot_radius = perception_radius

    for boid_entity in flock.sprites():
        dist = Vector.distance(boid.position, boid_entity.position)
        if boid_entity != boid and dist < eyeshot_radius:
            if is_separation:
                diff = Vector(boid.position.x - boid_entity.position.x, boid.position.y - boid_entity.position.y)
                diff.divide(pow(dist, 2))
                steering_force.add(diff)
            else:
                steering_force.add(boid_entity.position)

            local_flock_mates += 1

    data_gathered = {'steering force': steering_force, 'flock mates': local_flock_mates}

    return data_gathered
