import pygame


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen  # ship initialization
        self.screen_rect = self.screen.get_rect()  # ship starting position
        self.settings = ai_game.settings

        # getting ship and drawing rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # each new ship is settled at the mid-bottom

        self.x = float(self.rect.x)
        self.moving_right = False  # default state of ship movements to the right
        self.moving_left = False  # default state of ship movements to the left

    def update(self):
        # moving ship while the arrow button is pressed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # current position
