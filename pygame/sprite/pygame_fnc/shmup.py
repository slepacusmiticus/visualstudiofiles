import pygame, sys
import random
from os import path
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
        self.YELLOW =(255,255,0)

        self.img_dir = path.join(path.dirname(__file__), "img")

       
        

class Player(pygame.sprite.Sprite):
    
    # sprite for player
    def __init__(self,stt, bullet_img,all_sprites, bullets,player_img):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_img= bullet_img
        self.stt = stt
        self.image  = (pygame.transform.scale(player_img, (50,38))).convert()
        self.image.set_colorkey(stt.BLACK)
        self.rect = self.image.get_rect() 
        self.rect.centerx = stt.WIDTH/2
        self.rect.bottom = stt.HEIGHT -10
        self.speedx = 0
    
    def shoot(self,stt,bullet_img, all_sprites,bullets):
        bullet = Bullet(stt, bullet_img,self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


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

    def __init__(self,stt,meteor_img) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.stt = stt
        self.image  = (pygame.transform.scale(meteor_img, (25,25))).convert()
        self.image.set_colorkey(stt.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,self.stt.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.stt.HEIGHT + 10 or self.rect.left < -25 or self.rect.right>self.stt.WIDTH + 20:
            self.rect.x = random.randrange(0, self.stt.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)
            

class Bullet(pygame.sprite.Sprite):

    def __init__(self,stt,bullet_img,x,y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.stt = stt
        self.image  = (pygame.transform.scale(bullet_img, (5,35))).convert()
        self.image.set_colorkey(stt.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx=x
        self.speedy=-10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill() 


def game():
        
    pygame.init()
    #pygame.mixer.init()
    stt=Settings()
    screen = pygame.display.set_mode((stt.WIDTH, stt.HEIGHT))
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    # load images
    background = pygame.image.load(path.join(stt.img_dir, "stars.png")).convert()
    background_rect= background.get_rect()
    player_img = pygame.image.load(path.join(stt.img_dir,"playerShip1_orange.png"))
    print(player_img)
    meteor_img = pygame.image.load(path.join(stt.img_dir,"meteorBrown_med1.png"))
    bullet_img = pygame.image.load(path.join(stt.img_dir,"laserRed16.png"))

    
    all_sprites = pygame.sprite.Group()
    mobs= pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player(stt,bullet_img, all_sprites,bullets,player_img)
    all_sprites.add(player)
    
    for i in range(8):
        m=Mob(stt,meteor_img)
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
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    player.shoot(stt,bullet_img,all_sprites, bullets)
        
        all_sprites.update() 
        hits = pygame.sprite.groupcollide(mobs, bullets,True, True) # dokill1, dokill2, collided = None)
        for hit in hits:
            m=Mob(stt,meteor_img)
            all_sprites.add(m)
            mobs.add(m)
 
        hits=pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            game_is_running = False
       
        screen.fill(stt.BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game()