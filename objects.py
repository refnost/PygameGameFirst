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

    def draw(self, camera):
        temptransform = self.rect.copy()
        self.rect.center += camera
        self.screen.blit(self.image, self.rect)
        self.rect = temptransform


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

    def draw(self, camera):
        pygame.draw.polygon(self.screen, (0, 0, 200), self.pos_rectVert[:, 0:2] + camera)

        temptransform = self.rect.copy()
        self.rect.center += camera
        self.screen.blit(self.image, self.rect)
        self.rect = temptransform


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

    def draw(self, camera):
        pygame.draw.polygon(self.screen, (0, 0, 200), self.pos_rectVert[:, 0:2] + camera)
