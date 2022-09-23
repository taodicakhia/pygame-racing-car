import pygame
class State:
    def __init__(self, main):
        self.main = main
        self.prev_state = None
    
    def render(self):
        pygame.display.set_caption('Racing game!')
        clock = pygame.time.Clock()
        clock.tick(self.main.FPS)
        
    def update(self, actions):
        pass
    
    def join_state(self):
        if len(self.main.state_stack) > 1:
            self.prev_state = self.main.state_stack[-1]
        self.main.state_stack.append(self)
        
    def exit_state(self):
        self.main.state_stack.pop()