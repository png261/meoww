import os
import pygame

from .game import Game
from .settings import IMAGE_DIR


class Cat:
    def __init__(self, x, y, width, height):
        self.x = x;
        self.y = y;
        self.vx = x;
        self.vy = y;
        self.width = width
        self.height = height
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, "cat.png"))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.is_flipped_x = False

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.vx = (mouse_x - self.x) / 100
        self.vy = (mouse_y - self.y) / 100

        if not self.is_flipped_x  and self.vx > 0:
            self.is_flipped_x = True
            self.flip()

        if self.is_flipped_x and self.vx < 0:
            self.is_flipped_x = False
            self.flip()

        self.x += self.vx
        self.y += self.vy

        self.x = max(min(self.x, Game().window.width), 0)
        self.y = max(min(self.y, Game().window.height), 0)
    
    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def draw(self):
        from .game import Game
        Game().window.screen.blit(self.image, (self.x,self.y))

