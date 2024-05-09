from settings import *


class Camera:
    def __init__(self, screen, pos=(0, 0)):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        size = self.screen_rect.size

        self.pos_basic = translate(pos)  # np.eye(3) + [0,2] = pos[0], [1,2] = pos[1]
        self.angle = 0
        self.center = (size[0] / 2, size[1] / 2)

    def get_basic(self):
        return self.pos_basic

    def move_to(self, pos: tuple):
        self.pos_basic[:2, 2] = translate(pos)[:2, 2]

    def move(self, pos: tuple):
        self.pos_basic[:2, 2] += translate(pos)[:2, 2]  # к текущей позиции прибавляется перемещение на pos единиц

    def rotate(self, angle: int):
        self.pos_basic = self.pos_basic @ rotate_z(angle)

    def update(self, target: Object):
        self.pos_basic[:2, 2] = target.get_basic()[:2, 2]
