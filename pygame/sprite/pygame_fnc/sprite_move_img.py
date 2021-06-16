import pygame, sys
import random
import os


class Settings:
    def __init__(self):
        self.WIDTH = 360
        self.HEIGHT = 480
        self.FPS = 30

        self.WHITE = (255,255,255)
        self.BLACK =(0,0,0)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)

        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, "img")


class Player(pygame.sprite.Sprite):
    
    # sprite for player
    def __init__(self,stt):
        pygame.sprite.Sprite.__init__(self)
        
        self.stt= stt
        self.image = pygame.image.load(os.path.join(stt.img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(stt.BLACK)
        self.rect = self.image.get_rect() 
        self.rect.center = (stt.WIDTH/2, stt.HEIGHT/2)
    
    def update(self):
        
        self.rect.x +=5
        if self.rect.left > self.stt.WIDTH:
            self.rect.right = 0


def game():

    
    pygame.init()
    #pygame.mixer.init()
    stt=Settings()
    screen = pygame.display.set_mode((stt.WIDTH, stt.HEIGHT))
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = Player(stt)
    all_sprites.add(player)
    
    game_is_running = True
    while game_is_running:
        clock.tick(stt.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
                
        all_sprites.update()
        screen.fill(stt.BLUE)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game()