#from pygame.tiles_game.settings import WHITE
import pygame as pg
import random, sys
from os import path
from settings import *
from sprites import *
from tile_map import *

class Game:
    def __init__(self):   
        #initialaize game wndw, etc
        pg.init()
        pg.mixer.init()
        self.screen=pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock =pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.load_data()
    
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder =path.join(game_folder, 'img')
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.player_img = pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()
    
    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'P': 
                    self.player=Player(self,col,row)
            self.camera = Camera(self.map.width, self.map.height)        
                

    
    def run(self):
        #game loop
        
        self.playing=True
        while self.playing:
            self.dt= self.clock.tick(FPS) /1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()   
        sys.exit()   

    def update(self):
        #game loop update
        self.all_sprites.update()
        self.camera.update(self.player)  # track player,( can be any other sprite obj))

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen,LIGHTGRAY,(x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen,LIGHTGRAY,(0,y),(WIDTH,y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #pg.draw.rect(self.screen,WHITE,self.player.hit_rect,2)
        pg.display.flip() 

    def events(self):
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.quit()


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

#create the game object
g=Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()