from src.main.boid.boid import Boid


class BoidMovementController:
    """Class control boid objects to not leave designated area"""

    def __init__(self, screen_dimensions: tuple):
        self.areaSize = screen_dimensions

    def control(self, boid: Boid):
        self.__control_x(boid)
        self.__control_y(boid)

    def __control_x(self, boid: Boid):
        if boid.position.x > self.areaSize[0]:
            boid.position.x = 0
        elif boid.position.x < 0:
            boid.position.x = self.areaSize[0]

    def __control_y(self, boid):
        if boid.position.y > self.areaSize[1]:
            boid.position.y = 0
        elif boid.position.y < 0:
            boid.position.y = self.areaSize[1]
