import numpy as np
import pygame
from settings import *


class Car(Object):
    def __init__(self, screen, pos=(0, 0)):
        super(Car, self).__init__("darifto")
        self.screen = screen
        image = pygame.image.load("car.png")
        size = (30, 55)
        image = pygame.transform.scale(image, size)
        self.src_image = pygame.transform.rotate(image, 0)
        self.image = self.src_image

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # self.rect.centerx = self.scr_rect.centerx
        # self.rect.centery = self.scr_rect.centery
        self.rect.center = pos
        self.x, self.y = self.rect.centerx, self.rect.centery
        self.pos_rectVert = np.array([
            [-size[0]/2, -size[1]/2, 1],    # X.topleft     Y.topleft       1
            [size[0]/2, -size[1]/2, 1],     # X.topright    Y.topright      1
            [size[0]/2, size[1]/2, 1],      # X.bottomright Y.bottomright   1
            [-size[0]/2, size[1]/2, 1],     # X.bottomleft  Y.bottomleft    1
        ])
        self.pos_rectVert_orig = self.pos_rectVert.copy()

        self.pos_vec = np.array([pos[0], pos[1], 1])
        self.pos_basic = translate(pos)     # np.eye(3) + [0,2] = pos[0], [1,2] = pos[1]

        self.angle = 0

    def movement(self, speed: tuple, angle: int):
        self.pos_basic = np.eye(3) @ rotate_z(angle) @ translate(speed)
        for i in range(len(self.pos_rectVert)):
            vec = self.pos_rectVert_orig[i] @ self.pos_basic
            self.pos_rectVert[i, :] = np.array(vec)

    def translate(self, speed: tuple):
        print(self.pos_rectVert[0])
        for i in range(len(self.pos_rectVert)):
            vec = self.pos_rectVert_orig[i] + speed
            self.pos_rectVert[i, :] = np.array(vec)

    def translate_pos(self, pos: tuple):
        self.pos_basic = self.pos_basic @ translate(pos)
        print(self.pos_basic)

    def rotate_surf_angle(self, angle):
        self.pos_basic = self.pos_basic @ rotate_z(angle)

    def rotate_trans(self, angle):
        point = mat_center(self.pos_rectVert)
        self.pos_basic = self.pos_basic @ translate(-point) @ rotate_z(angle) @ translate(point) # ne robit
        # может не базисную хрень менять а буквально машину перемещать. HET

    def update(self):
        self.rect.center = self.pos_vec[0:2].copy()
        self.image = pygame.transform.rotate(self.src_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_vec[0:2].copy()

        for i in range(len(self.pos_rectVert)):
            vec = self.pos_basic @ self.pos_rectVert_orig[i]
            self.pos_rectVert[i, :] = np.array(vec)

    def draw(self):
        pygame.draw.polygon(self.screen, (0, 0, 200), self.pos_rectVert[:, 0:2])
        self.screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    # No using, just example.
    def __init__(self, pos=(0, 0), size=(200, 200)):
        super(Player, self).__init__()
        self.original_image = pygame.Surface(size)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 1 % 360  # Value will reapeat after 359. This prevents angle to overflow.
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.
