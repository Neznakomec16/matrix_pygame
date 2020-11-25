from collections import defaultdict

import pygame

from config import Settings, Colours


class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.pre_init()
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.objects = []
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = defaultdict(list)

    def update(self):
        self.all_sprites.update()
        for object in self.objects:
            object.update()

    def draw(self):
        self.all_sprites.draw(self.screen)
        for object in self.objects:
            object.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.type]:
                    handler(event.type)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.type]:
                    handler(event.type)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while self.running:
            self.screen.fill(Colours.BLACK)

            self.update()
            self.draw()
            self.handle_events()

            pygame.display.set_caption(f'{pygame.mouse.get_pos()}')
            pygame.display.update()
            self.clock.tick(Settings.FPS)
