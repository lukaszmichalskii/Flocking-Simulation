import sys

import pygame


class FlockingSimulation:
    """Main class of flocking simulation project"""

    def __init__(self):
        """Initialization of all imported pygame modules"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Flocking Simulation")

        self.bg_color = (230, 230, 230)

    def run(self):
        """Start of main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    fs = FlockingSimulation()
    fs.run()
