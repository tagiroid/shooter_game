import sys
import pygame
from settings import Settings
from ship import Ship


class MemeInvasion:

    def __init__(self):  # initializing
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Meme invasion")
        self.ship = Ship(self)

    def run_game(self):  # main game cycle
        while True:
            self._check_events()
            self.ship.update()
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
        pygame.display.flip()  # last screen capturing

    def _check_keydown_events(self, event):
        # ship movements press button
        if event.key == pygame.K_RIGHT:  # right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # right
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # quitbutton
            sys.exit()
    def _check_keyup_events(self, event):
        # ship movements release button
        if event.key == pygame.K_RIGHT:  # right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # left
            self.ship.moving_left = False

if __name__ == '__main__':
    ai = MemeInvasion()
    ai.run_game()
