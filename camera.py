from settings import *


class Camera(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(Camera, self).__init__(screen, pos)
        self.screen_rect = self.screen.get_rect()

        size = self.screen_rect.size
        self.center = (-size[0] / 2, size[1] / 2)

    def update(self):
        pass

    def draw(self):
        pass


class CameraOld(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(CameraOld, self).__init__("camera")
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect.center = pos
        self.x, self.y = self.rect.centerx, self.rect.centery
        self.angle = 0
        self.rotation = False
        self.pos_vec = np.array([pos[0], pos[2], 1])
        self.pos_basic = np.eye(2)
        self.movement = np.eye(3)

    def rotate(self, angle: int):
        self.movement[0] = rot_x_y(self.movement[0], angle)
        self.movement[1] = rot_x_y(self.movement[1], angle)
        self.pos_vec = self.movement * self.pos_vec

    def rotate_surf(self):
        pass

    def update(self):
        # self.rect.center = (self.x, self.y)
        # rotation
        # self.rect = self.image.get_rect()
        # self.rect.center = (self.x, self.y)
        pass

    def draw(self):
        # self.screen.blit(self.image, self.rect)
        pass
