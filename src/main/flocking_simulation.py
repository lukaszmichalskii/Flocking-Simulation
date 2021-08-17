import sys

import pygame

from src.main.flock.flock import Flock
from src.main.settings.settings import Settings
from src.main.tools.boid_movement_controller import BoidMovementController
from src.main.tools.flocking_behavior.flocking_behavior import FlockingBehavior
from src.main.tools.flocking_behavior.rules.rules_manager import create_rules


class FlockingSimulation:
    """Main class of flocking simulation project"""

    def __init__(self):
        """Initialization of all imported pygame modules"""
        pygame.init()

        self.settings = Settings()
        self.boid_movement_controller = BoidMovementController(self.settings.get_screen_dimensions())

        self.screen = pygame.display.set_mode(self.settings.get_screen_dimensions(), pygame.NOFRAME)
        self.screen.set_alpha(None)
        pygame.display.set_caption("Flocking Simulation")

        self.flock = Flock(self.settings.get_flock_size(),
                           self.settings.get_boid_parameters(),
                           self.settings.get_screen_dimensions(),
                           self.settings.get_limit_values()).flock

        self.flocking_behavior = FlockingBehavior(self.flock,
                                                  self.settings.get_limit_values(),
                                                  create_rules(),
                                                  self.settings.get_eyeshot())

    def run(self):
        """Start of main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.get_background_color())

            for boid in self.flock.sprites():
                boid.render(self.screen)
                self.boid_movement_controller.control(boid)
                self.flocking_behavior.flock_behavior(boid)
                boid.update()

            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    fs = FlockingSimulation()
    fs.run()
