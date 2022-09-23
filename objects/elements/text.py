import pygame

class Text:
    def __init__(self, text, font="Arial", x=120, y=20, font_size=18, color=(0, 0, 0), center_x=False, center_y=False):
        self.text = text
        self.font = pygame.font.SysFont(font, size=font_size)
        self.font_size = font_size
        self.color = color
        self.x, self.y = x, y
        self.textRender = self.font.render(self.text, True, self.color)
        self.center_x, self.center_y = center_x, center_y
        
    def render(self, window: pygame.Surface):
        window.blit(self.textRender, ((window.get_width() - self.textRender.get_width()) / 2 if self.center_x else self.x, (window.get_height() - self.textRender.get_height()) / 2 if self.center_y else self.y))