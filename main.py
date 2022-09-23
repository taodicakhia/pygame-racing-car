import pygame
from states.game import Game
from states.menu import Menu
from states.pause_game import Pause

class Main:
    def __init__(self):
        pygame.init()
        self.width_window, self.height_window = 1472, 828
        self.window = pygame.display.set_mode((self.width_window, self.height_window))
        self.is_running = True
        self.FPS = 60
        self.actions = {"settings" : False, "start" : False}
        self.state_stack = []
        self.load_states()
        
    def loop(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.render()
    
    def update(self):
        self.state_stack[-1].update(self.actions)    
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                
    def render(self):
        self.state_stack[-1].render()
        
    def load_states(self):
        self.main_menu = Menu(self)
        self.state_stack.append(self.main_menu)

if __name__ == '__main__':
    main = Main()
    main.loop()