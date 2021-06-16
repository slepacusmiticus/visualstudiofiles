
import pygame
# Loading and playing a sound effect:
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 2048) 

pygame.mixer.init()
soundObj = pygame.mixer.Sound('beep-01a.wav')

#soundObj.play()

import time

#time.sleep(1)

# Loading and playing background music:

pygame.mixer.music.load('remember.wav')

pygame.mixer.music.play(-1,0.0)
soundObj.play()#
time.sleep(10)
pygame.mixer.music.stop()
