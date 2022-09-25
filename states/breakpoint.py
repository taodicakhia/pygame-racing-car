from objects.elements.button import Button
from objects.elements.image import Image
from objects.elements.image_rect import ImageRect
from states.state import State
import pygame

class AnswerRect(ImageRect):
    def __init__(self, label: str, image: pygame.Surface, x, y, width, height, color=(255, 255, 255, 255), border_radius=0):
        super().__init__(image, x, y, width, height, color, border_radius)
        self.label = label
        
    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] == 1


class Breakpoint(State):
    def __init__(self, game, question, answer_A, answer_B, answer_C, answer_D, answer):
        super().__init__(game)
        self.is_answered = False
        self.question = ImageRect(pygame.image.load(question), 186, 120, 1100, 200, border_radius=5)
        self.answers = [AnswerRect('A', pygame.image.load(answer_A), 186, 420, 486, 120, border_radius=5), AnswerRect('B', pygame.image.load(answer_B), 800, 420, 486, 120, border_radius=5), AnswerRect('C', pygame.image.load(answer_C), 186, 580, 486, 120, border_radius=5), AnswerRect('D', pygame.image.load(answer_D), 800, 580, 486, 120, border_radius=5)]
        self.answer = answer
        self.is_answered = False
        self.is_answered_right = False
        self.run_continue = Button("Tiếp tục", 1000, 720, 400, 80, btn_color=(255, 128, 128), hovered_btn_color=(255, 102, 102), border_radius=6)
        self.reset = Button("Về màn hình chính", 1000, 720, 400, 80, btn_color=(255, 128, 128), hovered_btn_color=(255, 102, 102), border_radius=6)
        self.load_images()
        self.scale_images()
        
    def render(self):
        self.GRASS.show_image(self.main.window)
        self.draw_breakpoint()
        self.check_answer()
        if self.is_answered:
            if self.is_answered_right:
                self.run_continue.draw_button(self.main.window)
                if self.run_continue.is_hovered() and self.run_continue.is_clicked():
                    self.exit_state()
            else:
                self.reset.draw_button(self.main.window)
                if self.run_continue.is_hovered() and self.run_continue.is_clicked():
                    del self.main.state_stack[-1]
                    self.exit_state()
        pygame.display.flip()
    
    def load_images(self):
        self.GRASS = Image(pygame.image.load("images/grass.jpg"))
        self.YELLOW_CAR = Image(pygame.image.load("images/yellow-car.png"))
        
    def scale_images(self):
        self.GRASS.scale((self.main.width_window, self.main.height_window))
        self.question.scale_image((self.question.image.get_width() * 0.65, self.question.image.get_height() * 0.65))
        for item in self.answers:
            item.scale_image((item.image.get_width() * 0.65, item.image.get_height() * 0.65))
        
    def draw_breakpoint(self):
        # Draw question
        self.question.draw(self.main.window)
        # Draw answer
        for item in self.answers:
            item.draw(self.main.window)
    
    def check_answer(self):
        for item in self.answers:
            if item.is_hovered() and item.is_clicked() and not self.is_answered:
                if item.label == self.answer:
                    item.color = (120, 255, 120)
                    self.is_answered_right = True
                else:
                    item.color = (255, 128, 128)
                    self.is_answered_right = False
                self.is_answered = True