from random import choice, choices, randrange
from typing import Tuple

import pygame
from pygame.sprite import AbstractGroup

from config import Settings, TEXT_SCOPE


def get_random_char(interval, text_list=TEXT_SCOPE):
    char = choice(text_list)
    while True:
        yield char
        if pygame.time.get_ticks() % interval == 0:
            char = choice(text_list)


class TextObject:

    def __init__(self, pos_x: int, pos_y: int, text_func, color, font_name: str, font_size: int,
                 *groups: AbstractGroup, bold=False, velocity_x=0, velocity_y=0):
        super().__init__(*groups)
        self.pos = [pos_x, pos_y]
        self.interval = randrange(5, 30)
        self.text_func = text_func(self.interval)
        self.color = color
        self.text = next(self.text_func)
        self.font_size = font_size
        self.font = pygame.font.Font(font_name, font_size)
        _, self.bounds = self._get_bounds()
        self.velocity_y = velocity_y
        self.velocity_x = velocity_x

    def _get_bounds(self):
        text_surface = self.font.render(self.text, False, self.color)
        return text_surface, text_surface.get_rect()

    def update(self):
        self.text = next(self.text_func)
        self.pos[1] += self.velocity_y
        if self.pos[1] > Settings.HEIGHT:
            self.pos[1] = - self.font_size
        # if self.pos[1] < 0:
        #     self.pos[1] = Settings.HEIGHT
        if self.pos[0] > Settings.WIDTH:
            self.pos[0] = 0
        if self.pos[0] < 0:
            self.pos[0] = Settings.WIDTH

    def draw(self, surface):
        text_surface, self.bounds = self._get_bounds()
        surface.blit(text_surface, self.pos)


