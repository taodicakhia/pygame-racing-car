import pygame
import math

class Car:
    def __init__(self, car: pygame.Surface, max_vel, rotation_vel, start_pos=(0, 0), scale=0.5):
        self.car = pygame.transform.scale(car, (car.get_width() * scale, car.get_height() * scale))
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.speed = 0.3
        self.start_pos = start_pos
        self.x, self.y = self.start_pos

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
        self.move()
              
    def move_backward(self):
        self.vel = max(self.vel - self.speed, -self.max_vel / 2)
        self.move()
               
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.speed, 0)
        self.move()

    def collide(self, mask, x=0, y=0, top=0, left=0):
        car_mask = pygame.mask.from_surface(self.car)
        offset = (int(self.x - x - left), int(self.y - y - top))
        position = mask.overlap(car_mask, offset)
        return position

    def bounce(self):
        self.vel = -self.vel
        self.move()

    def reset(self):
        self.x, self.y = self.start_pos
        self.angle = 0
        self.vel = 0
