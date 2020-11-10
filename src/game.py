import pygame
from .constant import WIDTH, HEIGHT, DEATH_SOUND, BG_DAY, BG_NIGHT, FLOOR, BLUE_BIRD_MIDFLAP, GAMEOVER, GAMEOVER_RECT
from .bird import Bird
from .pipes import Pipe
from .score import Score

class Game:
    ACTIVE = True
    FLOOR_POS = 1

    def __init__(self, win):
        self.win = win
        self.bird = Bird()
        self.pipe = Pipe(self.win)
        self.score = Score(self.win)
        self.FONT = pygame.font.Font('04B_19.ttf', 30)

    def reset(self):
        self.pipe.pipe_list.clear()
        Bird.rect.center =  (100, HEIGHT//2)
        Bird.BIRD_MOVE = 0
        self.score.SCORE = 0
        self.ACTIVE = True

    def create_pipe(self):
        return self.pipe.create()

    def bird_animation(self):
        if Bird.index < 2:
            Bird.index += 1
        else:
            Bird.index = 0

        Bird.BIRD, Bird.rect = self.bird.animation(Bird.rect, Bird.index)

    def collision(self, bird_rect, pipes):
        # global can_score

        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                DEATH_SOUND.play()
                return False

        if bird_rect.top <= 0 or bird_rect.bottom >= 633:
            DEATH_SOUND.play()
            return False

        return True

    def _draw_floor(self, win, pos):
        win.blit(FLOOR, (pos, 633))
        win.blit(FLOOR, (pos+WIDTH, 633))

    def update(self):
        self.win.blit(BG_DAY, (0,0))

        if self.ACTIVE == True:
            #BIRD MOVEMENT
            Bird.BIRD_MOVE += Bird.GRAVITY
            Bird.rect.centery += Bird.BIRD_MOVE
            self.rotated_bird = self.bird.rotate(Bird.BIRD, Bird.BIRD_MOVE)            
            self.win.blit(self.rotated_bird, Bird.rect)

            self.ACTIVE = self.collision(Bird.rect, self.pipe.pipe_list)
            
            #DRAW PIPES
            self.pipe.pipe_list = self.pipe.move_pipes(self.pipe.pipe_list)
            self.pipe.draw_pipes(self.pipe.pipe_list)

            #SCORE
            self.score.SCORE = self.score.update_score(self.score.SCORE, self.pipe.pipe_list)
            self.score.display_score('main_game', self.FONT, self.score.SCORE, self.score.HIGH_SCORE)

            #FLOOR POSITION
            self.FLOOR_POS -= 1
        else:
            #DRAW BIRD
            self.win.blit(self.rotated_bird, Bird.rect)
            #DRAW PIPES
            self.pipe.draw_pipes(self.pipe.pipe_list)
            #DRAW SCORE
            self.win.blit(GAMEOVER, GAMEOVER_RECT)
            self.score.display_highscore(self.FONT)
        
        #DRAW FLOOR
        self._draw_floor(self.win, self.FLOOR_POS)

        if self.FLOOR_POS  <= -WIDTH:
            self.FLOOR_POS = 0

        pygame.display.update()