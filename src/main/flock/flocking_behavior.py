from src.main.boid.boid import Boid
from src.main.tools.vector import Vector


class FlockingBehavior:
    """Class define rules of flocking behavior"""

    def __init__(self, flock: list, max_force: float):
        self.__flock = flock
        self.__max_force = max_force

    def __align(self, boid: Boid) -> Vector:
        align_force = Vector()
        total = 0
        eyeshot_radius = 50
        for boid_entity in self.__flock:
            dist = Vector.distance(boid.position, boid_entity.position)
            if boid_entity != boid and dist < eyeshot_radius:
                align_force.add(boid_entity.velocity)
                total += 1

        if total > 0:
            align_force.divide(total)
            align_force.subtract(boid.velocity)
            align_force.limit(self.__max_force)

        return align_force

    def flock_behavior(self, boid: Boid):
        alignment = self.__align(boid)
        boid.acceleration = alignment
