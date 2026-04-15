class GameStats():
    """Tracking statistics for game 'Alien Invasion'."""

    def __init__(self, ai_game):
        """Initialises of statistic"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game launches with inactive mode
        self.game_active = False

    def reset_stats(self):
        """Initialises of statistic, that changes during the game"""
        self.ships_left = self.settings.ship_limit