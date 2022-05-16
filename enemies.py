import pygame
from constants import *
from sound import *
from platform import *
import random


class Rex(pygame.sprite.Sprite):
	def __init__(self,x,y,direction,ID):
		pygame.sprite.Sprite.__init__(self)

		self.walk_frames = []
		self.smashed_frames = []
		self.dead_frames = []

		self.walk_frames.append(pygame.image.load('Graphics/Enemies/Rex/rex_walk_1.png').convert_alpha())
		self.walk_frames.append(pygame.image.load('Graphics/Enemies/Rex/rex_walk_2.png').convert_alpha())
		self.smashed_frames.append(pygame.image.load('Graphics/Enemies/Rex/rex_smashed_1.png').convert_alpha())
		self.smashed_frames.append(pygame.image.load('Graphics/Enemies/Rex/rex_smashed_2.png').convert_alpha())
		self.dead_frames.append(pygame.image.load('Graphics/Enemies/Rex/rex_dead.png').convert_alpha())


		self.walk_frames[0] = pygame.transform.scale(self.walk_frames[0],(19 * SCALE, 32 * SCALE))
		self.walk_frames[1] = pygame.transform.scale(self.walk_frames[1],(20 * SCALE, 31 * SCALE))

		self.smashed_frames[0] = pygame.transform.scale(self.smashed_frames[0],(16 * SCALE, 16 * SCALE))
		self.smashed_frames[1] = pygame.transform.scale(self.smashed_frames[1],(16 * SCALE, 15 * SCALE))

		self.dead_frames[0] = pygame.transform.scale(self.dead_frames[0],(16 * SCALE, 8 * SCALE))

		self.image = self.walk_frames[0]
		self.rect = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y

		self.direction = direction
		self.state = 'normal'

		self.xvel = 0
		self.yvel = 0
		self.onGround = True
		self.deadtimer = 50
		self.ID = ID
		self.onscreen = False

		if self.direction == 'left':
			self.image = pygame.transform.flip(self.image,True,False)

	def update(self,playerx):

		if self.rect.y > 800:
			for e in enemies:
				if e.rect.y > 800:
					all_sprites.remove(e)
					enemies.remove(e)

		if self.rect.x > playerx and self.rect.x - playerx > S_WIDTH + 100 or self.rect.x < playerx and playerx - self.rect.x > S_WIDTH + 100:
			self.onscreen = False

		else:
			self.onscreen = True
			if self.state == 'normal':
				self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,h= 31 * SCALE, bottom=self.rect.bottom,left=self.rect.left)

			if self.state == 'smashed':
				self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,h= 15 * SCALE,left=self.rect.left,right=self.rect.right,bottom=self.rect.bottom)

			if self.state == 'dead':
				self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=14* SCALE,h= 8 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

			if not self.state == 'dead' or self.rect.x <= 0:
				if self.direction == 'left' and self.rect.x - playerx <= S_WIDTH:

					if self.state == 'normal':
						self.xvel = -2

					elif self.state == 'smashed':
						self.xvel = -3

					self.direction = 'left'

					if self.state == 'normal':
						self.frame = (self.rect.x // 20) % len(self.walk_frames)
						self.image = self.walk_frames[self.frame]

					elif self.state == 'smashed':
						self.frame = (self.rect.x // 20) % len(self.smashed_frames)
						self.image = self.smashed_frames[self.frame]


				if self.direction == 'right':

					if self.state == 'normal':
						self.xvel = 2

					elif self.state == 'smashed':
						self.xvel = 3

					self.direction = 'right'

					if self.state == 'normal':
						self.frame = (self.rect.x // 15) % len(self.walk_frames)
						self.image = self.walk_frames[self.frame]
						self.image = pygame.transform.flip(self.image,True,False)



					elif self.state == 'smashed':
						self.frame = (self.rect.x // 20) % len(self.smashed_frames)
						self.image = self.smashed_frames[self.frame]
						self.image = pygame.transform.flip(self.image,True,False)



			if not self.onGround:
				self.yvel += 1
				if self.yvel > 20:
					self.yvel = 20


			self.rect.left += self.xvel

			self.collide(self.xvel, 0, platforms)

			self.rect.top += self.yvel

			self.onGround = False;

			self.collide(0, self.yvel, platforms)


			if self.rect.x <= -30:
				for e in enemies:
					if e.rect.x <= -30:
						all_sprites.remove(e)
						enemies.remove(e)

			if self.state == 'dead':
				self.xvel = 0
				if self.direction == 'left':
					self.image = self.dead_frames[0]
				elif self.direction == 'right':
					self.image = self.dead_frames[0]
					self.image = pygame.transform.flip(self.image,True,False)

				if self.deadtimer == 0:
					for e in enemies:
						if e.ID == 1:
							if e.deadtimer == 0:
								all_sprites.remove(e)
								enemies.remove(e)
				else:
					self.deadtimer -= 1


	def collide(self,xvel,yvel,platforms):
		for p in platforms:
			if pygame.sprite.collide_rect(self, p):
				if xvel > 0:
					self.rect.right = p.rect.left
					self.direction = 'left'
					self.xvel = 0
		
				if xvel < 0:
					self.rect.left = p.rect.right
					self.direction = 'right'
					self.xvel = 0
		
				if yvel > 0:
					self.rect.bottom = p.rect.top
					self.onGround = True
					self.yvel = 0
				if yvel < 0:
					self.rect.top = p.rect.bottom
					self.yvel = 0


		for e in enemies:
			if pygame.sprite.collide_rect(self,e):
				if e.rect.x != self.rect.x and e.ID != 4 and e.ID != 2:
					if xvel > 0:
						self.rect.x -= 1
						self.direction = 'left'

					if xvel < 0:
						self.rect.x += 1
						self.direction = 'right'

class Mole(pygame.sprite.Sprite):
	def __init__(self,x,y,direction,ID):
		pygame.sprite.Sprite.__init__(self)

		self.walk_frames = []
		self.dig_frames = []
		self.jump_frames = []

		self.walk_frames.append(pygame.image.load('Graphics/Enemies/Monty Mole/mole_walk1.png').convert_alpha())
		self.walk_frames.append(pygame.image.load('Graphics/Enemies/Monty Mole/mole_walk2.png').convert_alpha())
		self.dig_frames.append(pygame.image.load('Graphics/Enemies/Monty Mole/mole_digging1.png').convert_alpha())
		self.dig_frames.append(pygame.image.load('Graphics/Enemies/Monty Mole/mole_digging2.png').convert_alpha())
		self.jump_frames.append(pygame.image.load('Graphics/Enemies/Monty Mole/mole_jump.png').convert_alpha())

		
		self.walk_frames[0] = pygame.transform.scale(self.walk_frames[0],(16 * SCALE, 16 * SCALE))
		self.walk_frames[1] = pygame.transform.scale(self.walk_frames[1],(16 * SCALE, 16 * SCALE))

		self.dig_frames[0] = pygame.transform.scale(self.dig_frames[0],(15 * SCALE, 14 * SCALE))
		self.dig_frames[1] = pygame.transform.scale(self.dig_frames[1],(15 * SCALE, 14 * SCALE))

		self.jump_frames[0] = pygame.transform.scale(self.jump_frames[0],(16 * SCALE, 16 * SCALE))

		self.image = pygame.image.load('Graphics/Enemies/Monty Mole/mole_hidden.png').convert_alpha()
		self.image = pygame.transform.scale(self.image,(16 * SCALE, 16 * SCALE))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.homex = x
		self.homey = y

		self.direction = direction
		self.state = 'dormant'

		self.xvel = 0
		self.yvel = 0
		self.speed = random.randint(4,5)
		self.acceleration = 0.5
		self.friction = 0.05
		self.onGround = False
		self.dig_timer = 10
		self.dig_frame =0
		self.openingjump = False
		self.deadjump = False
		self.deadtimer = 15
		self.soundplayed = False
		self.dig_frame_delay = 2
		self.ID = ID
		self.onscreen = False
		self.a_s = 10


	def update(self,playerx):

		if self.rect.y > 800:
			for e in enemies:
				if e.rect.y > 800:
					all_sprites.remove(e)
					enemies.remove(e)

		if self.rect.x > playerx and self.rect.x - playerx > S_WIDTH + 100 or self.rect.x < playerx and playerx - self.rect.x > S_WIDTH + 100:
			self.onscreen = False

		else:
			self.onscreen = True

		if self.state == 'chase' or self.state == 'jump' or self.state == 'dead':
			self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=16 * SCALE,h= 16 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)

		if self.state == 'dig':
			self.rect = self.image.get_rect(x=self.rect.x,y=self.rect.y,w=15* SCALE,h= 14 * SCALE,left=self.rect.left,right=self.rect.right,midbottom=self.rect.midbottom)


		if self.state == 'dormant':
			if playerx < self.rect.x and self.rect.x - playerx <= 250 or playerx > self.rect.x and playerx - self.rect.x <= 250: 
				self.state = 'dig'

			else:
				pass

		if self.state == 'dig' and not self.state == 'dormant':
			if self.dig_timer > 0:
				if self.dig_frame == 0:
					if self.dig_frame_delay > 0:
						self.dig_frame_delay -= 0.5
					else:
						self.dig_frame_delay = 2
						self.image = self.dig_frames[0]

				else:
					if self.dig_frame_delay > 0:
						self.dig_frame_delay -= 0.5
					else:
						self.dig_frame_delay = 2
						self.image = self.dig_frames[1]

				self.dig_timer -= 0.1
				if self.dig_frame == 0:
					self.dig_frame = 1

				else:
					self.dig_frame = 0

			else:
				self.dig_timer = 0
				self.state = 'jump'

		if self.state == 'jump' and not self.state == 'dormant':
			self.image = self.jump_frames[0]
			if self.openingjump == False:
				if self.soundplayed == False:
					breakblock_sfx.play()
				else:
					pass
				self.yvel -= 16
				self.openingjump = True
			if self.onGround == True:
				self.state = 'chase'

			else:
				pass


		if self.state == 'chase' and not self.state == 'dormant':
			if not self.state == 'dead':
				if self.rect.x  > playerx and self.rect.x - playerx <= S_WIDTH:
					self.frame = (self.rect.x // self.a_s) % len(self.walk_frames)
					self.image = self.walk_frames[self.frame]

					if self.xvel > 2:
						self.xvel -= self.friction
					else:
						if self.xvel > self.speed:
							self.xvel -= self.acceleration

						else:
							self.xvel = -self.speed

				elif self.rect.x  < playerx and playerx - self.rect.x <= S_WIDTH:	
					self.frame = (self.rect.x // self.a_s) % len(self.walk_frames)
					self.image = self.walk_frames[self.frame]
					self.image = pygame.transform.flip(self.image,True,False)


					if self.xvel < -2:
						self.xvel += self.friction

					else:	
						if self.xvel > self.speed:
							self.xvel += self.acceleration
						else:
							self.xvel = self.speed

		if not self.onGround and self.state == 'jump' or not self.onGround and self.state == 'chase':
			if not self.state == 'dormant':
				self.yvel += 0.6
				if self.yvel > 10:
					self.yvel = 10

		if not self.state == 'dormant':
			self.rect.left += self.xvel
			self.collide(self.xvel, 0, platforms)

			if self.deadjump == False:
				self.rect.top += self.yvel

			else:
				if self.yvel < 5:
					self.yvel += 0.5
				self.rect.y += self.yvel

			self.onGround = False;

			self.collide(0, self.yvel, platforms)

		if self.state == 'dead':
			self.image = self.walk_frames[0]
			self.image = pygame.transform.flip(self.image,False,True)
			if self.deadjump == False:
				self.yvel = -5
				self.deadjump = True

			if self.rect.y > 850:
				for e in enemies:
					if e.rect.y > 850:
						all_sprites.remove(e)
						enemies.remove(e)

	def collide(self,xvel,yvel,platforms):
		for p in platforms:
			if pygame.sprite.collide_rect(self, p):
				if xvel > 0 and self.state != 'dead':
					self.rect.right = p.rect.left
					self.direction = 'left'
					self.xvel = -5

				if xvel < 0 and self.state != 'dead':
					self.rect.left = p.rect.right
					self.direction = 'right'
					self.xvel = 5

				if yvel > 0 and self.state != 'dead':
					self.rect.bottom = p.rect.top
					self.onGround = True
					self.yvel = 0
				if yvel < 0 and self.state != 'jump' and self.state != 'dead':
					self.rect.top = p.rect.bottom
					self.yvel = 0
