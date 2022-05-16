import pygame
from constants import *
from levels import *
from sound import *


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.jump = False
        self.fall = False
        self.crouch = False
        self.playerun = False
        self.runmax = False

        self.maximum_velocity = 30
        self.gravity = 0.4
        self.max_speed = 3
        self.run_speed = 6
        self.jump_speed = 7
        self.runjump_speed = 9
        self.jump_cooldown = 0
        self.acceleration = 0.2
        self.friction = 0.1
        self.image_speed = 10  
        self.onscreen = True
        self.collision = False
        self.grounded = False
        self.lastframe = 0
        self.glide = False
        self.glidetimer = 0
        self.jump_power = 5

        self.powerup_pause = False
        self.powertimer = 4
        self.powernum = 0
        self.pimgcount = 1

        self.walkframes_s = []
        self.walkframes_s.append(pygame.image.load('Graphics/Mario/smallmstill.png').convert_alpha())
        self.walkframes_s.append(pygame.image.load('Graphics/Mario/smallmwalk.png').convert_alpha())

        self.walkframes_b = []
        self.walkframes_b.append(pygame.image.load('Graphics/Mario/bigmstill.png').convert_alpha())
        self.walkframes_b.append(pygame.image.load('Graphics/Mario/bigmwalk1.png').convert_alpha())
        self.walkframes_b.append(pygame.image.load('Graphics/Mario/bigmwalk2.png').convert_alpha())

        self.runframes_s = []
        self.runframes_s.append(pygame.image.load('Graphics/Mario/smallmrun1.png').convert_alpha())
        self.runframes_s.append(pygame.image.load('Graphics/Mario/smallmrun2.png').convert_alpha())


        self.runframes_b = []
        self.runframes_b.append(pygame.image.load('Graphics/Mario/bigmrun1.png').convert_alpha())
        self.runframes_b.append(pygame.image.load('Graphics/Mario/bigmrun2.png').convert_alpha())
        self.runframes_b.append(pygame.image.load('Graphics/Mario/bigmrun3.png').convert_alpha())

        self.jumpframe_s = []
        self.jumpframe_s.append(pygame.image.load('Graphics/Mario/smallmjump.png').convert_alpha())

        self.runjumpframe_s = []
        self.runjumpframe_s.append(pygame.image.load('Graphics/Mario/smallmrunjump.png').convert_alpha())


        self.jumpframe_b = []
        self.jumpframe_b.append(pygame.image.load('Graphics/Mario/bigmjump.png').convert_alpha())


        self.runjumpframe_b = []
        self.runjumpframe_b.append(pygame.image.load('Graphics/Mario/bigmrunjump.png').convert_alpha())

        self.fallframe_s = []
        self.fallframe_s.append(pygame.image.load('Graphics/Mario/smallmfall.png').convert_alpha())

        self.fallframe_b = []
        self.fallframe_b.append(pygame.image.load('Graphics/Mario/bigmfall.png').convert_alpha())


        self.quickturn_frame_s = []
        self.quickturn_frame_s.append(pygame.image.load('Graphics/Mario/smallmquickturn.png').convert_alpha())

        self.quickturn_frame_b = []
        self.quickturn_frame_b.append(pygame.image.load('Graphics/Mario/bigmquickturn.png').convert_alpha())

        self.crouch_frame_s = []
        self.crouch_frame_s.append(pygame.image.load('Graphics/Mario/smallmcrouch.png').convert_alpha())

        self.crouch_frame_b = []
        self.crouch_frame_b.append(pygame.image.load('Graphics/Mario/bigmcrouch.png').convert_alpha())

        self.powerup_frames = []
        self.powerup_frames.append(pygame.image.load('Graphics/Mario/smallmstill.png').convert_alpha())
        self.powerup_frames.append(pygame.image.load('Graphics/Mario/bigmstill.png').convert_alpha())


        self.powerup_frames[0] = pygame.transform.scale(self.powerup_frames[0],(14 * SCALE, 20 * SCALE))
        self.powerup_frames[1] = pygame.transform.scale(self.powerup_frames[1],(15 * SCALE, 28 * SCALE))

        self.walkframes_s[0] = pygame.transform.scale(self.walkframes_s[0],(14 * SCALE, 20 * SCALE))
        self.walkframes_s[1] = pygame.transform.scale(self.walkframes_s[1],(15 * SCALE, 20 * SCALE))
        self.runframes_s[0] = pygame.transform.scale(self.runframes_s[0],(15 * SCALE, 20 * SCALE))
        self.runframes_s[1] = pygame.transform.scale(self.runframes_s[1],(16 * SCALE, 19 * SCALE))
        self.runjumpframe_s[0] = pygame.transform.scale(self.runjumpframe_s[0],(14 * SCALE, 20 * SCALE))
        self.jumpframe_s[0] = pygame.transform.scale(self.jumpframe_s[0],(16 * SCALE, 22 * SCALE))
        self.quickturn_frame_s[0] = pygame.transform.scale(self.quickturn_frame_s[0],(15 * SCALE, 21 * SCALE))
        self.fallframe_s[0] = pygame.transform.scale(self.fallframe_s[0],(16*SCALE,20*SCALE))



        self.fallframe_b[0] = pygame.transform.scale(self.fallframe_b[0],(16*SCALE,29*SCALE))
        self.walkframes_b[0] = pygame.transform.scale(self.walkframes_b[0],(15 * SCALE, 28 * SCALE))
        self.walkframes_b[1] = pygame.transform.scale(self.walkframes_b[1],(16 * SCALE, 28 * SCALE))
        self.walkframes_b[2] = pygame.transform.scale(self.walkframes_b[2],(16 * SCALE, 27 * SCALE))
        self.runframes_b[0] = pygame.transform.scale(self.runframes_b[0],(18 * SCALE, 28 * SCALE))
        self.runframes_b[1] = pygame.transform.scale(self.runframes_b[1],(18 * SCALE, 28 * SCALE))
        self.runframes_b[2] = pygame.transform.scale(self.runframes_b[2],(18 * SCALE, 27 * SCALE))
        self.jumpframe_b[0] = pygame.transform.scale(self.jumpframe_b[0],(16 * SCALE, 31 * SCALE))
        self.runjumpframe_b[0] = pygame.transform.scale(self.runjumpframe_b[0],(19 * SCALE, 26 * SCALE))
        self.quickturn_frame_b[0] = pygame.transform.scale(self.quickturn_frame_b[0],(16 * SCALE, 29 * SCALE))
        self.crouch_frame_b[0] = pygame.transform.scale(self.crouch_frame_b[0],(16 * SCALE, 15 * SCALE))
        self.crouch_frame_s[0] = pygame.transform.scale(self.crouch_frame_s[0],(15 * SCALE, 14 * SCALE))

        self.image = self.walkframes_s[0]
        self.rect = self.image.get_rect(x=TILESIZE,y= total_level_height - TILESIZE * 3)

        self.direction = 'right'
        self.state = 'small'
 
     
    def update(self, up, down, left, right, run, platforms):
        if self.powerup_pause == True:
            self.state = 'big'
            self.xvel = 0
            self.right = False
            self.left = False
            if self.powernum < 8:
                if self.powertimer > 0:
                    self.powertimer -= 1

                else:
                    if self.pimgcount == 1:
                        self.image = self.walkframes_b[0]
                    elif self.pimgcount == 2:
                        self.image = self.walkframes_s[0]

                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)
                    self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=15*SCALE,bottom=self.rect.bottom,left=self.rect.left)
                    if self.pimgcount == 1:
                        self.pimgcount = 2
                    else:
                        self.pimgcount = 1
                    self.powertimer = 4
                    self.powernum += 1

            else:

                self.powerup_pause = False
                if not self.crouch:
                    self.image = self.walkframes_b[0]
                if self.direction == 'left':
                    self.image = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=15 * SCALE,h= 28 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)
            

        else:

            if not (self.fall or self.jump) and (self.yvel> -1 and self.yvel <  0.9):
                self.grounded = True

            else:
                self.grounded = False

            if not down:    
                    if self.state == 'small':
                        self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=13 * SCALE,h= 20 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

                    if self.state == 'big':
                        self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=13 * SCALE,h= 28 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

            else:
                if down and self.crouch:
                    if self.state == 'small':
                        self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=13 * SCALE,h= 14 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

                    if self.state == 'big':
                        self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=13 * SCALE,h= 15 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

            if up and self.jump== True:
                if self.jump_power > 0:
                    self.yvel -= 0.5
                    self.jump_power -= 1

            if not up:
                self.jump_power = 0

            if self.glidetimer > 0:
                self.glidetimer -= 1
                self.acceleration = 0.5
            else:
                self.glidetimer = 0
                self.acceleration = 0.2
                self.glide = False

            if self.state == 'small':
                self.jump_speed = 6
                self.runjump_speed = 8

            else:
                self.jump_speed = 7
                self.runjump_speed = 9

            if self.yvel > 0.8:
              self.fall = True
              if not self.crouch:
                if self.state == 'small':
                    self.image = self.fallframe_s[0]
                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)

                else:
                    self.image = self.fallframe_b[0]
                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)                

            if self.rect.x <= 0:
                self.rect.x = 1
                self.xvel = 0  

            if self.jump == True and self.fall == False and not down:

                if self.runmax:
                    if self.state == 'small': 
                        self.image = self.runjumpframe_s[0]
                    elif self.state == 'big':
                        self.image = self.runjumpframe_b[0]
                    
                else:
                    if self.state == 'small': 
                        self.image = self.jumpframe_s[0]
                    elif self.state == 'big':
                        self.image = self.jumpframe_b[0]

                if self.direction == 'left':
                    self.image = pygame.transform.flip(self.image,True,False)


            if up and not down and self.jump_cooldown == 0:
                if self.onGround:
                    self.jump_cooldown = 2
                    self.jump = True
                    jump_sfx.play()

                    if self.runmax:
                        self.yvel -= self.runjump_speed
                        self.jump_power = 4
                    else:
                        self.yvel -= self.jump_speed
                        self.jump_power = 8

            if down and not (self.jump):
                self.crouch = True
                if self.state == 'small':
                    self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=13 * SCALE,h= 14 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

                if self.state == 'big':
                    self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=13 * SCALE,h= 15 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

                if  not self.jump:
                    if self.state == 'small':
                        if self.direction == 'right':
                            self.image = self.crouch_frame_s[0]


                        else:
                            self.image = self.crouch_frame_s[0]
                            self.image = pygame.transform.flip(self.image,True,False)


                    elif self.state == 'big':
                        if self.direction == 'right':
                            self.image = self.crouch_frame_b[0]
                   

                        else:
                            self.image = self.crouch_frame_b[0]
                            self.image = pygame.transform.flip(self.image,True,False)   
            else:

                if self.crouch == True:
                    down = False 
                    self.crouch = False
        
                    if self.state == 'small':
                        self.image = self.walkframes_s[0]

                    elif self.state == 'big':
                        self.image = self.walkframes_b[0]

                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)  
            

            if run and not down:
                if left and self.rect.x > 0 and not right and not down and self.xvel <= -self.max_speed:
                    self.playerun = True
                    if self.xvel > -self.run_speed and not down and not (self.jump or self.fall):
                        self.xvel -= self.acceleration /4
                        self.runmax = False

                    elif not self.xvel > -self.run_speed :
                        if not down:
                            self.runmax = True
                            self.xvel = -self.run_speed 

                if right and not left and not down and self.xvel >= self.max_speed and not (self.jump or self.fall):
                    self.playerun = True
                    if self.xvel < self.run_speed and not down and not (self.jump or self.fall):
                        self.xvel += self.acceleration /4
                        self.runmax = False

                    elif not self.xvel < self.run_speed:
                        if not down:
                            self.runmax = True
                            self.xvel = self.run_speed 

            else:
                self.playerun = False
                self.runmax = False

            if left and self.rect.x > 0 and not right and not down:
                
                self.direction = 'left'
                if self.xvel > -self.max_speed and not down:
                    self.xvel -= self.acceleration

                else:
                    if not down and not self.playerun:

                        if self.xvel < -self.max_speed -1:
                            self.xvel += 0.05

                        else:
                            self.xvel = -self.max_speed


                if not self.jump and not self.fall and (self.rect.x // self.image_speed) != self.lastframe  and self.glide == False:

                    if self.xvel < -self.max_speed - 2.5:

                        if self.state == 'small':
                            self.frame = (self.rect.x // self.image_speed) % len(self.runframes_s)
                            self.lastframe = self.rect.x // self.image_speed
                            self.image = self.runframes_s[self.frame]

                        elif self.state == 'big':
                            self.frame = (self.rect.x // self.image_speed) % len(self.runframes_b)
                            self.lastframe = self.rect.x // self.image_speed
                            self.image = self.runframes_b[self.frame]

                    else:

                        if self.state == 'small':
                            self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_s)
                            self.lastframe = self.rect.x // self.image_speed
                            self.image = self.walkframes_s[self.frame]

                        elif self.state == 'big':
                            self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_b)
                            self.lastframe = self.rect.x // self.image_speed
                            self.image = self.walkframes_b[self.frame]
                    self.image = pygame.transform.flip(self.image,True,False)

                elif self.xvel > 1.5 and self.jump == False and self.fall == False and self.glide == False and not down:

                    if self.xvel > self.max_speed:
                        self.glidetimer = 15
                    else:
                        self.glidetimer = 6
                    self.glide = True

                    if self.state == 'small':
                        self.image = self.quickturn_frame_s[0]
                        self.image = pygame.transform.flip(self.image,True,False)

                    elif self.state == 'big':
                        self.image = self.quickturn_frame_b[0]
                        self.image = pygame.transform.flip(self.image,True,False)


            if right and not left and not down:
                self.direction = 'right'
                if self.xvel < self.max_speed and not down:
                    self.xvel += self.acceleration

                else:
                    if not down and not self.playerun:

                        if self.xvel > self.max_speed + 1:
                            self.xvel -= 0.05

                        else:
                            self.xvel = self.max_speed

                if not self.jump and not self.fall and (self.rect.x // self.image_speed) != self.lastframe and self.glide == False and not down:
                    
                    if self.xvel > self.max_speed + 2.5:


                        if self.state == 'small':
                            self.frame = (self.rect.x // self.image_speed) % len(self.runframes_s)
                            self.lastframe = (self.rect.x // self.image_speed)
                            self.image = self.runframes_s[self.frame]

                        elif self.state == 'big':
                            self.frame = (self.rect.x // self.image_speed) % len(self.runframes_b)
                            self.lastframe = self.rect.x // self.image_speed
                            self.image = self.runframes_b[self.frame]

                    else:
                        if self.state == 'small':
                            self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_s)
                            self.lastframe = (self.rect.x // self.image_speed)
                            self.image = self.walkframes_s[self.frame]

                        elif self.state == 'big':
                            self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_b)
                            self.lastframe = self.rect.x // self.image_speed
                            self.image = self.walkframes_b[self.frame]


                elif self.xvel < -1.5 and self.jump == False and self.fall == False and self.glide == False and not down:

                    if self.xvel < -self.max_speed:
                        self.glidetimer = 15
                    else:
                        self.glidetimer = 6
                    self.glide = True
                    if self.state == 'small':
                        self.image = self.quickturn_frame_s[0]
                    elif self.state == 'big':
                        self.image = self.quickturn_frame_b[0]

            if not self.onGround:

                self.yvel += self.gravity
                if self.yvel > self.maximum_velocity:
                    self.yvel = self.maximum_velocity

            if not(left or right) or (left and right) or down:
                
                if self.xvel > self.friction:
                    self.xvel -= self.friction
                   
                elif self.xvel < self.friction:
                    self.xvel += self.friction
                 	
                else:
                    self.xvel = 0

                if self.jump == False and self.fall == False and not down and (self.xvel > 0 or self.xvel < 0):
                    if self.state == 'small':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_s)
                        self.image = self.walkframes_s[self.frame]

                    elif self.state == 'big':
                        self.frame = (self.rect.x // self.image_speed) % len(self.walkframes_b)
                        self.image = self.walkframes_b[self.frame]
                  
                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)    
                if self.jump == False and self.fall == False and (self.xvel > 0 and self.xvel < 0.2) and not down:
                    if self.state == 'small':
                        self.image = self.walkframes_s[0]

                    elif self.state == 'big':
                        self.image = self.walkframes_b[0]

                    if self.direction == 'left':
                        self.image = pygame.transform.flip(self.image,True,False)  
        
            self.rect.left += round(self.xvel,1)
       
            self.collide(self.xvel, 0, platforms)
      
            self.rect.top += self.yvel
        
            self.onGround = False;

            self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if p.solid == True:

                    if xvel > 0:
                        self.rect.right = p.rect.left
                        self.xvel = 0
                        if not self.crouch and not self.fall and not self.jump:
                            if self.state == 'small':
                                self.image = self.walkframes_s[0]

                            elif self.state == 'big':
                                self.image = self.walkframes_b[0]

                            if self.direction == 'left':
                                self.image = pygame.transform.flip(self.image,True,False)

                    if xvel < 0:
                        self.rect.left = p.rect.right
                        self.xvel = 0
                        if not self.crouch and not self.fall and not self.jump:
                            if self.state == 'small':
                                self.image = self.walkframes_s[0]

                            elif self.state == 'big':
                                self.image = self.walkframes_b[0]

                            if self.direction == 'left':
                                self.image = pygame.transform.flip(self.image,True,False)


                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0
                        self.jump_power = 0
                        if p.id == 'd':
                        	p.state = 'hit'

                           
                    if yvel > 0 and p.semisolid == False:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.jump = False
                        self.fall = False
                        self.yvel = 0  

                        if self.jump_cooldown > 0:
                            self.jump_cooldown -= 1  


                else:
                    if self.yvel > 0 and self.rect.bottom - 10< (p.rect.top) and p.semisolid == True:   
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.jump = False
                        self.fall = False
                        self.yvel = 0
                        if self.jump_cooldown > 0:
                            self.jump_cooldown -= 1
                
        
        for m in powerups:
            if pygame.sprite.collide_rect(self, m):
                m.removed = True
                all_sprites.remove(m) 
                powerups.remove(m) 
                powerup_sfx.play()
                if self.state == 'small':
                    self.powerup_pause = True    

        for c in coins:
            if pygame.sprite.collide_rect(self,c):
                c.removed = True
                all_sprites.remove(c)
                coins.remove(c)
                coin_sfx.play()

        for e in enemies:
            if pygame.sprite.collide_rect(self,e):
                if yvel > 0:
                    if e.ID == 1:
                        if e.state != 'dead':
                            kick_sfx.play()          
                            if self.state == 'small':
                                self.yvel = 0
                                jump = False
                                if not up:
                                    self.yvel -= self.jump_speed 

                            else:
                                self.yvel = 0
                                jump = False
                                if not up:
                                    self.yvel -= self.jump_speed 
                        if e.state == 'normal':
                            e.state = 'smashed'
                        elif e.state == 'smashed':
                            e.state = 'dead'


                    if e.ID == 2:
                        if e.state == 'chase':
                            kick_sfx.play()          
                            if self.state == 'small':
                                self.yvel = 0
                                jump = False
                                self.yvel -= self.jump_speed 
                                e.state = 'dead'
                            else:
                                self.yvel = 0
                                jump = False
                                self.yvel -= self.jump_speed 
                                e.state = 'dead'

   