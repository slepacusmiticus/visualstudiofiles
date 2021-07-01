import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        

        pg.init()
        pg.mixer.init()
        self.screen=pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Platformer')
        self.clock =pg.time.Clock()
        self.running = True

    def new(self):
        #start a new game

        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()
    
    def run(self):
        #game loop
        
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        #game loop update
        self.all_sprites.update()

    def events(self):
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

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




