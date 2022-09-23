import pygame
from objects.elements.button import Button

from objects.elements.image import Image
from objects.elements.text import Text
from states.state import State

class Pause(State):
    def __init__(self, window: pygame.Surface):
        super().__init__(window)
        self.load_assets()
        self.paused_text = Text("Game paused", y = 220, font="Constantia", font_size = 50, center_x=True, color=(255, 255, 255))
        self.resume_button = Button("Resume", 300, 550, 300, 80, btn_color=(120, 255, 120), hovered_btn_color=(46, 255, 46), border_radius=6)
        self.exit_game_button = Button("Return to main menu", 872, 550, 300, 80, btn_color=(255, 128, 128), hovered_btn_color=(255, 102, 102), text_color=(255, 255, 255), border_radius=6)
    
    def load_assets(self):
        self.GRASS = Image(pygame.image.load("images/grass.jpg"))
        self.GRASS.scale((self.width_window, self.height_window))
        
    def render(self):
        self.GRASS.show_image(self.window)
        self.paused_text.render(self.window)
        self.resume_button.draw_button(self.window)
        self.exit_game_button.draw_button(self.window)
        pygame.display.update()
        if self.resume_button.is_hovered() and self.resume_button.is_clicked():
            self.is_showed = False  