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
        self.RED = (255,0,0)

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
        self.speedx=0
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        
        self.rect.x += self.speedx
        if self.rect.right > self.stt.WIDTH:
            self.rect.right = self.stt.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):

    def __init__(self,stt) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.stt=stt
        self.image = pygame.Surface((30,40))
        self.image.fill(stt.RED)
        self.rect = self.image.get_rect()
        self.rect.x=random.randrange(0,self.stt.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > self.stt.HEIGHT +10:
            self.rect.x=random.randrange(0,self.stt.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

def game():
        
    pygame.init()
    #pygame.mixer.init()
    stt=Settings()
    screen = pygame.display.set_mode((stt.WIDTH, stt.HEIGHT))
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    mobs= pygame.sprite.Group()
    player = Player(stt)
    all_sprites.add(player)
    
    for i in range(8):
        m=Mob(stt)
        all_sprites.add(m)
        mobs.add(m)


    # game loop
    game_is_running = True

    while game_is_running:
        clock.tick(stt.FPS)
        
        #input events
        player.speedx=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
            
        
        all_sprites.update()
       
        screen.fill(stt.BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game()