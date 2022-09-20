from trace import Trace
import pygame
import time
import math

class Image:
    def __init__(self, image: pygame.Surface):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.size = self.width, self.height

    def scale(self, size):
        self.width, self.height = size
        self.size = size

    def get_image_surface(self):
        return pygame.transform.scale(self.image, self.size)

    def show_image(self, window: pygame.Surface, center=False):
        window.blit(self.get_image_surface(), ((window.get_width() - self.width) / 2, 0) if center is True else (0, 0))

class Window:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()

    def update(self, size):
        self.window = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)

# Car class
class Car:
    def __init__(self, car: pygame.Surface, max_vel, rotation_vel, start_pos=(0, 0), scale=0.4):
        self.car = pygame.transform.scale(car, (car.get_width() * scale, car.get_height() * scale))
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.speed = 0.1
        self.x, self.y = start_pos

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        if right:
            self.angle -= self.rotation_vel
        
    def show_rotated_centre(self, window, image, topleft, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
        window.blit(rotated_image, new_rect.topleft)

    def draw(self, window):
        self.show_rotated_centre(window, self.car, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.speed, self.max_vel)
        self.move(forward=True)

    def move_backward(self):
        self.vel = min(self.vel + self.speed, self.max_vel)
        self.move(backward=True)

    def move(self, forward=False, backward=False):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        if forward:
            self.y -= vertical
            self.x -= horizontal
        if backward:
            self.y += vertical
            self.x += horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.speed / 2, 0)
        self.move()


pygame.init()

# Config game
FPS = 60

# Load image
GRASS = Image(pygame.image.load("images/grass.jpg"))
TRACK = Image(pygame.image.load("images/track.png"))

# Load car image
RED_CAR = Car(pygame.image.load("images/red-car.png"), 4, 4, (400, 300))


def gameloop():
    pygame.display.set_caption('Racing game!')
    is_running = True
    clock = pygame.time.Clock()
    clock.tick(FPS)
    window = Window(pygame.display.set_mode((700, 700), pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF))

    GRASS.scale((window.width, window.height))

    while is_running:
        GRASS.show_image(window.window)
        TRACK.scale((window.height, window.height))
        TRACK.show_image(window.window, center=True)
        RED_CAR.draw(window.window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            
            if event.type == pygame.VIDEORESIZE:
                window.update(event.dict['size'])
                GRASS.scale(event.dict['size'])
        
        pygame.display.update()

        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_a]:
            RED_CAR.rotate(left=True)
        if keys[pygame.K_d]:
            RED_CAR.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            RED_CAR.move_forward()
        if keys[pygame.K_s]:
            moved = True
            RED_CAR.move_backward()

        if not moved:
            RED_CAR.reduce_speed()

    pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    gameloop()