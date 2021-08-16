from src.main.boid.boid import Boid


class BoidMovementController:
    """Class control boid objects to not leave designated area"""

    def __init__(self, screen_dimensions: tuple):
        self.areaSize = screen_dimensions

    def control(self, boid: Boid):
        if self.__check_x(boid.position.x):
            boid.velocity.x *= -1
        elif self.__check_y(boid.position.y):
            boid.velocity.y *= -1

    def __check_x(self, x: float) -> bool:
        if x < 0 or x > self.areaSize[0]:
            return True

    def __check_y(self, y: float) -> bool:
        if y < 0 or y > self.areaSize[1]:
            return True
