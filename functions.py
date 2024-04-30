import pygame
import math
from settings import *
from car import Car


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def check_controls(surf: Car):
    forward_step = 1
    angle_step = 1
    cos_a = math.cos(surf.angle * (math.pi / 180))      # переход в радианы
    sin_a = math.sin(surf.angle * (math.pi / 180))      # переход в радианы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_PLUS]:
        pass
    if keys[pygame.K_KP_MINUS]:
        pass
    if keys[pygame.K_e]:
        surf.translate((forward_step * sin_a, -forward_step * cos_a, 0))
    if keys[pygame.K_q]:
        surf.translate((-forward_step * sin_a, forward_step * cos_a, 0))
    if keys[pygame.K_r]:
        surf.translate_to((0, 0, 0))
        surf.rotate(-surf.angle)
        surf.angle = 0
    if keys[pygame.K_w]:
        surf.translate((forward_step * cos_a, -forward_step * sin_a, 0))
    if keys[pygame.K_s]:
        surf.translate((-forward_step * cos_a, forward_step * sin_a, 0))
    if keys[pygame.K_d]:
        surf.angle = (surf.angle - angle_step) % 360
        surf.rotate(-angle_step)
    if keys[pygame.K_a]:
        surf.angle = (surf.angle + angle_step) % 360
        surf.rotate(angle_step)
