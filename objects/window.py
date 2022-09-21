import pygame


class Window:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()

    def update(self, size):
        self.window = pygame.display.set_mode(size)