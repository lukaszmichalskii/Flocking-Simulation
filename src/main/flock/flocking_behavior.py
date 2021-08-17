from src.main.boid.boid import Boid
from src.main.tools.vector import Vector


class FlockingBehavior:
    """Class define rules of flocking behavior"""

    def __init__(self, flock: list, limit_values: dict):
        self.__flock = flock
        self.__max_force = limit_values['max force']
        self.__max_speed = limit_values['max speed']

    def __look_around(self, boid: Boid):
        steering_force = Vector()
        local_flock_mates = 0
        eyeshot_radius = 50
        for boid_entity in self.__flock:
            dist = Vector.distance(boid.position, boid_entity.position)
            if boid_entity != boid and dist < eyeshot_radius:
                steering_force.add(boid_entity.position)
                local_flock_mates += 1

        data_gathered = {'steering force': steering_force, 'flock mates': local_flock_mates}

        return data_gathered

    def __align(self, boid: Boid) -> Vector:
        observation = self.__look_around(boid)
        align_force = observation['steering force']
        flock_mates = observation['flock mates']

        if flock_mates > 0:
            align_force.divide(flock_mates)
            align_force.set_magnitude(self.__max_speed)
            align_force.subtract(boid.velocity)
            align_force.limit(self.__max_force)

        return align_force

    def __cohesion(self, boid: Boid) -> Vector:
        observation = self.__look_around(boid)
        cohesion_force = observation['steering force']
        flock_mates = observation['flock mates']

        if flock_mates > 0:
            cohesion_force.divide(flock_mates)
            cohesion_force.subtract(boid.position)
            cohesion_force.set_magnitude(self.__max_speed)
            cohesion_force.subtract(boid.velocity)
            cohesion_force.limit(self.__max_force)

        return cohesion_force

    def flock_behavior(self, boid: Boid):
        alignment = self.__align(boid)
        cohesion = self.__cohesion(boid)
        boid.acceleration.add(alignment)
        boid.acceleration.add(cohesion)
