import sys

import pygame

from src.main.boid import Boid
from src.main.settings import Settings


class FlockingSimulation:
    """Main class of flocking simulation project"""

    def __init__(self):
        """Initialization of all imported pygame modules"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flocking Simulation")

        self.boid = Boid(40, 40, 5)

    def run(self):
        """Start of main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.boid.render(self.screen)

            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    fs = FlockingSimulation()
    fs.run()
