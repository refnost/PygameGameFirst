import numpy as np
import pygame
from settings import *


class Map(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(Map, self).__init__(screen, pos)

        image = load_asset("assets/test_map.bmp")
        size = image.get_rect().size

        image = pygame.transform.scale(image, size)

        self.src_image = pygame.transform.rotate(image, 0)       # Для коректного поворота изображения

        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.center = self.pos_basic[:2, 2]

    def update(self):
        self.rect.center = self.pos_basic[:2, 2].copy()
        self.image = pygame.transform.rotate(self.src_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_basic[:2, 2].copy()

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Car(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(Car, self).__init__(screen, pos)

        image = load_asset("assets/car.png")
        size = image.get_rect().size

        image = pygame.transform.scale(image, size)

        self.src_image = pygame.transform.rotate(image, 0)       # Для коректного поворота изображения

        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.center = self.pos_basic[:2, 2]

        self.pos_rectVert = np.array([
            [-size[0]/2, -size[1]/2, 1],    # X.topleft     Y.topleft       1
            [size[0]/2, -size[1]/2, 1],     # X.topright    Y.topright      1
            [size[0]/2, size[1]/2, 1],      # X.bottomright Y.bottomright   1
            [-size[0]/2, size[1]/2, 1],     # X.bottomleft  Y.bottomleft    1
        ])
        self.pos_rectVert_orig = self.pos_rectVert.copy()

    def update(self):
        self.rect.center = self.pos_basic[:2, 2].copy()
        self.image = pygame.transform.rotate(self.src_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_basic[:2, 2].copy()

        for i in range(len(self.pos_rectVert)):
            vec = self.pos_basic @ self.pos_rectVert_orig[i]
            self.pos_rectVert[i, :] = np.array(vec)

    def draw(self):
        pygame.draw.polygon(self.screen, (0, 0, 200), self.pos_rectVert[:, 0:2])
        self.screen.blit(self.image, self.rect)


class FriendCar(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(FriendCar, self).__init__(screen, pos)

        size = (100, 45)

        self.screen_rect = self.screen.get_rect()

        self.pos_rectVert = np.array([
            # [-size[0]/2, -size[1]/2, 1],    # X.topleft     Y.topleft       1
            [-size[0] / 2, -size[1] / 2 + 6, 1],
            [-size[0] / 2 + 10, -size[1] / 2 + 6, 1],
            [-size[0] / 2 + 10, -size[1] / 2, 1],
            [-size[0] / 2 + 20, -size[1] / 2, 1],
            [-size[0] / 2 + 20, -size[1] / 2 + 6, 1],

            [size[0] / 2 - 30, -size[1] / 2 + 6, 1],
            [size[0] / 2 - 30, -size[1] / 2 + 4, 1],
            [size[0] / 2 - 34, -size[1] / 2 + 4, 1],
            [size[0] / 2 - 34, -size[1] / 2, 1],
            [size[0] / 2 - 20, -size[1] / 2, 1],
            [size[0] / 2 - 20, -size[1] / 2 + 4, 1],
            [size[0] / 2 - 24, -size[1] / 2 + 4, 1],
            [size[0] / 2 - 24, -size[1] / 2 + 10, 1],
            [size[0] / 2 - 8, -size[1] / 2 + 10, 1],
            [size[0] / 2 - 8, -size[1] / 2, 1],
            [size[0]/2, -size[1]/2, 1],     # X.topright    Y.topright      1

            [size[0]/2, size[1]/2, 1],      # X.bottomright Y.bottomright   1
            [size[0] / 2 - 8, size[1] / 2, 1],
            [size[0] / 2 - 8, size[1] / 2 - 10, 1],
            [size[0] / 2 - 24, size[1] / 2 - 10, 1],
            [size[0] / 2 - 24, size[1] / 2 - 4, 1],
            [size[0] / 2 - 20, size[1] / 2 - 4, 1],
            [size[0] / 2 - 20, size[1] / 2, 1],
            [size[0] / 2 - 34, size[1] / 2, 1],
            [size[0] / 2 - 34, size[1] / 2 - 4, 1],
            [size[0] / 2 - 30, size[1] / 2 - 4, 1],
            [size[0] / 2 - 30, size[1] / 2 - 6, 1],

            [-size[0] / 2 + 20, size[1] / 2 - 6, 1],
            [-size[0] / 2 + 20, size[1] / 2, 1],
            [-size[0] / 2 + 10, size[1] / 2, 1],
            [-size[0] / 2 + 10, size[1] / 2 - 6, 1],
            [-size[0] / 2, size[1] / 2 - 6, 1]
            # [-size[0]/2, size[1]/2, 1],     # X.bottomleft  Y.bottomleft    1
        ])
        self.pos_rectVert_orig = self.pos_rectVert.copy()

    def update(self):
        for i in range(len(self.pos_rectVert)):
            vec = self.pos_basic @ self.pos_rectVert_orig[i]
            self.pos_rectVert[i, :] = np.array(vec)

    def draw(self):
        pygame.draw.polygon(self.screen, (0, 0, 200), self.pos_rectVert[:, 0:2])


class Camera(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(Camera, self).__init__(screen, pos)
        self.screen_rect = self.screen.get_rect()

        size = self.screen_rect.size

        self.pos = np.array([*pos, 1.])
        self.vec_x = np.array([1., 0., 1.])
        self.vec_y = np.array([0., 1., 1.])

        self.pos_rectVert = np.array([
            [-size[0] / 2, size[1] / 2, 1]
        ])
        self.pos_rectVert_orig = self.pos_rectVert.copy()

    def view_matrix(self):
        return np.array([
            self.pos,
            [0., 1., 0.],
            [0., 0., 1.]
        ])

    # надо разобраться
    def update_vecs(self):
        self.vec_x = self.move((1, 1, 0))
        self.vec_y = self.move((1, 1, 0))

    # надо разобраться
    def camera_matrix(self):
        self.update_vecs()
        return self.translate_matrix() @ self.rotate_matrix()

    # надо разобраться
    def translate_matrix(self):
        x, y = self.pos
        return np.array([
            [1, 0, 0],
            [0, 1, 0],
            [-x, -y, 1]
        ])

    # надо разобраться
    def rotate_matrix(self):
        rx, ry = self.vec_x
        ux, uy = self.vec_y
        return np.array([
            [rx, ux, 0],
            [ry, uy, 0],
            [0, 0, 1]
        ])

    def update(self):
        for i in range(len(self.pos_rectVert)):
            vec = self.pos_basic @ self.pos_rectVert_orig[i]
            self.pos_rectVert[i, :] = np.array(vec)

    def draw(self):
        pass