class Settings:
    """Class stores all simulation settings"""

    def __init__(self):
        """Initialization of simulation settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # boid settings
        self.boid_radius = 3
        self.boid_color = (0, 0, 0)
        self.boid_max_speed = 0.5

        # flock settings
        self.flock_size = 100
