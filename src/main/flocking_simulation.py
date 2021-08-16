import sys

import pygame

from src.main.flock import Flock
from src.main.settings import Settings
from src.main.tools.boid_movement_controller import BoidMovementController


class FlockingSimulation:
    """Main class of flocking simulation project"""

    def __init__(self):
        """Initialization of all imported pygame modules"""
        pygame.init()

        self.settings = Settings()
        self.boid_movement_controller = BoidMovementController((self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flocking Simulation")

        self.flock = Flock(self.settings.flock_size, self.settings.boid_radius, self.settings.boid_color).flock

    def run(self):
        """Start of main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            for boid in self.flock:
                boid.render(self.screen)
                boid.position.add(boid.velocity)
                self.boid_movement_controller.control(boid)

            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    fs = FlockingSimulation()
    fs.run()
