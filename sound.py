import pygame
from constants import *

pygame.mixer.pre_init(22050,-16, 2, 1024)
pygame.init()

def music(level):
    if level == 1:
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load('Sound/Overworld.mp3')
        pygame.mixer.music.play(-1)



jump_sfx = pygame.mixer.Sound('Sound/jump.wav')
all_sfx.append(jump_sfx)
jump_sfx.set_volume(1.0)

powerup_appear_sfx = pygame.mixer.Sound('Sound/powerup_appear.wav')
all_sfx.append(powerup_appear_sfx)
powerup_appear_sfx.set_volume(1.0)

powerup_sfx = pygame.mixer.Sound('Sound/powerup.wav')
all_sfx.append(powerup_sfx)
powerup_sfx.set_volume(1.0)

coin_sfx = pygame.mixer.Sound('Sound/coin.wav')
all_sfx.append(coin_sfx)
coin_sfx.set_volume(1.0)

pause_sfx = pygame.mixer.Sound('Sound/pause.wav')
all_sfx.append(pause_sfx)
pause_sfx.set_volume(1.0)


kick_sfx = pygame.mixer.Sound('Sound/kick.wav')
all_sfx.append(kick_sfx)
kick_sfx.set_volume(1.0)

breakblock_sfx = pygame.mixer.Sound('Sound/breakblock.wav')
all_sfx.append(breakblock_sfx)
breakblock_sfx.set_volume(1.0)