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
    angle_step = 1# % 360
    cos_a = math.cos(surf.angle * (math.pi / 180))
    sin_a = math.sin(surf.angle * (math.pi / 180))
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
        surf.translate_pos((forward_step * cos_a, -forward_step * sin_a, 0))
    if keys[pygame.K_s]:
        # surf.x -= forward_step * cos_a
        # surf.y += forward_step * sin_a
        # surf.translate((-forward_step * cos_a, forward_step * sin_a, 0))
        surf.translate_pos((-forward_step * cos_a, forward_step * sin_a, 0))
    if keys[pygame.K_d]:
        surf.pre_angle = surf.angle
        surf.angle -= angle_step
        # surf.rotate_surf()
        surf.rotate_surf_angle(-angle_step)
        # surf.rotate_trans(-angle_step)
    if keys[pygame.K_a]:
        surf.pre_angle = surf.angle
        surf.angle += angle_step
        # surf.rotate_surf()
        surf.rotate_surf_angle(angle_step)
        # surf.rotate_trans(angle_step)
