import pygame as pg
import random, sys
from settings import *
from sprites import *

class Game:
    def __init__(self):   
        #initialaize game wndw, etc
        pg.init()
        pg.mixer.init()
        self.screen=pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock =pg.time.Clock()
        self.load_data()
    
    def load_data(self):
        pass

    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        
    
    def run(self):
        #game loop
        
        self.playing=True
        while self.playing:
            self.clock.tick(FPS) /1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()   
        sys.exit()   

    def update(self):
        #game loop update
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen,LIGHTGRAY,(x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen,LIGHTGRAY,(0,y),(WIDTH,y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip() 

    def events(self):
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
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
    pg.show_go_screen()
