class Settings:
    """Class stores all simulation settings"""

    def __init__(self):
        """Initialization of simulation settings"""
        # screen settings
        self.__screen_width = 1200
        self.__screen_height = 800
        self.__bg_color = (12, 20, 69)  # RGB -> night sky color

        # boid settings
        self.__boid_radius = (3, 5)
        self.__boid_color = (240, 248, 255)  # RGB -> aliceblue color
        self.__boid_speed = (2, 4)

        # flock settings
        self.__flock_size = 50

        # flock behavior perception settings
        self.__eye_shot_radius = 40

        # limit values
        self.__max_force = 1
        self.__max_speed = 4

    def get_screen_dimensions(self) -> tuple:
        return self.__screen_width, self.__screen_height

    def get_background_color(self) -> tuple:
        return self.__bg_color

    def get_boid_parameters(self) -> dict:
        boid_parameters = {'radius': self.__boid_radius, 'color': self.__boid_color,
                           'speed interval': self.__boid_speed}
        return boid_parameters

    def get_flock_size(self) -> int:
        return self.__flock_size

    def get_limit_values(self) -> dict:
        limit_values = {'max force': self.__max_force, 'max speed': self.__max_speed}
        return limit_values

    def get_eyeshot(self):
        return self.__eye_shot_radius
