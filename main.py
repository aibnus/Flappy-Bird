import pygame, random
from src.constant import WIDTH, HEIGHT, FLAP_SOUND
from src.bird import Bird
from src.game import Game

FPS = 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.ACTIVE == True:
                    Bird.BIRD_MOVE = 0
                    Bird.BIRD_MOVE -= 5
                    FLAP_SOUND.play()
                if event.key == pygame.K_SPACE and game.ACTIVE == False:
                    game.reset()

            if event.type == SPAWNPIPE:
                game.create_pipe()

            if event.type == BIRDFLAP:
                game.bird_animation()

        game.update()
    
    pygame.quit()

main()