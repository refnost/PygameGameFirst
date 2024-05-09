import pygame
import math
from settings import *


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            return pygame.mouse.get_pos()
    return True


def check_mouse() -> tuple:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return pygame.mouse.get_pos()
    return -1, -1


def check_global_controls(num: int) -> int:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_PLUS]:
        pass
    if keys[pygame.K_KP_MINUS]:
        pass
    if keys[pygame.K_KP_1]:
        num = 1
    if keys[pygame.K_KP_2]:
        num = 2
    return num


def check_controls(surf: Object):
    forward_step = 1
    angle_step = 1
    scale_step = 0.1
    cos_a = math.cos(surf.angle * (math.pi / 180))      # переход в радианы
    sin_a = math.sin(surf.angle * (math.pi / 180))      # переход в радианы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        surf.scale_param += scale_step          # картинки
        surf.scaling(1 + scale_step)            # точки
    if keys[pygame.K_q]:
        surf.scale_param = abs(surf.scale_param - scale_step)           # картинки
        surf.scaling(abs(1 - scale_step))                               # точки
    if keys[pygame.K_r]:
        surf.move_to((0, 0, 0))
        surf.rotate(-surf.angle)
        surf.angle = 0
    if keys[pygame.K_w]:
        surf.move((forward_step * cos_a, -forward_step * sin_a, 0))     # точки и картинки
    if keys[pygame.K_s]:
        surf.move((-forward_step * cos_a, forward_step * sin_a, 0))     # точки и картинки
    if keys[pygame.K_d]:
        surf.angle = (surf.angle - angle_step) % 360    # картинки
        surf.rotate(-angle_step)                        # точки
    if keys[pygame.K_a]:
        surf.angle = (surf.angle + angle_step) % 360    # картинки
        surf.rotate(angle_step)                         # точки
