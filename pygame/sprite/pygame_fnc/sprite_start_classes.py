import pygame, sys
import random



class Settings:
    def __init__(self):
        self.WIDTH = 360
        self.HEIGHT = 480
        self.FPS = 30

        self.white = (255,255,255)
        self.black =(0,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)

class Player(pygame.sprite.Sprite):
    
    # sprite for player
    def __init__(self,stt):
        pygame.sprite.Sprite.__init__(self)
        
        self.stt=stt
        self.image = pygame.Surface((50,50))
        self.image.fill(stt.green)
        self.rect = self.image.get_rect() 
        self.rect.center = ((stt.WIDTH)/2, stt.HEIGHT/2)


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
        screen.fill(stt.blue)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game()