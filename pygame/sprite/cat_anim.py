
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), pygame.RESIZABLE)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
catImg = pygame.image.load('Images/cat.png') #125/79
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    ws=pygame.display.get_window_size()
    print(ws)
    if direction == 'right':
        catx += 5
        if catx >= ws[0]-125:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty >= ws[1]-79:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)