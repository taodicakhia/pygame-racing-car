import pygame

class Breakpoint:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.run_qna = False

    def show_question(self):
        self.window.fill((255, 255, 255))
