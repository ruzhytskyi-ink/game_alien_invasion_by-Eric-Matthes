import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Manage resources class"""

    def __init__(self):
        """Initialization of the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heihgt))
        
        # FULLSCREEN mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        # Creating an instance to store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Creating Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Run main game cycle"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

            # Showing of the last painted screen
            pygame.display.flip()

    def _check_events(self):
        """Works with pushes the buttons and mouse cliks"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)  

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game while Play button is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset game settings
            self.settings.initialize_dynamic_settings()
            
            # reset game statistacs
            self.stats.reset_stats()         
            self.stats.game_active = True

            # clean the lists of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # creating of new fleet and centering the ship
            self._create_fleet()
            self.ship.center_ship()

            # the mouse pointer disapeares
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        # Responds to keystrokes
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.type == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # Responds to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creating of new bullet and intersection it in group Bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and destroy old bullets"""
        self.bullets.update()
                
        # removing bullets that have gone-off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # debug
            # print(len(self.bullets))
        self._check_bullet_alien_collisions()

        

    def _check_bullet_alien_collisions(self):
        """Handling collisions between bullets and aliens"""
        # Deleting bullets and aliens 
        
        # checking hits on aliens
        # if a hit is detected, delete bullet and alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # destroing current bullets, speed increasing
            # and creating of the new fleet
            self.bullets.empty()
            self._create_fleet()  
            self.settings.increase_speed()  

    def _create_alien(self, alien_number, row_number):
        """creating of alien and setting its in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        
        """Check if fleet reaches the edge of the screen 
        and update positions of all aliens"""
        self._check_fleet_edges()

        """Update positions of all alins of fleet"""
        self.aliens.update()

        # Checking of colisions "Alien-Ship"
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # check if aliens reached the botoom
        self._check_aliens_botoom() 
            
    def _create_fleet(self):
        """Building an invasion fleet."""
        # Alien creating and calculating number of aliens in the row
        # Distance near the neighbour aliens is equel to width of alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        """Specified the number of rows displayed on the screen"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_heihgt - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
       
        # creating  the fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Reacts when alien reaches the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction() # _
                break

    def _change_fleet_direction(self):
        """Sinks the entire fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Handles a collision between ship and alien"""
        if self.stats.ships_left > 0:
            # decreasing of ship_left
            self.stats.ships_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        # clear a list of aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # creating of new fleet an locate ship in the centre
        self._create_fleet()
        self.ship.center_ship()

        # pause
        sleep(0.5)

    def _check_aliens_botoom(self):
        """Check if alien reaches the botoom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # action the same when alien hits ship
                self._ship_hit()
                break

    def _update_screen(self):
        # Reload the image on the screen and load new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Play button apeares if game  is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # create an exemple and start the game
    ai = AlienInvasion()
    ai.run_game()