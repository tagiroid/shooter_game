import pygame


class Ship():

    def __init__(self, ai_game):
        self.screen = ai_game.screen  # ship initialization
        self.screen_rect = ai_game.screen.get_rect()  # ship starting position

        # getting ship and drawing rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # each new ship is settled at the mid-bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # current position
