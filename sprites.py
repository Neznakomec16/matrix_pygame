import random

import pygame
from config import Settings, Colours


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(Colours.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, Settings.WIDTH), random.randint(0, Settings.HEIGHT))
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.05

    def update(self):
        if self.rect.center[0] >= Settings.WIDTH or self.rect.center[0] <= 0:
            self.velocity_x = -self.velocity_x
        if self.rect.center[1] >= Settings.HEIGHT or self.rect.center[1] <= 0:
            self.velocity_y = -self.velocity_y
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.velocity_y > 0:
            self.velocity_y += self.acceleration
        else:
            self.velocity_y -= self.acceleration
