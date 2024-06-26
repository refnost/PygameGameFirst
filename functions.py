import math
from settings import *


def check_events(s):
    states = s
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            states["game"] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            states["mouse"] = True
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            states["stop"] = True
    return states


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
    forward_step = 4
    angle_step = 2
    scale_step = 0.1
    forward = False
    back = False
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
        forward = True
    if keys[pygame.K_s]:
        surf.move((-forward_step * cos_a, forward_step * sin_a, 0))     # точки и картинки
        back = True
    if forward:
        if keys[pygame.K_d]:
            surf.angle = (surf.angle - angle_step) % 360    # картинки
            surf.rotate(-angle_step)                        # точки
        if keys[pygame.K_a]:
            surf.angle = (surf.angle + angle_step) % 360  # картинки
            surf.rotate(angle_step)  # точки
    elif back:
        if keys[pygame.K_d]:
            surf.angle = (surf.angle + angle_step) % 360  # картинки
            surf.rotate(angle_step)  # точки
        if keys[pygame.K_a]:
            surf.angle = (surf.angle - angle_step) % 360  # картинки
            surf.rotate(-angle_step)  # точки
    forward = False
    back = True
