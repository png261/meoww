import os
import pygame

from .game import Game
from .settings import IMAGE_DIR


class Cursor:
    def __init__(self, width=32, height=32):
        self.width = width
        self.height = height
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, "cursor.png"))
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = 0
        self.y = 0
        pygame.mouse.set_visible(False)

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.x = mouse_x 
        self.y = mouse_y 

    def draw(self):
        Game().window.screen.blit(self.image, (self.x,self.y))


