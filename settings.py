import numpy as np
from math import *
import pygame
from abc import ABCMeta, abstractmethod


class Settings:
    def __init__(self):
        self.scr_width = 500
        self.scr_height = 500
        self.bg_color = (0, 150, 255)
        self.caption_name = "Кошки мышки"
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
    def __init__(self, menu_surf: pygame.Surface, pos: tuple = (0, 0), scaling: int = 5,  text: str = ""):
        super(MyButton, self).__init__(menu_surf, pos)
        size = (np.array(self.surf.get_rect().size) / 10) * scaling
        size[1] *= 0.3      # height
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

        text_size = scaling * 10
        self.font = pygame.font.SysFont('Arial', text_size, bold=True)
        self.text_image = self.font.render(text, True, pygame.Color('white'))
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = pos

    def check_col(self):
        # size = self.get_rect()
        pass

    def update(self):
        for i in range(len(self.pos_rectVert)):
            vec = self.pos_basic @ self.pos_rectVert_orig[i]
            self.pos_rectVert[i, :] = np.array(vec)
        self.text_rect.center = self.pos_basic[:2, 2]

    def draw(self, cam_vec):
        pygame.draw.polygon(self.surf, (100, 0, 200), self.pos_rectVert[:, 0:2])
        self.surf.blit(self.text_image, self.text_rect)


class MyText:
    def __init__(self, surf: pygame.Surface, text: str = "Empty", pos: tuple = (0, 0), scaling: int = 5):
        self.surf = surf
        self.text = text
        text_size = scaling * 10
        self.font = pygame.font.SysFont('Arial', text_size, bold=True)
        self.text_image = self.font.render(text, True, pygame.Color('white'))
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = pos

    def set_text(self, text):
        self.text = text

    def update_pos(self, pos):
        self.text_rect.center = pos

    def draw(self, cam_vec: int = 0):
        if cam_vec:
            temp = self.text_rect.center
            self.text_rect.center += cam_vec
            self.surf.blit(self.text_image, self.text_rect)
            self.text_rect.center = temp
        else:
            self.surf.blit(self.text_image, self.text_rect)


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
