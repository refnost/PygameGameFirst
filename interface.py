import numpy as np
import pygame
from settings import *


class Menu:
    def __init__(self, screen, pos=(0, 0)):
        # origin in (0, 0)
        self.screen = screen
        self.pos_basic = translate(pos)
        self.angle = 0
        self.scale_param = 1
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        screen = self.screen.get_rect().size
        self.buttons.append(MyButton(self.screen, (screen[0] / 2, screen[1] / 2 - 70), 1, "button"))
        self.buttons.append(MyButton(self.screen, (screen[0] / 2, screen[1] / 2), 2, "button2"))
        self.buttons.append(MyButton(self.screen, (screen[0] / 2, screen[1] / 2 + 70), 3, "exit"))

    def update(self):
        for button in self.buttons:
            button.update()

    def draw(self, cam_vec):
        for button in self.buttons:
            button.draw(cam_vec)
