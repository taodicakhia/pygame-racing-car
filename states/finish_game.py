from objects.elements.button import Button
from objects.elements.text import Text
from states.state import State
import pygame

class FinishGame(State):
    def __init__(self, game):
        super().__init__(game)
        self.rect_notification = pygame.Rect(361, 264, 750, 300)
        self.text_completed = Text("Bạn đã hoàn thành chặng đua.", font="Constantia", x = 361, y = 320, font_size=30, center_x=True)
        self.again_btn = Button("Tiếp tục", 400, 460, 220, 50, btn_color=(120, 255, 120), hovered_btn_color=(46, 255, 46), border_radius=6, font_size=20)
        self.quit_btn = Button("Về màn hình chính", 855, 460, 220, 50, btn_color=(255, 128, 128), hovered_btn_color=(255, 102, 102), text_color=(255, 255, 255), border_radius=6, font_size=20)
        
    def render(self):
        pygame.draw.rect(self.main.window, (255, 255, 255), self.rect_notification, border_radius=6)
        self.text_completed.render(self.main.window)
        self.again_btn.draw_button(self.main.window)
        self.quit_btn.draw_button(self.main.window)
        
        if self.again_btn.is_hovered() and self.again_btn.is_clicked():
            self.exit_state()
        elif self.quit_btn.is_hovered() and self.again_btn.is_clicked():
            self.exit_state()
            del self.main.state_stack[-1]
        
        pygame.display.update()