import pygame
# pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=256)
pygame.init()

#APPEARANCES
WIDTH, HEIGHT = 405, 720

#COLORS (R,G,B)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

#ASSETS
BG_DAY = pygame.transform.scale(pygame.image.load('assets/background-day.png'), (WIDTH, HEIGHT))
BG_NIGHT = pygame.transform.scale(pygame.image.load('assets/background-night.png'), (WIDTH, HEIGHT))
FLOOR = pygame.transform.scale(pygame.image.load('assets/base.png'), (WIDTH, 168))

BLUE_BIRD_DWNFLAP = pygame.transform.scale(pygame.image.load('assets/bluebird-downflap.png'), (51, 36))
BLUE_BIRD_MIDFLAP = pygame.transform.scale(pygame.image.load('assets/bluebird-midflap.png'), (51, 36))
BLUE_BIRD_UPFLAP = pygame.transform.scale(pygame.image.load('assets/bluebird-upflap.png'), (51, 36))
BLUE_BIRD_FRAMES = [BLUE_BIRD_DWNFLAP, BLUE_BIRD_MIDFLAP, BLUE_BIRD_UPFLAP]

RED_BIRD_DWNFLAP = pygame.transform.scale(pygame.image.load('assets/redbird-downflap.png'), (51, 36))
RED_BIRD_MIDFLAP = pygame.transform.scale(pygame.image.load('assets/redbird-midflap.png'), (51, 36))
RED_BIRD_UPFLAP = pygame.transform.scale(pygame.image.load('assets/redbird-upflap.png'), (51, 36))
RED_BIRD_FRAMES = [RED_BIRD_DWNFLAP, RED_BIRD_MIDFLAP, RED_BIRD_UPFLAP]

YELLOW_BIRD_DWNFLAP = pygame.transform.scale(pygame.image.load('assets/yellowbird-downflap.png'), (51, 36))
YELLOW_BIRD_MIDFLAP = pygame.transform.scale(pygame.image.load('assets/yellowbird-midflap.png'), (51, 36))
YELLOW_BIRD_UPFLAP = pygame.transform.scale(pygame.image.load('assets/yellowbird-upflap.png'), (51, 36))
YELLOW_BIRD_FRAMES = [YELLOW_BIRD_DWNFLAP, YELLOW_BIRD_MIDFLAP, YELLOW_BIRD_UPFLAP]

PIPE = pygame.transform.scale(pygame.image.load('assets/pipe-green.png'), (78, 480))

SPLASH_SCREEN = pygame.transform.scale(pygame.image.load('assets/message.png'), (276, 400))
SPLASH_SCREEN_RECT = SPLASH_SCREEN.get_rect(center = (WIDTH//2, HEIGHT//2))

GAMEOVER = pygame.transform.scale(pygame.image.load('assets/gameover.png'), (288, 63))
GAMEOVER_RECT = GAMEOVER.get_rect(center = (WIDTH//2, HEIGHT//2))

#SOUND
FLAP_SOUND = pygame.mixer.Sound('sounds/sfx_wing.wav')
SCORE_SOUND = pygame.mixer.Sound('sounds/sfx_point.wav')
DEATH_SOUND = pygame.mixer.Sound('sounds/sfx_hit.wav')