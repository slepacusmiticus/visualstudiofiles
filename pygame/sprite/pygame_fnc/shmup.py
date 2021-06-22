import pygame, sys
import random
from os import path
from pygame.constants import K_LEFT, K_RIGHT



class Settings:
    def __init__(self):
        self.WIDTH = 700
        self.HEIGHT = 500
        self.FPS = 60

        self.WHITE = (255,255,255)
        self.BLACK =(0,0,0)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.YELLOW =(255,255,0)

        self.img_dir = path.join(path.dirname(__file__), "img")
        self.snd_dir = path.join(path.dirname(__file__), "snd")
        
        self.font_name =pygame.font.match_font('arial')

       
        
   
class Player(pygame.sprite.Sprite):
    
    # sprite for player
    def __init__(self,stt, bullet_img,all_sprites, bullets,player_img, shoot_sound):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.bullets=bullets
        self.bullet_img= bullet_img
        self.shoot_sound= shoot_sound
        self.stt = stt
        self.image = (pygame.transform.scale(player_img, (50,38))).convert()
        self.image.set_colorkey(stt.BLACK)
        self.rect = self.image.get_rect() 
        self.radius=20
        # pygame.draw.circle(self.image, stt.RED,self.rect.center,self.radius)
        self.rect.centerx = stt.WIDTH/2
        self.rect.bottom = stt.HEIGHT -10
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden =False
        self.hide_timer = pygame.time.get_ticks()

    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.stt, self.bullet_img, self.rect.centerx, self.rect.top)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)
            self.shoot_sound.play()

    def hide(self):
        self.hidden = True
        self.hidden_timer = pygame.time.get_ticks()
        self.rect.center = (self.stt.WIDTH/2, self.stt.HEIGHT + 200)

    def update(self):
        #unhide if hidden
        if self.hidden and pygame.time.get_ticks()-self.hidden_timer >1000: 
            self.hidden =False
            self.rect.centerx=self.stt.WIDTH/2 
            self.rect.bottom=self.stt.HEIGHT -10


        self.speedx = 0
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > self.stt.WIDTH:
            self.rect.right = self.stt.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):

    def __init__(self,stt,meteor_img) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.stt = stt
        
        self.image_orig  = random.choice(meteor_img)  # (pygame.transform.scale(meteor_img, (25,25))).convert()
        self.image_orig.set_colorkey(stt.BLACK)
        self.image =  self.image_orig.copy() 
        self.rect = self.image.get_rect()
        self.radius=(self.rect.width*.8/2)   
        # pygame.draw.circle(self.image, stt.RED,self.rect.center,self.radius)
        self.rect.x = random.randrange(0,self.stt.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150,-100)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update= pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()  
        if now - self.last_update >50:
            self.last_update = now
            self.rot= (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center



    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > self.stt.HEIGHT + 10 or self.rect.left < -25 or self.rect.right>self.stt.WIDTH + 20:
            self.rect.x = random.randrange(0, self.stt.WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            

class Bullet(pygame.sprite.Sprite):

    def __init__(self, stt, bullet_img, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.stt = stt
        self.image  = (pygame.transform.scale(bullet_img, (5,35))).convert()
        self.image.set_colorkey(stt.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy =-10

    def update(self):
        self.rect.y += self.speedy 

        if self.rect.bottom < 0:
            self.kill() 

class Explosion(pygame.sprite.Sprite):
    def __init__(self,explosion_anim, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.explosion_anim =explosion_anim
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update =pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def draw_text(surf, text, size, x, y):
    stt = Settings()
    font = pygame.font.Font(stt.font_name, size)
    text_surface = font.render(text, True, stt.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop =  (x, y)
    surf.blit(text_surface, text_rect)

def newmob(stt, meteor_img, all_sprites, mobs):
    m = Mob(stt, meteor_img)
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LEN =100
    BAR_HEIGHT =10
    fill = (pct) / 100 * BAR_LEN
    outline_rect = pygame.Rect(x,y,  BAR_LEN, BAR_HEIGHT)
    fill_rect=pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame. draw.rect(surf, (0, 255, 0), fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 2)

def draw_lives(surf,x,y,lives,img):
    for _ in range (lives):
        img_rect=img.get_rect()
        img_rect.x = x+30 * _
        img_rect.y = y
        surf.blit(img, img_rect)

def game():
        
    pygame.init()
    pygame.mixer.init()
    stt = Settings()
    screen = pygame.display.set_mode((stt.WIDTH, stt.HEIGHT))
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    # load images
    background = pygame.image.load(path.join(stt.img_dir, "stars.png")).convert()
    background_rect= background.get_rect()
    player_img = pygame.image.load(path.join(stt.img_dir,"playerShip1_orange.png"))
    player_mini_img =pygame.transform.scale(player_img,(25,19))
    player_mini_img.set_colorkey(stt.BLACK)
    bullet_img = pygame.image.load(path.join(stt.img_dir, "laserRed16.png"))
    meteor_img = []
    meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_med1.png', 
                  'meteorBrown_med1.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png', 
                  'meteorBrown_tiny1.png'] 
    for img in meteor_list:
        print('\nXXX',path.join(stt.img_dir,img))
        meteor_img.append(pygame.image.load(path.join(stt.img_dir, img)).convert())

    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = []
    explosion_anim['player']=[]
    for _ in range(9):
        filename = f'regularExplosion0{_}.png'
        img = pygame.image.load(path.join(stt.img_dir,filename)).convert()
        img.set_colorkey(stt.BLACK)
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32,32))
        explosion_anim['sm'].append(img_sm)
        #explosion for the player if it's hit
        filename = f'sonicExplosion0{_}.png'
        img = pygame.image.load(path.join(stt.img_dir,filename)).convert()
        img.set_colorkey(stt.BLACK)
        explosion_anim['player'].append(img)

    # load all game sounds
    shoot_sound = pygame.mixer.Sound(path.join(stt.snd_dir, "laser9.wav"))
    pygame.mixer.Sound.set_volume(shoot_sound, 0.3)

    expl_sounds =[]
    for snd in ['rock_breaking.flac', 'expl.wav']:
        expl_sounds.append(pygame.mixer.Sound(path.join(stt.snd_dir, snd)))
        #pygame.mixer.Sound.set_volume(expl_sounds[0:], 0.3)
    for sound in expl_sounds:
        sound.set_volume(0.2)

    player_die_snd = pygame.mixer.Sound(path.join(stt.snd_dir, 'rumble1.ogg'))
    pygame.mixer.Sound.set_volume(player_die_snd, 0.9)
    pygame.mixer.music.load(path.join(stt.snd_dir, 'bkg.wav'))
    pygame.mixer.music.set_volume(0.1)

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player(stt, bullet_img, all_sprites, bullets, player_img, shoot_sound)
    all_sprites.add(player)


    for i in range(8):
        newmob(stt, meteor_img, all_sprites,mobs)

    score = 0
    pygame.mixer.music.play(loops=-1)

    # game loop
    game_is_running = True
    while game_is_running:
        clock.tick(stt.FPS)
        
        # input events
        player.speedx=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_is_running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key ==pygame.K_SPACE:
            #         player.shoot(stt,bullet_img,all_sprites, bullets,shoot_sound)
        
        all_sprites.update() 
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True) # dokill1, dokill2, collided = None)
        for hit in hits: 
            score += abs(50 - (int(hit.radius))) 
            random.choice(expl_sounds).play()
            expl = Explosion(explosion_anim,hit.rect.center, "lg")
            all_sprites.add(expl)
            newmob(stt, meteor_img, all_sprites, mobs)
    
 
        hits=pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= int(hit.radius) *2
            expl = Explosion(explosion_anim,hit.rect.center, "sm")
            all_sprites.add(expl)
            newmob(stt,meteor_img, all_sprites,mobs)
            if player.shield <= 0:
                player_die_snd.play()
                death_explosion= Explosion(explosion_anim, player.rect.center,'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -=1
                player.shields = 100

        if player.lives==0 and not death_explosion.alive():
            game_is_running = False

            

        screen.fill(stt.BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score),24, stt.WIDTH/2, 10)
        draw_shield_bar(screen, 5,5, player.shield)
        draw_lives(screen, stt.WIDTH-100,5,player.lives,player_mini_img)
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game()