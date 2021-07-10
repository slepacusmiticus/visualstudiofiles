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

    def draw(self):
        self.screen.fill(BGCOLOR)
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

    def show_gameover_screen(self):
        pass


g=Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()
pg.quit()
