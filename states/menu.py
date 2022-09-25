import pygame
from objects.elements.button import Button

from objects.elements.image import Image
from states.game import Game
from states.state import State


class Menu(State):
    def __init__(self, game):
        super().__init__(game)
        self.is_playing, self.is_setting = False, False
        self.BACKGROUND = Image(pygame.image.load("images/background.png"))
        self.BACKGROUND.scale((self.main.width_window, self.main.height_window))

    def render(self):
        self.main.window.fill((230, 230, 230))
        self.BACKGROUND.show_image(self.main.window)

        start_button = Button("Bắt đầu", 100, 700, 220, 80, btn_color=(120, 255, 120), hovered_btn_color=(46, 255, 46), border_radius=6)
        start_button.draw_button(self.main.window)
        
        quit_button = Button("Thoát", 1152, 700, 220, 80, btn_color=(255, 128, 128), hovered_btn_color=(255, 102, 102), text_color=(255, 255, 255), border_radius=6)
        quit_button.draw_button(self.main.window)
        
        # setting_button = Button("Settings", 636, 700, 220, 80, btn_color=(128, 191, 255), hovered_btn_color=(77, 166, 255), border_radius=6)
        # setting_button.draw_button(self.main.window)

        if start_button.is_hovered() and start_button.is_clicked():
            game = Game(self.main)
            self.main.state_stack.append(game)
            
        if quit_button.is_hovered() and quit_button.is_clicked():
            self.main.is_running = False

        pygame.display.update()
