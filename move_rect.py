import pygame, sys

def moving_rect():
	global x1_speed, y1_speed, x2_speed, y2_speed

	#rect_1
	move_rect1.x+= x1_speed
	move_rect1.y+= y1_speed

	#rect_2
	move_rect2.x+= x2_speed
	move_rect2.y+= y2_speed

	#border collision for rect_1
	if move_rect1.right>= screen_width or move_rect1.left<= 0:
		x1_speed*= -1 
	if move_rect1.bottom>= screen_height or move_rect1.top<= 0:
		y1_speed*= -1

	#border collision for rect_2
	if move_rect2.right>= screen_width or move_rect2.left<= 0:
		x2_speed*= -1 
	if move_rect2.bottom>= screen_height or move_rect2.top<= 0:
		y2_speed*= -1

	#rect_1 collision with rect_2
	collision_tolarance = 10
	if move_rect1.colliderect(move_rect2):
		if abs(move_rect2.top- move_rect1.bottom)< collision_tolarance and y1_speed > 0:
			y1_speed*= -1
		if abs(move_rect2.bottom- move_rect1.top)< collision_tolarance and y1_speed < 0:
			y1_speed*= -1
		if abs(move_rect2.right- move_rect1.left)< collision_tolarance and x1_speed < 0:
			x1_speed*= -1
		if abs(move_rect2.left- move_rect1.right)< collision_tolarance and x1_speed > 0:
			x1_speed*= -1


	#rect_2 collision with rect_1
	collision_tolarance = 10
	if move_rect2.colliderect(move_rect1):
		if abs(move_rect1.top- move_rect2.bottom)< collision_tolarance and y2_speed > 0:
			y2_speed*= -1
		if abs(move_rect1.bottom- move_rect2.top)< collision_tolarance and y2_speed < 0:
			y2_speed*= -1
		if abs(move_rect1.right- move_rect2.left)< collision_tolarance and x2_speed < 0:
			x2_speed*= -1
		if abs(move_rect1.left- move_rect2.right)< collision_tolarance and x2_speed > 0:
			x2_speed*= -1

	pygame.draw.rect(screen, (255, 255, 153), move_rect1)
	pygame.draw.rect(screen, (000, 128, 128), move_rect2)

pygame.init()
clock= pygame.time.Clock()
screen_width, screen_height= 600, 600
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Moving rectangles | Bhathi')
pygame.display.set_icon(pygame.image.load('Bicon.png'))

#define rect_1
move_rect1= pygame.Rect(20, 20, 20, 20)
x1_speed, y1_speed= 9, 6

#define rect_2
move_rect2= pygame.Rect(20, 20, 40, 40)
x2_speed, y2_speed= 2, 3


while True:
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((000, 000, 000))
	moving_rect( )
	pygame.display.flip()
	clock.tick(60)