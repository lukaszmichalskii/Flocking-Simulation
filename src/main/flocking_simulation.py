import sys

import pygame

from src.main.flock.flock import Flock
from src.main.flock.flocking_behavior import FlockingBehavior
from src.main.settings.settings import Settings
from src.main.tools.boid_movement_controller import BoidMovementController


class FlockingSimulation:
    """Main class of flocking simulation project"""

    def __init__(self):
        """Initialization of all imported pygame modules"""
        pygame.init()

        self.settings = Settings()
        self.boid_movement_controller = BoidMovementController(self.settings.get_screen_dimensions())

        self.screen = pygame.display.set_mode(self.settings.get_screen_dimensions())
        pygame.display.set_caption("Flocking Simulation")

        self.flock = Flock(flock_size=self.settings.get_flock_size(),
                           boid_parameters=self.settings.get_boid_parameters(),
                           screen_dimensions=self.settings.get_screen_dimensions()).flock

        self.flocking_behavior = FlockingBehavior(self.flock, self.settings.get_limit_values())

    def run(self):
        """Start of main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.get_background_color())
            for boid in self.flock:
                boid.render(self.screen)
                self.boid_movement_controller.control(boid)
                self.flocking_behavior.flock_behavior(boid)
                boid.update()

            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    fs = FlockingSimulation()
    fs.run()
