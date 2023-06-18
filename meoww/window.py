import pygame

class Window:
    def __init__(self, width, height, FPS):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.background_image = None

    def set_background_image(self, img_path):
        self.background_image = pygame.image.load(img_path)
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def draw_background_image(self):
        if not self.background_image is None:
            self.screen.blit(self.background_image, (0, 0))

    def fill(self, color: pygame.Color):
        self.screen.fill(color)

    def handle_FPS(self):
        self.clock.tick(self.FPS)

    def get_screen(self):
        return self.screen
