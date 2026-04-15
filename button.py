import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        # Initialise atributes of the button
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set size and settings of buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Building of rect object button and centering it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message created only 1 time
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert msg into the rectangle and centering the text"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Display empty button and showing a message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)