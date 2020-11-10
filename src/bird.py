import pygame
from .constant import WIDTH, HEIGHT, BLUE_BIRD_FRAMES

class Bird:
    index = 0
    BIRD = BLUE_BIRD_FRAMES[index]
    rect = BIRD.get_rect(center = (100, HEIGHT//2))

    BIRD_MOVE = 0
    GRAVITY = 0.1875

    # BIRDFLAP = pygame.USEREVENT + 1
    # pygame.time.set_timer(BIRDFLAP, 200)

    def __init__(self):
        pass

    def rotate(self, bird, movement):
        new_bird = pygame.transform.rotozoom(bird, movement * -2, 1)
        return new_bird

    def animation(self, bird_rect, index):
        new_bird = BLUE_BIRD_FRAMES[index]
        new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
        return new_bird, new_bird_rect
