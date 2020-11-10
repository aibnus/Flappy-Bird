import pygame
from .constant import WIDTH, HEIGHT, WHITE, SCORE_SOUND

class Score:
    SCORE = 0
    HIGH_SCORE = 0
    can_score = True

    def __init__(self, win):
        self.win = win

    def display_score(self, game_state, font, score, high_score):
        if game_state == 'main_game':
            new_score = font.render(str(int(score)), True, (WHITE))
            score_rect = new_score.get_rect(center = (WIDTH//2, 100))
            self.win.blit(new_score, score_rect)
        elif game_state == 'game_over':
            new_score = font.render(f'Score: {int(score)}', True, (WHITE))
            score_rect = new_score.get_rect(center = (WIDTH//2, 100))
            self.win.blit(new_score, score_rect)

            new_high_score = font.render(f'High Score: {int(high_score)}', True, (WHITE))
            high_score_rect = new_high_score.get_rect(center = (WIDTH//2, 550))
            self.win.blit(new_high_score, high_score_rect)

    def update_score(self, score, pipe_list):
        if pipe_list:
            for pipe in pipe_list:
                if 98 < pipe.centerx < 102 and self.can_score:
                    score += 1
                    SCORE_SOUND.play()
                    self.can_score = False
                elif pipe.centerx < 0:
                    self.can_score = True

        return score

    def update_high_score(self, score, high_score):
        if score > high_score:
            high_score = score

        return high_score    

    def display_highscore(self, font):
        self.HIGH_SCORE = self.update_high_score(self.SCORE, self.HIGH_SCORE)
        self.display_score('game_over', font, self.SCORE, self.HIGH_SCORE)