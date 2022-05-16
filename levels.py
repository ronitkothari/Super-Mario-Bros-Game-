from constants import *
from platform import *
from powerup import *
from bg import *
from enemies import *

level_1 = [ 
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000ccccc0c000c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000c00000c000c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000ccccc0c000c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000c00000c000c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000c00000c000c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000c00000ccccc0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "222222222222222222222230000122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222",
            "555555555555555555555560000455555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",


            ]

level_x = 0
level_y = 0
total_level_width  = len(level_1[0])* TILESIZE
total_level_height = len(level_1)* TILESIZE

"""
0 = nothing
1 = Top Left Corner
2 = Top Middle
3 = Top Right Corner
4 = Middle Left
5 = Middle Middle
6 = Middle Right
7 = Bottom Left Corner
8 = Bottom Middle
9 = Bottom Right Corner

a = Still block
b = cloud
c = coin
d = question block mushroom
e = bush 1

! = Rex
@ = Mole

"""

def build_level():
      global level_x
      global level_y
      global platforms

      bgnumber = round(total_level_width / S_WIDTH)
      backgroundx = 0
      backgroundy = 0
      for b in range(bgnumber):
            b = Background(backgroundx,backgroundy,S_WIDTH * SCALE,S_HEIGHT * SCALE,'Graphics/Bg/bg1.png',1,total_level_height)
            backgroundx += S_WIDTH * SCALE
            backgroundy =  total_level_height - b.h
            b.y = backgroundy
            all_sprites.add(b)
            backgrounds.append(b)



      level_x = 0
      level_y = 0

      for row in level_1:
            for col in row:
                  if col == "1":
                        p = Platform(level_x,level_y,1,True,False)
                        platforms.append(p)
                        all_sprites.add(p)
                  if col == "2":
                        p = Platform(level_x,level_y,2,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "3":
                        p = Platform(level_x,level_y,3,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "4":
                        p = Platform(level_x,level_y,4,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "5":
                        p = Platform(level_x,level_y,5,True,False)
                        platforms.append(p)
                        all_sprites.add(p)
  
                  if col == "6":
                        p = Platform(level_x,level_y,6,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "7":
                        p = Platform(level_x,level_y,7,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "8":
                        p = Platform(level_x,level_y,8,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "9":
                        p = Platform(level_x,level_y,9,True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                  if col == "a":
                        p = Platform(level_x,level_y,'a',True,False)
                        platforms.append(p)
                        all_sprites.add(p)          

                  if col == "b":
                        p = Platform(level_x,level_y,'b',False,True)
                        platforms.append(p)
                        all_sprites.add(p)   

                  if col == "c":
                        p = Platform(level_x,level_y,'c',False,False)
                        platforms.append(p)
                        coins.append(p)
                        all_sprites.add(p)

                  if col == "d":
                        m = Powerup(level_x,level_y,'mushroom')  
                        powerups.append(m)
                        all_sprites.add(m)

                        p = Platform(level_x,level_y,'d',True,False)
                        platforms.append(p)
                        all_sprites.add(p) 

                  if col == "e":
                        p = Platform(level_x,level_y,'e',False,False)
                        platforms.append(p)
                        all_sprites.add(p)  


                  level_x += TILESIZE

            level_y += TILESIZE
            level_x = 0




      level_x = 0
      level_y = 0

      for row in level_1:
            for col in row:
                  if col == "!":
                        e = Rex(level_x,level_y,'left',1)
                        all_sprites.add(e)
                        enemies.append(e)

                  if col =="@":
                        p = Platform(level_x,level_y,'@',True,False)
                        platforms.append(p)
                        all_sprites.add(p)

                        e = Mole(level_x,level_y,'left',2)
                        all_sprites.add(e)
                        enemies.append(e)


                  level_x += TILESIZE

            level_y += TILESIZE
            level_x = 0
