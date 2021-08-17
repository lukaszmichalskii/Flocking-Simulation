from src.main.boid.boid import Boid
from src.main.tools.vector import Vector


def customize_force(boid: Boid,observation: dict, limitations: dict, is_cohesion: bool = False) -> Vector:
    force = observation['steering force']
    flock_mates = observation['flock mates']

    if flock_mates > 0:
        force.divide(flock_mates)
        if is_cohesion:
            force.subtract(boid.position)
        force.set_magnitude(limitations['max speed'])
        force.subtract(boid.velocity)
        force.limit(limitations['max force'])

    return force
