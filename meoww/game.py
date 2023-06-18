import os
import pygame

from . import util
from .settings import IMAGE_DIR

@util.singleton
class Game:
    def __init__(self):
        from .cat import Cat
        from .window import Window
        from .cursor import Cursor

        self.FPS = 60
        self.window = Window(700, 700, 60)
        self.window.set_background_image(os.path.join(IMAGE_DIR, "background.png"))
        self.isRunning=True
        self.cursor = Cursor(50, 50)
        self.cat = Cat(0, 0, 100, 100)


    def update(self):
        self.cursor.update()
        self.cat.update()


    def handle_event(self):
        self.window.handle_FPS()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False


    def render(self):
        self.window.fill(("white"))
        self.window.draw_background_image()

        self.cat.draw()
        self.cursor.draw()

        pygame.display.flip()


    def clean(self):
        pygame.quit()
