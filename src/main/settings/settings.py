class Settings:
    """Class stores all simulation settings"""

    def __init__(self):
        """Initialization of simulation settings"""
        # screen settings
        self.__screen_width = 1200
        self.__screen_height = 800
        self.__bg_color = (230, 230, 230)

        # boid settings
        self.__boid_radius = 3
        self.__boid_color = (0, 0, 0)
        self.__boid_speed = 3

        # flock settings
        self.__flock_size = 100

        # flock behavior settings
        self.__max_force = 0.2
        self.__max_speed = 4

    def get_screen_dimensions(self) -> tuple:
        return self.__screen_width, self.__screen_height

    def get_background_color(self) -> tuple:
        return self.__bg_color

    def get_boid_parameters(self) -> dict:
        boid_parameters = {'radius': self.__boid_radius, 'color': self.__boid_color,
                           'max speed': self.__boid_speed}
        return boid_parameters

    def get_flock_size(self) -> int:
        return self.__flock_size

    def get_limit_values(self) -> dict:
        limit_values = {'max force': self.__max_force, 'max speed': self.__max_speed}
        return limit_values
