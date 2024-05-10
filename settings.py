import numpy as np
from math import *
import pygame
from abc import ABCMeta, abstractmethod


class Settings:
    def __init__(self):
        self.scr_width = 500
        self.scr_height = 500
        self.bg_color = (0, 150, 255)
        self.caption_name = "Some of game"
        self.FPS = 60


class Object:
    def __init__(self, surf: pygame.Surface, pos: tuple = (0, 0)):
        self.surf = surf
        self.pos_basic = translate(pos)                 # np.eye(3) + [0,2] = pos[0], [1,2] = pos[1]
        # масштаб, поворот (и скос) для точек и позиция для точек и картинок
        self.angle = 0              # угол для картинок
        self.scale_param = 1        # масштаб для картинок

    def get_basic(self):
        return self.pos_basic

    def move_to(self, pos: tuple):
        self.pos_basic[:2, 2] = translate(pos)[:2, 2]

    def move(self, pos: tuple):
        self.pos_basic[:2, 2] += translate(pos)[:2, 2]  # к текущей позиции прибавляется перемещение на pos единиц
        # self.pos_basic = self.pos_basic @ translate(pos)    # Надо сделать нормальной мат операцией

    def rotate(self, angle: int):
        self.pos_basic = self.pos_basic @ rotate_z(angle)

    def scaling(self, s: float):
        self.pos_basic = self.pos_basic @ scale(s)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, vector):
        pass


class MyButton(Object):
    def __init__(self, surf: pygame.Surface, func, pos: tuple = (0, 0), scaling: int = 5,  text: str = ""):
        super(MyButton, self).__init__(surf, pos)
        self.function = func
        self.clicked = False

        self.size = (np.array(self.surf.get_rect().size) / 10) * scaling
        self.size[1] *= 0.3      # height
        size = self.size
        bevel = 7
        self.pos_rectVert = np.array([
            # [-size[0]/2, -size[1]/2, 1],    # X.topleft     Y.topleft       1
            [-size[0] / 2, -size[1] / 2 + bevel, 1],
            [-size[0] / 2 + bevel, -size[1] / 2, 1],

            # [size[0] / 2, -size[1] / 2, 1],  # X.topright    Y.topright      1
            [size[0] / 2 - bevel, -size[1] / 2, 1],
            [size[0] / 2, -size[1] / 2 + bevel, 1],

            # [size[0] / 2, size[1] / 2, 1],  # X.bottomright Y.bottomright   1
            [size[0] / 2, size[1] / 2 - bevel, 1],
            [size[0] / 2 - bevel, size[1] / 2, 1],

            # [-size[0]/2, size[1]/2, 1],     # X.bottomleft  Y.bottomleft    1
            [-size[0] / 2 + bevel, size[1] / 2, 1],
            [-size[0] / 2, size[1] / 2 - bevel, 1]
        ])
        self.pos_rectVert_orig = self.pos_rectVert.copy()

        self.text = MyText(self.surf, text, pos, scaling)

    def check_col(self, m_pos) -> dict:
        if m_pos != (-1, -1):
            x, y = self.pos_basic[0, 2] - self.size[0] / 2, self.pos_basic[1, 2] - self.size[1] / 2
            if x <= m_pos[0] <= x + self.size[0] and y <= m_pos[1] <= y + self.size[1]:
                self.scaling(1.1)
                return self.function()
        return {}

    def update(self):
        for i in range(len(self.pos_rectVert)):
            vec = self.pos_basic @ self.pos_rectVert_orig[i]
            self.pos_rectVert[i, :] = np.array(vec)
        self.text.update_pos(self.pos_basic[:2, 2])

    def draw(self, cam_vec):
        pygame.draw.polygon(self.surf, (100, 0, 200), self.pos_rectVert[:, 0:2])
        self.text.draw()


class MyText:
    def __init__(self, surf: pygame.Surface, text: str = "Empty", pos: tuple = (0, 0), scaling: int = 5,
                 color: tuple = (255, 255, 255)):
        self.surf = surf
        self.text = text
        text_size = scaling * 10
        self.font = pygame.font.SysFont('Arial', text_size, bold=True)
        self.text_image = self.font.render(text, True, color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = pos

    def update_pos(self, pos):
        self.text_rect.center = pos

    def draw(self):
        self.surf.blit(self.text_image, self.text_rect)


class InterfaceButtons:
    def __init__(self, screen, pos=(0, 0)):
        # origin in (0, 0)
        self.screen = screen
        self.pos_basic = translate(pos)
        self.angle = 0
        self.scale_param = 1
        self.buttons = []
        self.create_buttons()
        self.state = {}

    def update(self, click_mouse: bool):
        self.state = {}
        if click_mouse:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                state = button.check_col(pos)
                if state != {}:
                    self.state = state
                button.update()
        else:
            for button in self.buttons:
                button.update()

    def draw(self, cam_vec):
        self.screen.fill((0, 150, 255))
        for button in self.buttons:
            button.draw(cam_vec)

    def get_states(self):
        return self.state

    @abstractmethod
    def create_buttons(self):
        pass


def rot_x_y(point: np.array, a: int) -> np.array:
    x = point[0] * cos(a) - point[1] * sin(a)
    y = point[0] * sin(a) + point[1] * cos(a)
    return np.array([x, y])


def rotate_z(a: int) -> np.array:
    return np.array([
        [cos(a * (pi / 180)), sin(a * (pi / 180)), 0.],
        [-sin(a * (pi / 180)), cos(a * (pi / 180)), 0.],
        [0., 0., 1.]
    ])


def scale(n) -> np.array:
    return np.array([
        [n, 0., 0.],
        [0., n, 0.],
        [0., 0., 1.]
    ])


def translate(pos: np.array) -> np.array:
    return np.array([
        [1., 0., pos[0]],
        [0., 1., pos[1]],
        [0., 0., 1.]
    ])


def mat_center(vec: np.array) -> np.array:
    x = sum(vec[:, 0]) / len(vec)
    y = sum(vec[:, 1]) / len(vec)
    return np.array([x, y, 1])


def load_asset(path: str) -> pygame.Surface:
    image = None
    try:
        image = pygame.image.load(path)
    except FileNotFoundError:
        image = pygame.image.load("assets/error_stub.png")
    finally:
        return image


def start_game_b():
    print("Game started by button")
    return {"menu": False, "start": True}


def exit_game_b():
    print("Game exit by button")
    return {"game": False}


def options_b():
    print("Open options by button")
    return {"options": True}


def option1_b():
    print("Open option 1 by button")
    return {}


def option2_b():
    print("Open option 2 by button")
    return {}


def option3_b():
    print("Open option 3 by button")
    return {}
