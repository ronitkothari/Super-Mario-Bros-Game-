import pygame
from constants import *

class Background(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,filename,ID,total_level_height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.oldx = x
        self.level_height = total_level_height
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.onscreen = True
        self.delay = 0
        self.id = ID

    def update(self,x,y,playerxvel,camx):

        self.rect.x = (camx * -1)/ 2 + self.oldx
        self.rect.y = self.level_height-self.h









