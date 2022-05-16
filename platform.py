import pygame,time
from levels import *
from constants import *



class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,ID,solid,semi):
        pygame.sprite.Sprite.__init__(self)
        self.ID = ID
        
        if self.ID == 1:
            self.image = pygame.image.load('Graphics/Tiles/gtopleft.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 1
            self.solid = solid

        if self.ID == 2:
            self.image = pygame.image.load('Graphics/Tiles/gtopmid.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 2
            self.solid = solid

        if self.ID == 3:
            self.image = pygame.image.load('Graphics/Tiles/gtopright.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 3
            self.solid = solid

        if self.ID == 4:
            self.image = pygame.image.load('Graphics/Tiles/gleftmid.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 4
            self.solid = solid

        if self.ID == 5:
            self.image = pygame.image.load('Graphics/Tiles/gmidmid.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 5
            self.solid = solid 

        if self.ID == 6:
            self.image = pygame.image.load('Graphics/Tiles/grightmid.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 6
            self.solid = solid

        if self.ID == 7:
            self.image = pygame.image.load('Graphics/Tiles/gleftbottom.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 7
            self.solid = solid

        if self.ID == 8:
            self.image = pygame.image.load('Graphics/Tiles/gmidbottom.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 8
            self.solid = solid 


        if self.ID == 9:
            self.image = pygame.image.load('Graphics/Tiles/grightbottom.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 9
            self.solid = solid


        if self.ID == 'a':
            self.image = pygame.image.load('Graphics/Tiles/cementblock.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 'a'
            self.solid = solid

        if self.ID == 'b':
            self.image = pygame.image.load('Graphics/Tiles/cloudtile.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
            self.id = 'b'
            self.solid = solid

        if self.ID == 'c':
            self.id = 'c'
            self.coin_frames = []
            self.solid = solid

            self.coin_frames.append(pygame.image.load('Graphics/Objects/coin1.png').convert_alpha())
            self.coin_frames[0] = pygame.transform.scale(self.coin_frames[0],(12 * SCALE, 16 * SCALE))
            self.coin_frames.append(pygame.image.load('Graphics/Objects/coin2.png').convert_alpha())
            self.coin_frames[1] = pygame.transform.scale(self.coin_frames[1],(12 * SCALE, 16 * SCALE))
            self.coin_frames.append(pygame.image.load('Graphics/Objects/coin3.png').convert_alpha())
            self.coin_frames[2] = pygame.transform.scale(self.coin_frames[2],(12 * SCALE, 16 * SCALE))
            self.coin_frames.append(pygame.image.load('Graphics/Objects/coin4.png').convert_alpha())
            self.coin_frames[3] = pygame.transform.scale(self.coin_frames[3],(12 * SCALE, 16 * SCALE))

            self.image = self.coin_frames[0]
            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.y = y
            self.num = 0
            self.timer = 0
            self.onscreen = False


        if self.ID == 'd':
            self.qblockframes = []
            self.qblockhitframe = []
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock1.png').convert_alpha())
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock2.png').convert_alpha())
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock3.png').convert_alpha())
            self.qblockframes.append(pygame.image.load('Graphics/Tiles/qblock4.png').convert_alpha())
            self.qblockhitframe.append(pygame.image.load('Graphics/Tiles/qblockhit.png').convert_alpha())
            self.qblockframes[0] = pygame.transform.scale(self.qblockframes[0],(TILESIZE,TILESIZE))
            self.qblockframes[1] = pygame.transform.scale(self.qblockframes[1],(TILESIZE,TILESIZE))
            self.qblockframes[2] = pygame.transform.scale(self.qblockframes[2],(TILESIZE,TILESIZE))
            self.qblockframes[3] = pygame.transform.scale(self.qblockframes[3],(TILESIZE,TILESIZE))
            self.qblockhitframe[0] = pygame.transform.scale(self.qblockhitframe[0],(TILESIZE,TILESIZE))
            self.id = 'd'
            self.solid = solid
            self.state = 'nothit'
            self.anim_timer = 2
            self.anim_num = 0
            self.image = self.qblockframes[0]
            self.hit_timer = 3
            self.hit_move = False
            self.newrect = False


        if self.ID == 'e':
            self.image = pygame.image.load('Graphics/Tiles/bush1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image,(96 * SCALE,56 * SCALE))
            self.id = 'e'
            self.solid = solid

        if self.ID == '@':
            self.mole_frames = []
            self.mole_frames.append(pygame.image.load('graphics/Tiles/gmidmid.png').convert_alpha()) 
            self.mole_frames.append(pygame.image.load('graphics/Tiles/moleout.png').convert_alpha())
            self.mole_frames[0] = pygame.transform.scale(self.mole_frames[0],(TILESIZE,TILESIZE))
            self.mole_frames[1] = pygame.transform.scale(self.mole_frames[1],(TILESIZE,TILESIZE))
            self.image = self.mole_frames[0]
            self.rect = pygame.Rect(x,y,TILESIZE,TILESIZE)
            self.id = '@'
            self.solid = solid


        self.semisolid = semi
        self.rect = pygame.Rect(x,y,TILESIZE,TILESIZE)
        self.onscreen = False


    def update(self,playerx):

        if self.rect.x > playerx and self.rect.x - playerx > S_WIDTH or self.rect.x < playerx and playerx - self.rect.x > S_WIDTH:
            self.onscreen = False

        else:
            self.onscreen = True


            if self.id == 'c':
                if self.timer >= 3:
                    self.timer = 0
                    if self.num >= 3:
                        self.num = 0
                    self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,top=self.rect.top,bottom=self.rect.bottom)
                    self.image = self.coin_frames[self.num]
                    self.num+= 1    

                else:
                    self.timer += 1

            elif self.id == 'd' and self.state == 'nothit':
                if self.anim_timer > 0:
                    self.anim_timer -= 1

                else:
                    self.image = self.qblockframes[self.anim_num]
                    if self.anim_num < len(self.qblockframes) - 1:
                        self.anim_num += 1
                    else:
                        self.anim_num = 0
                    self.anim_timer = 2

            elif self.id == 'd' and self.state == 'hit':
                self.image = self.qblockhitframe[0]
 
                if self.hit_timer > 0:
                    self.hit_timer -= 1
                    self.rect.y -= 4

                else:
                    if self.hit_timer == 0 and self.hit_move == False:
                        self.hit_timer = -3
                        self.hit_move = True
                    if self.hit_timer < 0:
                        self.hit_timer += 1
                        self.rect.y += 4

                    else:
                        self.hit_timer = 0
                        for m in powerups:
                            if m.rect.x == self.rect.x and m.rect.y == self.rect.y:
                                m.move = True

            elif self.id == '@':
                for e in enemies:
                    if e.ID == 2:
                        if e.homex == self.rect.x and e.homey == self.rect.y and e.ID == 2 and e.state == 'jump':
                            self.image = self.mole_frames[1]

                    else:
                        pass


                                    


                                







 

