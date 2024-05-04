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
    def __init__(self, screen, pos=(0, 0)):
        self.screen = screen
        self.pos_basic = translate(pos)                 # np.eye(3) + [0,2] = pos[0], [1,2] = pos[1]
        self.angle = 0

    def move_to(self, pos: tuple):
        self.pos_basic[:2, 2] = translate(pos)[:2, 2]

    def move(self, pos: tuple):
        self.pos_basic[:2, 2] += translate(pos)[:2, 2]  # к текущей позиции прибавляется перемещение на pos единиц
        # self.pos_basic = self.pos_basic @ translate(pos)    # Надо сделать нормальной мат операцией

    def rotate(self, angle: int):
        self.pos_basic = self.pos_basic @ rotate_z(angle)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
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
