class Settings():
    """Class for storage of all settings of the game"""

    def __init__(self):
        """Initialize static game settings"""
        # params of the screen
        self.screen_width = 1200
        self.screen_heihgt = 800
        self.bg_color = (230, 230, 230)
        
        # params of ship
        self.ship_limit = 2 # 3 lives
        
        # params of the bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # params of the alien
        self.fleet_drop_speed = 10

        # game speed
        self.speedup_scale = 1.1
        # increasing of value of alien
        self.scrore_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which changes during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.alien_points = 50
        
        self.fleet_direction = 1 # 1 - means movement to right and -1 means movement to left

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.scrore_scale)
