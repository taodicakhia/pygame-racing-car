import pygame

class Button:
    def __init__(self, text, x, y, width, height, btn_color=(255, 255, 255), hovered_btn_color=(255, 255, 255), text_color=(0, 0, 0, 220), border_radius=0,) -> None:
        self.text = text
        self.x, self.y, self.width, self.height = x, y, width, height
        self.btn_color, self.hovered_btn_color, self.text_color = btn_color, hovered_btn_color, text_color
        self.border_radius = border_radius
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("Constantia", 30)
        self.textBtn = self.font.render(self.text, True, self.text_color)
        self.textWidth, self.textHeight = self.textBtn.get_width(), self.textBtn.get_height()
        self.clicked = False
        
    def draw_button(self, window: pygame.Surface):
        pygame.draw.rect(window, self.hovered_btn_color if self.is_hovered() else self.btn_color, self.rect, border_radius=self.border_radius)
        window.blit(self.textBtn, (self.x + (self.width - self.textWidth) / 2, self.y + (self.height - self.textHeight) / 2))
    
    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] == 1