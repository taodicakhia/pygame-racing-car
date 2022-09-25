import pygame

from utils import edit_tuple

class ImageRect:
    def __init__(self, image: pygame.Surface, x, y, width, height, color=(255, 255, 255), border_radius=0):
        self.image = image
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.border_radius = border_radius
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_faded = False
        
    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, self.color, self.rect, border_radius=self.border_radius)
        window.blit(self.image, (self.x + (self.width - self.image.get_width()) / 2 + 15, self.y + (self.height - self.image.get_height()) / 2 + 10))
    
    def scale_image(self, size):
        self.width, self.height = size
        self.image = pygame.transform.scale(self.image, (self.width, self.height))