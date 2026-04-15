class Settings():
    """Class for storage of all settings of the game"""

    def __init__(self):
        """Initialize game settings"""
        # params of the screen
        self.screen_width = 1200
        self.screen_heihgt = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        
        # params of the bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3