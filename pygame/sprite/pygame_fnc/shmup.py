import pygame, sys
import random

from pygame.constants import K_LEFT, K_RIGHT



class Settings:
    def __init__(self):
        self.WIDTH = 360
        self.HEIGHT = 480
        self.FPS = 60

        self.WHITE = (255,255,255)
        self.BLACK =(0,0,0)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)

class Player(pygame.sprite.Sprite):
    
    # sprite for player
    def __init__(self,stt):
        pygame.sprite.Sprite.__init__(self)
        
        self.stt=stt
        self.image = pygame.Surface((50,40))
        self.image.fill(stt.GREEN)
        self.rect = self.image.get_rect() 
        self.rect.centerx = stt.WIDTH/2
        self.rect.bottom = stt.HEIGHT -10
        self.speedx = 0


    def update(self):
        # self.speedx=0
        # keystate = pygame.key.get_pressed()
        # #print(keystate)
        # if keystate[pygame.K_LEFT]:
        #     print('left')
        #     self.speedx = -5
        # if keystate[pygame.K_RIGHT]:
        #     print('right')
        #     self.speedx = 5
        
        self.rect.x += self.speedx
        #pass

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

    #game loop
    while game_is_running:
        clock.tick(stt.FPS)
        
        #input events
        player.speedx=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
            
            # elif event.type == pygame.KEYDOWN :
            #     if event.key ==pygame.K_LEFT:
            #         player.speedx -= 5
            #         print('left')
        
            #     if event.key ==pygame.K_RIGHT:
            #         player.speedx += 5  
            #         print('right')
            
            # elif event.type == pygame.KEYUP :
            #     if event.key ==pygame.K_LEFT:
            #         player.speedx = 0
            #         print('left')
        
            #     if event.key ==pygame.K_RIGHT:
            #         player.speedx = 0  
            #         print('right')
                
        all_sprites.update()
       
        screen.fill(stt.BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game()