import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Manage resources class"""

    def __init__(self):
        """Initialization of the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heihgt))
        pygame.display.set_caption("Alien Invasion")

        pygame.display.set_caption("Alien Invasion")
        # choose colors
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Run main game cycle"""
        while True:
            # check mouse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # recolor the srceen after every cycle
            self.screen.fill(self.settings.bg_color)

            # Showing of the last painted screen
            pygame.display.flip()

if __name__ == '__main__':
    # create an exemple and start the game
    ai = AlienInvasion()
    ai.run_game()