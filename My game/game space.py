import pygame, control
import sys
from gun import Gun
from pygame.sprite import Group




def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космо-защитники")
    bg_color = (129, 32, 255)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    control.create_army(screen, inos)


    while True:
        control.events(screen, gun, bullets)
        gun.update_gun()
        control.update(bg_color, screen, gun, inos, bullets)
        control.update_bullets(bullets)
        control.update_inos(inos)

run()