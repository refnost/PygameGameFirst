from settings import *
import pygame
import numpy as np


class MapOld:
    def __init__(self, screen):
        self.screen = screen
        self.image = load_asset("assets/test_map.bmp")
        self.rect = self.image.get_rect()
        # self.scr_rect = self.scr.get_rect()

        # для линейки
        self.font = pygame.font.SysFont('Arial', 10, bold=True)
        # pygame.font.Font('C:\\Windows\\Fonts\\HOAMAI1T.ttf', 30)

        self.text, self.text_rect = [], []
        k = 0
        for i in np.arange(0, self.rect.height, 25):
            self.text.append(self.font.render(str(i), True, pygame.Color('white')))
            self.text_rect.append(self.text[k].get_rect())
            self.text_rect[k].centerx = 15
            self.text_rect[k].centery = i
            k += 1
        self.n = k

    # def update(self):
    #     self.rect.center = self.pos_basic[:2, 2].copy()
    #     self.image = pygame.transform.rotate(self.src_image, self.angle)
    #     self.rect = self.image.get_rect()
    #     self.rect.center = self.pos_basic[:2, 2].copy()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for i in range(self.n):
            self.screen.blit(self.text[i], self.text_rect[i])
