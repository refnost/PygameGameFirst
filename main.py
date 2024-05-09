import pygame
from settings import Settings
from objects import *
from functions import *
from camera import *
from interface import *
# from decimal import Decimal     # to correct inaccuracies like 0.1 + 0.1 + 0.1 == 0.30000000000000004


class Game:
    def __init__(self):
        pygame.init()
        self.sett = Settings()
        self.screen = pygame.display.set_mode((self.sett.scr_width, self.sett.scr_height))
        self.screen.fill(self.sett.bg_color)
        pygame.display.set_caption(self.sett.caption_name)
        self.clock = pygame.time.Clock()
        self.mouse_pos = (-1, -1)

        self.camera = Camera(self.screen, (self.sett.scr_width / 2, self.sett.scr_height / 2))

        self.interface = []     # можно ключ-значение, но пока что обычный массив
        self.create_interface()

        self.objects = []
        self.selected_obj = 1
        self.create_objects()

    def create_interface(self):
        self.interface.append(Menu(self.screen))

    def create_objects(self):
        self.objects.append(Map(self.screen))
        self.objects.append(Car(self.screen, (self.sett.scr_width / 2, self.sett.scr_height / 2)))
        self.objects.append(FriendCar(self.screen, (100, 45)))

    def draw(self):
        self.camera.update(self.objects[self.selected_obj])
        cam_vec = self.camera.center - self.camera.pos_basic[:2, 2]
        for obj in self.objects:
            obj.update()
            obj.draw(cam_vec)
        self.mouse_pos = check_mouse()
        for i in self.interface:
            i.update(self.mouse_pos)
            i.draw(cam_vec)

    def run(self):
        game = True
        while game:
            game = check_events()
            self.selected_obj = check_global_controls(self.selected_obj)
            check_controls(self.objects[self.selected_obj])
            self.draw()
            self.clock.tick(self.sett.FPS)
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
        pygame.display.quit()


if __name__ == '__main__':
    g = Game()
    g.run()

