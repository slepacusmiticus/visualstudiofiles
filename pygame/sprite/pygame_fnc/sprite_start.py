import pygame, sys
import random




def game():
    WIDTH = 360
    HEIGHT = 480
    FPS = 30

    white = (255,255,255)
    black =(0,0,0)
    blue = (0,0,255)
    green = (0,255,0)
    
    pygame.init()
    #pygame.mixer.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('My game')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    game_is_running = True

    while game_is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False
                
        
        screen.fill(blue)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game()