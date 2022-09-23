import pygame


class Image:
    def __init__(self, image: pygame.Surface):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.size = self.width, self.height
        self.angle = 0

    def scale(self, size):
        self.width, self.height = size
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)

    def rotate(self, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle)

    def show_image(self, window: pygame.Surface, center=False):
        center_blit = self.get_center_pos_of_window(window) if center is True else (0, 0)
        window.blit(self.image, center_blit)

    def show_image_with_position(self, window: pygame.Surface, position=(0, 0)):
        window.blit(self.image, position)

    def get_center_pos_of_window(self, window: pygame.Surface):
        return self.image.get_rect(center = window.get_rect().center)
