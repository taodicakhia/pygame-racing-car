import pygame
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
        center_blit = self.get_center_pos_of_window(window) if center is True else (0, 0)
        window.blit(self.get_image_surface(), center_blit)

    def show_image_with_position(self, window: pygame.Surface, position=(0, 0)):
        window.blit(self.get_image_surface(), position)

    def get_center_pos_of_window(self, window: pygame.Surface):
        return self.get_image_surface().get_rect(center = window.get_rect().center)

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
        self.speed = 0.14
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

pygame.init()

def move_car(car: Car):
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_a]:
        car.rotate(left=True)
    if keys[pygame.K_d]:
        car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        car.move_forward()
    elif keys[pygame.K_s]:
        moved = True
        car.move_backward()

    if not moved:
        car.reduce_speed()



def gameloop():
    window = Window(pygame.display.set_mode((1550, 800)))
    # Config game
    FPS = 60

    # Load image
    GRASS = Image(pygame.image.load("images/grass.jpg"))
    GRASS.scale((window.width, window.height))
    TRACK = Image(pygame.image.load("images/track.png"))
    TRACK.scale((window.height, window.height))
    TRACK_BORDER = Image(pygame.image.load("images/track-border.png"))
    TRACK_BORDER.scale((window.height, window.height))
    TRACK_CENTER_POS = TRACK.get_center_pos_of_window(window.window)
    TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER.get_image_surface())

    FINISH = Image(pygame.image.load("images/finish.png"))
    FINISH.scale((FINISH.width * 0.75, FINISH.height * 0.75))
    FINISH_MASK = pygame.mask.from_surface(FINISH.image)
    FINISH_POSITION = (TRACK_CENTER_POS.x + 137, TRACK_CENTER_POS.y + 230)

    # Load car image
    RED_CAR = Car(pygame.image.load("images/red-car.png"), 2.2, 2, (TRACK_CENTER_POS.x + 160, TRACK_CENTER_POS.y + 190))

    pygame.display.set_caption('Racing game!')
    is_running = True
    clock = pygame.time.Clock()
    clock.tick(FPS)

    while is_running:
        GRASS.show_image(window.window)
        TRACK.show_image(window.window, center=True)
        FINISH.show_image_with_position(window.window, position=FINISH_POSITION)
        RED_CAR.draw(window.window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break

        pygame.display.update()
        move_car(RED_CAR)

        if RED_CAR.collide(TRACK_BORDER_MASK, -3, -3, TRACK_CENTER_POS.y, TRACK_CENTER_POS.x):
            RED_CAR.bounce()
        
        # Create breakpoint


        finish_poi_collide = RED_CAR.collide(FINISH_MASK, *FINISH_POSITION)
        if finish_poi_collide != None:
            if finish_poi_collide[1] == 0:
                RED_CAR.bounce()
            else:
                RED_CAR.reset()
                print("finish")


    pygame.quit()


if __name__ == '__main__':
    gameloop()