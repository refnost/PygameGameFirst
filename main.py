import random
from settings import *
from objects import *
from functions import *
from camera import *
from interface import *


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

        self.interface = None
        self.create_interface("menu")

        self.objects = []
        self.selected_obj = 1
        # self.create_objects()

        self.states = {"game": True, "mouse": False, "menu": True, "start": False, "stop": False, "options": False}

    def create_interface(self, key):
        if key == "menu":
            self.interface = Menu(self.screen)
        elif key == "options":
            self.interface = MenuOptions(self.screen)

    def create_objects(self):
        self.objects.append(Map(self.screen))
        self.objects.append(Car(self.screen, (self.sett.scr_width / 2, self.sett.scr_height / 2)))
        self.objects.append(FriendCar(self.screen, (100, 45)))
        # self.objects.append(Target(self.screen, (random.randint(0, self.objects[0].size[0]),
        #                                          random.randint(0, self.objects[0].size[1]))))

    def target_collision(self):
        # self.objects[len(self.objects)]
        pass

    def start_gameplay(self):
        self.create_objects()
        self.states["menu"] = False
        self.interface = None

    def draw(self, states):
        if not self.states["menu"]:
            self.camera.update(self.objects[self.selected_obj])
        cam_vec = self.camera.center - self.camera.pos_basic[:2, 2]
        for obj in self.objects:
            obj.update()
            obj.draw(cam_vec)
        if self.interface:
            self.interface.update(states["mouse"])
            self.interface.draw(cam_vec)
        self.states["mouse"] = False

    def run(self):
        while self.states["game"]:
            self.states = check_events(self.states)                 # проверка нажатий и закрывания окна
            if self.states["stop"]:
                self.states.update({"start": False, "menu": True, "stop": False, "options": False})
                self.objects.clear()
                self.create_interface("menu")
            if self.states["menu"]:
                self.states.update(self.interface.get_states())     # получение состояний от нажатий на кнопки меню
            else:
                self.selected_obj = check_global_controls(self.selected_obj)
                check_controls(self.objects[self.selected_obj])
            if self.states["options"]:
                self.create_interface("options")
            if self.states["start"]:
                self.states["start"] = False
                self.start_gameplay()
            self.draw(self.states)
            self.clock.tick(self.sett.FPS)
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
        pygame.display.quit()


if __name__ == '__main__':
    g = Game()
    g.run()
