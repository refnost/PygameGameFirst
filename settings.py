import numpy as np
from math import *

class Settings:
    def __init__(self):
        self.scr_width = 500
        self.scr_height = 500
        self.bg_color = (0, 150, 255)
        self.caption_name = "Кошки мышки"
        self.FPS = 60


class Object:
    def __init__(self, name):
        self.name = name
        self.position = np.eye(3)

    def update(self):
        pass

    def rotate(self, angle: int):
        pass

    def draw(self):
        pass

    def translate(self, pos: tuple):
        pass

    def translate_to(self, pos: tuple):
        pass


def rot_x_y(point: np.array, a: int) -> np.array:
    x = point[0] * cos(a) - point[1] * sin(a)
    y = point[0] * sin(a) + point[1] * cos(a)
    return np.array([x, y])


def rotate_z(a: int) -> np.array:
    return np.array([
        [cos(a * (pi / 180)), sin(a * (pi / 180)), 0],
        [-sin(a * (pi / 180)), cos(a * (pi / 180)), 0],
        [0, 0, 1]
    ])


def scale(n) -> np.array:
    return np.array([
        [n, 0, 0],
        [0, n, 0],
        [0, 0, 1]
    ])


def translate(pos: np.array) -> np.array:
    return np.array([
        [1, 0, pos[0]],
        [0, 1, pos[1]],
        [0, 0, 1]
    ])


def mat_center(vec: np.array) -> np.array:
    x = sum(vec[:, 0]) / len(vec)
    y = sum(vec[:, 1]) / len(vec)
    return np.array([x, y, 1])
