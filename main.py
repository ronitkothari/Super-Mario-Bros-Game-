import pygame, time, random
from levels import *
from platform import *
from constants import *
from camera import *
from player import *
from bg import * 
from sound import *
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
caption = pygame.display.set_caption('Super Mario World by Richard C')

def main():
	global left
	global right
	global down
	global up 
	global run
	global all_sprites
	global total_level_width
	global total_level_height
	global pause

	camera = Camera(complex_camera, total_level_width, total_level_height)

	running = True

	build_level()
	music(1)

	player = Player(TILESIZE,total_level_height - TILESIZE)
	all_sprites.add(player)

	while running:
		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:   
				up = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				down = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				left = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				right = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
				run = True	
			if event.type == pygame.KEYDOWN and event.key == pygame.K_p and player.powerup_pause == False:

				if pause == False:
					pygame.mixer.music.pause()
					pygame.mixer.stop()
					pause_sfx.play()
					pause = True	

				else:
					pause = False
					pause_sfx.play()
					pygame.mixer.music.unpause()	

			if event.type == pygame.KEYUP and event.key == pygame.K_UP:
				up = False
			if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
				down = False
			if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
				right = False
			if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
				left = False
			if event.type == pygame.KEYUP and event.key == pygame.K_z:
				run = False
  
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False

		
		CLOCK.tick(FPS)
		if level == 1:
			screen.fill(LEVEL_BLUE)

		if pause == False:
			player.update(up, down, left, right, run, platforms)
			camera.update(player,player.crouch)

			if player.powerup_pause == False:   	    
				for p in platforms:
					p.update(player.rect.x)
				for b in backgrounds:
					b.update(b.rect.x,b.rect.y,player.xvel,camera.state.x)
				for m in powerups:
					if m.move == True:
						m.update(player.rect.x)
				for e in enemies:
					e.update(player.rect.x)
		for x in all_sprites:
			if x.onscreen == True:
				screen.blit(x.image, camera.apply(x))
		    
		pygame.display.flip()



	pygame.quit()
        	

main()
