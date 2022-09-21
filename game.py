import pygame
from objects.breakpoint import Breakpoint
from objects.car import Car
from objects.image import Image

class Game:
    def __init__(self):
        pygame.init()
        self.is_running, self.is_playing = True, False
        self.width_window, self.height_window = 1550, 800
        self.FPS = 60
        self.window = pygame.display.set_mode((self.width_window, self.height_window))
        self.GRASS = Image(pygame.image.load("images/grass.jpg"))
        self.TRACK = Image(pygame.image.load("images/track.png"))
        self.TRACK_BORDER = Image(pygame.image.load("images/track-border.png"))
        self.FINISH = Image(pygame.image.load("images/finish.png"))

        self.GRASS.scale((self.width_window, self.height_window))
        self.TRACK.scale((self.height_window, self.height_window))
        self.TRACK_BORDER.scale((self.height_window, self.height_window))
        self.FINISH.scale((self.FINISH.width * 0.75, self.FINISH.height * 0.75))

        self.TRACK_BORDER_MASK = pygame.mask.from_surface(self.TRACK_BORDER.image)
        self.FINISH_MASK = pygame.mask.from_surface(self.FINISH.image)
        # Position
        self.TRACK_CENTER_POS = self.TRACK.get_center_pos_of_window(self.window)
        self.FINISH_POSITION = (self.TRACK_CENTER_POS.x + 137, self.TRACK_CENTER_POS.y + 230)

        self.RED_CAR = Car(pygame.image.load("images/red-car.png"), 2.2, 2, (self.TRACK_CENTER_POS.x + 160, self.TRACK_CENTER_POS.y + 190))
        self.BREAKPOINT_1 = Image(pygame.image.load(f"images/point1.png"))
        self.BREAKPOINT_2 = Image(pygame.image.load(f"images/point2.png"))
        self.BREAKPOINT_3 = Image(pygame.image.load(f"images/point3.png"))
        self.BREAKPOINT_4 = Image(pygame.image.load(f"images/point4.png"))

        self.BREAKPOINT_1.scale((self.BREAKPOINT_1.width * 0.5, self.BREAKPOINT_1.height * 0.5))
        self.BREAKPOINT_2.scale((self.BREAKPOINT_2.width * 0.5, self.BREAKPOINT_2.height * 0.5))
        self.BREAKPOINT_3.scale((self.BREAKPOINT_3.width * 0.5, self.BREAKPOINT_3.height * 0.5))
        self.BREAKPOINT_4.scale((self.BREAKPOINT_4.width * 0.5, self.BREAKPOINT_4.height * 0.5))

        self.BREAKPOINT_1.rotate(223)
        self.BREAKPOINT_2.rotate(270)
        self.BREAKPOINT_4.rotate(180)

        self.BREAKPOINT_1_MASK = pygame.mask.from_surface(self.BREAKPOINT_1.image)
        self.BREAKPOINT_2_MASK = pygame.mask.from_surface(self.BREAKPOINT_2.image)
        self.BREAKPOINT_3_MASK = pygame.mask.from_surface(self.BREAKPOINT_3.image)
        self.BREAKPOINT_4_MASK = pygame.mask.from_surface(self.BREAKPOINT_4.image)

        self.BREAKPOINT_1_POS = (560, 600)
        self.BREAKPOINT_2_POS = (1002, 688)
        self.BREAKPOINT_3_POS = (740, 278)
        self.BREAKPOINT_4_POS = (620, 220)


    def game_loop(self):
        while self.is_playing:
            pygame.display.set_caption('Racing game!')
            clock = pygame.time.Clock()
            clock.tick(self.FPS)

            self.check_events()
            self.draw_object()
            self.move_car(self.RED_CAR)
            self.check_collide_track()
            self.check_collide_breakpoint()
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running, self.is_playing = False, False

    def draw_object(self):
        self.GRASS.show_image(self.window)
        self.TRACK.show_image(self.window, center=True)
        self.FINISH.show_image_with_position(self.window, position=self.FINISH_POSITION)
        self.BREAKPOINT_1.show_image_with_position(self.window, self.BREAKPOINT_1_POS)
        self.BREAKPOINT_2.show_image_with_position(self.window, self.BREAKPOINT_2_POS)
        self.BREAKPOINT_3.show_image_with_position(self.window, self.BREAKPOINT_3_POS)
        self.BREAKPOINT_4.show_image_with_position(self.window, self.BREAKPOINT_4_POS)
        self.RED_CAR.draw(self.window)
        pygame.display.update()

    def move_car(self, car: Car):
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

    def check_collide_track(self):
        if self.RED_CAR.collide(self.TRACK_BORDER_MASK, -3, -3, self.TRACK_CENTER_POS.y, self.TRACK_CENTER_POS.x):
            self.RED_CAR.bounce()
        
    def check_collide_breakpoint(self):
        BREAKPOINT_POS_COLLIDE = self.RED_CAR.collide(self.BREAKPOINT_1_MASK, *self.BREAKPOINT_1_POS)
        if BREAKPOINT_POS_COLLIDE:
            print("Breakpoint 1")

    def check_collide_finish(self):
        finish_poi_collide = self.RED_CAR.collide(self.FINISH_MASK, *self.FINISH_POSITION)
        if finish_poi_collide != None:
            if finish_poi_collide[1] == 0:
                self.RED_CAR.bounce()
            else:
                self.RED_CAR.reset()
                print("finish")
