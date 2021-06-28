import pygame as pygame
import random

from platformer_settings import *

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')
clock=pygame.time.Clock()

all_sprites =pygame.sprite.Group()

running = True
while running:
    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()