import pygame
from settings import Settings
# from map import Map
from objects import *
from functions import *
from camera import *

# from decimal import Decimal     # to correct inaccuracies like 0.1 + 0.1 + 0.1 == 0.30000000000000004

# from camera import Camera
# камера и машина это два объектая которые независимо
# друг от друга будут перемещаться по карте.
# камера меньше карты, можно отрисовывать не всю карту а по чанкам.
# при удерживании кнопки движения, чем больше подряд идет кнопка движения,
# тем быстрее движение


class Game:
    def __init__(self):
        pygame.init()
        self.sett = Settings()
        self.screen = pygame.display.set_mode((self.sett.scr_width, self.sett.scr_height))
        self.screen.fill(self.sett.bg_color)
        pygame.display.set_caption(self.sett.caption_name)
        self.clock = pygame.time.Clock()

        self.camera = Camera(self.screen)
        self.objects = []
        self.selected_obj = 1
        self.create_objects()

    def create_objects(self):
        # self.map = Map(self.screen)
        self.objects.append(Map(self.screen))
        self.objects.append(Car(self.screen, (self.sett.scr_width / 2, self.sett.scr_height / 2)))
        self.objects.append(FriendCar(self.screen, (100, 45)))

    def draw(self):
        # self.map.draw()
        for obj in self.objects:
            obj.update()
            obj.draw()

    def run(self):
        game = True
        while game:
            game = check_events()       # from functions
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

