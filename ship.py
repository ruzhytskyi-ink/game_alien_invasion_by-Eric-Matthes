import pygame

class Ship():
    """Class to control the ship"""
    def __init__(self, ai_game):
        """Initializing of the ship and create the start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Download image of ship and recieve rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Every new ship appear at the down side
        self.rect.midbottom = self.screen_rect.midbottom

        # save coordinates of the ship cenre
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # update ship location depends of the flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # updating rect atribute base on self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image, self.rect)