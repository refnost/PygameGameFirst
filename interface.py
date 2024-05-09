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
        self.buttons.append(MyButton(self.screen, start_game_b, (screen[0] / 2, screen[1] / 2 - 70), 3, "start"))
        self.buttons.append(MyButton(self.screen, exit_game_b, (screen[0] / 2, screen[1] / 2), 3, "options"))
        self.buttons.append(MyButton(self.screen, options_b, (screen[0] / 2, screen[1] / 2 + 70), 3, "exit"))

    def update(self, mouse_pos):
        for button in self.buttons:
            button.check_col(mouse_pos)
            button.update()

    def draw(self, cam_vec):
        for button in self.buttons:
            button.draw(cam_vec)
