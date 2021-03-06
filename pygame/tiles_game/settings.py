import pygame as pg
vec =pg.math.Vector2

WIDTH = 1024
HEIGHT =768
FPS =60
TITLE = "Tilemap"
FONT_NAME='arial'

#define colors
WHITE =(255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)
YELLOW =(255,255,0)
LIGHTGRAY=(100,100,100)
DARKGRAY=(40,40,40)
BROWN =(106,55,5)
CYAN = (0,255,255)
BGCOLOR = BROWN


TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#wall image
WALL_IMG ='tileGreen_39.png'

#player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 350
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT= pg.Rect(0,0,35,35)
BARREL_OFFSET = vec(30,10)



#gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED=500
BULLET_LIFETIME=1000
BULLET_RATE =150
BULLET_DAMAGE=10
KICK_BACK =  200  #recul
GUN_SPREEAD = 5     #inaccuracy of the bullet
BULLET_DAMAGE=10

#mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS= [150,100,75,125]
MOB_HIT_RECT = pg.Rect(0,0,30,30)
MOB_HEALTH=100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS =50