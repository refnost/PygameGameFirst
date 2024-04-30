import pygame
import numpy as np


class Map:
    def __init__(self, scr):
        self.scr = scr
        self.image = pygame.image.load("assets/test_map.bmp")
        self.rect = self.image.get_rect()
        # self.scr_rect = self.scr.get_rect()

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

    def draw(self):
        self.scr.blit(self.image, self.rect)
        for i in range(self.n):
            self.scr.blit(self.text[i], self.text_rect[i])

