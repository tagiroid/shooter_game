import sys
import pygame
from settings import Settings
from ship import Ship

class MemeInvasion:

    def __init__(self):  # initializing
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Meme invasion")
        self.ship = Ship(self)

    def run_game(self):  # main game cycle
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # checking for keyboard and mouse status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # background colour
        self.ship.blitme()
        pygame.display.flip()  # last screen capturing

if __name__ == '__main__':
    ai = MemeInvasion()
    ai.run_game()
