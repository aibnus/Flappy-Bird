import pygame, random
from .constant import WIDTH, HEIGHT, PIPE

class Pipe:
    PIPE_HEIGHT = [400,500,600]

    # pipe_list = []
    # SPAWNPIPE = pygame.USEREVENT
    # pygame.time.set_timer(SPAWNPIPE, 1200)

    def __init__(self, win, pipe_list = []):
        self.pipe_list = pipe_list
        self.win = win

    def create(self):
        return self.pipe_list.extend(self.create_pipe())

    def create_pipe(self):
        random_pipe_pos = random.choice(self.PIPE_HEIGHT)
        bottom_pipe = PIPE.get_rect(midtop = (WIDTH+78, random_pipe_pos))
        top_pipe = PIPE.get_rect(midbottom = (WIDTH+78, random_pipe_pos - 225))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 3

        return pipes

    def draw_pipes(self, pipes):
        for pipe in pipes:
            if pipe.bottom >= 720:
                self.win.blit(PIPE, pipe)
            else:
                flip_pipe = pygame.transform.flip(PIPE, False, True)
                self.win.blit(flip_pipe, pipe)