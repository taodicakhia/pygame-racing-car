import pygame
from objects.car import Car
from objects.elements.image import Image
from states.state import State

class Game(State):
    def __init__(self, game):
        super().__init__(game)
        self.load_images()
        self.scale_images()
        self.load_masks()
        self.load_breakpoints()
        self.load_cars()

    def render(self):
        self.draw_object()
        self.move_car(self.RED_CAR)
        self.check_collide_track()
        self.check_collide_breakpoint()
        self.check_collide_finish()

    def draw_object(self):
        self.GRASS.show_image(self.main)
        self.TRACK.show_image(self.main, center=True)
        self.FINISH.show_image_with_position(self.main, position=self.FINISH_POSITION)
        self.BREAKPOINT_1.show_image_with_position(self.main, self.BREAKPOINT_1_POS)
        self.BREAKPOINT_2.show_image_with_position(self.main, self.BREAKPOINT_2_POS)
        self.BREAKPOINT_3.show_image_with_position(self.main, self.BREAKPOINT_3_POS)
        self.BREAKPOINT_4.show_image_with_position(self.main, self.BREAKPOINT_4_POS)
        self.RED_CAR.draw(self.main)
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
        if self.RED_CAR.collide(self.TRACK_BORDER_MASK, -6, -6, self.TRACK_CENTER_POS.y, self.TRACK_CENTER_POS.x):
            self.RED_CAR.bounce()
        
    def check_collide_breakpoint(self):
        BREAKPOINT_1_POS_COLLIDE = self.RED_CAR.collide(self.BREAKPOINT_1_MASK, *self.BREAKPOINT_1_POS)
        if BREAKPOINT_1_POS_COLLIDE:
            print("Breakpoint 1")

    def check_collide_finish(self):
        finish_poi_collide = self.RED_CAR.collide(self.FINISH_MASK, *self.FINISH_POSITION)
        if finish_poi_collide != None:
            if finish_poi_collide[1] == 0:
                self.RED_CAR.bounce()
            else:
                self.RED_CAR.reset()
                print("finish")

    def load_images(self):
        self.GRASS = Image(pygame.image.load("images/grass.jpg"))
        self.TRACK = Image(pygame.image.load("images/track.png"))
        self.TRACK_BORDER = Image(pygame.image.load("images/track-border.png"))
        self.FINISH = Image(pygame.image.load("images/finish.png"))

    def scale_images(self):
        self.GRASS.scale((self.main.width_window, self.main.height_window))
        self.TRACK.scale((self.main.height_window, self.main.height_window))
        self.TRACK_BORDER.scale((self.main.height_window, self.main.height_window))
        self.FINISH.scale((self.FINISH.width * 0.75, self.FINISH.height * 0.75))

    def load_masks(self):
        self.TRACK_BORDER_MASK = pygame.mask.from_surface(self.TRACK_BORDER.image)
        self.FINISH_MASK = pygame.mask.from_surface(self.FINISH.image)
        self.TRACK_CENTER_POS = self.TRACK.get_center_pos_of_window(self.main.window)
        self.FINISH_POSITION = (self.TRACK_CENTER_POS.x + 145, self.TRACK_CENTER_POS.y + 230)

    def load_breakpoints(self):
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

        self.BREAKPOINT_1_POS = (495, 600)
        self.BREAKPOINT_2_POS = (975, 715)
        self.BREAKPOINT_3_POS = (700, 290)
        self.BREAKPOINT_4_POS = (575, 220)

    def load_cars(self):
        self.RED_CAR = Car(pygame.image.load("images/red-car.png"), 2.2, 2, (self.TRACK_CENTER_POS.x + 160, self.TRACK_CENTER_POS.y + 190))
