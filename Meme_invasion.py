import sys
import pygame


class MemeInvasion:

    def __init__(self):  # initializing
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Meme invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):  # main game cycle
        while True:  # checking for keyboard and mouse status
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)  # background colour
            pygame.display.flip()  # last screen capturing


if __name__ == '__main__':
    ai = MemeInvasion()
    ai.run_game()

