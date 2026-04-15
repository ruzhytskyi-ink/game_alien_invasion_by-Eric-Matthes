import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class represents 1 alien"""

    def __init__(self, ai_game):
        """Initialize alien and set its current position"""
        super().__init__()
        self.screen = ai_game.screen

        # load image of alien and set RECT atribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every new alien appears at top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Maintaining the alien’s precise horizontal position.
        self.x = float(self.rect.x)
