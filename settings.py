# this file contains the Settings class. This class only
# has an __init__() method, which initializes attributes
# controlling the game’s appearance and the ship’s speed.


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 2

        # Alien settings
        self.alien_speed_factor = 1

        # fleet drop speed controls how quickly the fleet drops down the screen
        self.fleet_drop_speed = 1

        # horizontal speed, fleet direction of 1 represents movement to the right; -1 means to the left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 7
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (255, 69, 0)  # Fiery orange/red color
        self.bullets_allowed = 3