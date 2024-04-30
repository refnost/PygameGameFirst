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
        surf.movement((forward_step, -forward_step, 0), angle_step)
    if keys[pygame.K_q]:
        surf.movement((-forward_step, forward_step, 0), -angle_step)
    if keys[pygame.K_r]:
        surf.translate((150, 150, 0))
    if keys[pygame.K_w]:
        # surf.x += forward_step * cos_a
        # surf.y -= forward_step * sin_a
        # surf.translate((forward_step * cos_a, -forward_step * sin_a, 0))
        surf.translate_pos((forward_step * cos_a, forward_step * sin_a, 0))
        print(f"cos = {forward_step * cos_a}, sin = {forward_step * sin_a}")
    if keys[pygame.K_s]:
        # surf.x -= forward_step * cos_a
        # surf.y += forward_step * sin_a
        # surf.translate((-forward_step * cos_a, forward_step * sin_a, 0))
        surf.translate_pos((forward_step * cos_a, forward_step * sin_a, 0))
        print(f"cos = {forward_step * cos_a}, sin = {forward_step * sin_a}")
    if keys[pygame.K_d]:
        surf.angle = (surf.angle - angle_step) % 360
        surf.rotate_surf_angle(-angle_step)
    if keys[pygame.K_a]:
        surf.angle = (surf.angle + angle_step) % 360
        surf.rotate_surf_angle(angle_step)
