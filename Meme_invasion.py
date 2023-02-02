import sys
import pygame
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien


class MemeInvasion:

    def __init__(self):  # initializing
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Meme invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):  # main game cycle
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        # checking for keyboard and mouse status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # background colour
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()  # last screen capturing

    def _check_keydown_events(self, event):
        # ship movements press button
        if event.key == pygame.K_RIGHT:  # right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # right
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # quitbutton
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # ship movements release button
        if event.key == pygame.K_RIGHT:  # right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # left
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)


if __name__ == '__main__':
    ai = MemeInvasion()
    ai.run_game()

