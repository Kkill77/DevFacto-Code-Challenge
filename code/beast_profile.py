import pygame
import os
from util import displayText, button

# declaring global variables needed
white = (255, 255, 255)
hovergreen = (140, 240, 100)
green = (140, 200, 100)
hoverred = (255, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
hoverblue = (0, 0, 255)
black = (0, 0, 0)
display_width, display_height = 2000, 1000
current = 0

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
button_size = int((display_width / display_height) * 25)

def displayProfile(mySet):
	gameDisplay.fill(black)
	displayText(mySet[current].name, '../fonts/Antonio-Bold.ttf', 100, display_width / 20, (display_height / 10),
                 white, 0)
	displayText(mySet[current].species, '../fonts/Antonio-Bold.ttf', 100, display_width / 2, (display_height / 3),
                 white, 0)
	displayText(mySet[current].age, '../fonts/Antonio-Bold.ttf', 100, display_width / 5, (display_height / 10),
                 white, 0)
	displayText(mySet[current].sex, '../fonts/Antonio-Bold.ttf', 100, display_width / 3, (display_height / 10),
                 white, 0)
	displayText(mySet[current].info, '../fonts/Antonio-Bold.ttf', 100, display_width / 2, (display_height / 2),
                 white, 0)
	displayText(mySet[current].med, '../fonts/Antonio-Bold.ttf', 100, display_width / 2, (display_height / 1.5),
                 white, 0)
	imagePath = os.path.join('../images/', mySet[current].image)
	profilePic = pygame.image.load(imagePath).convert()
	profilePic = pygame.transform.scale(profilePic, (400, 200))
	gameDisplay.blit(profilePic, (display_width / 1.5, display_height / 20))

def profileScreen(mySet, owned):
	global current
	play = True
	while play:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
		# creating the buttons
		return_state = button("Return", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 2, display_height - button_size - 100, 50, True)
		left_state = button("Previous", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 18, display_height / 5, 50, True)
		right_state = button("Next", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 5, display_height / 5, 50, True)
		pygame.display.update()
		# returning the state selected
		if return_state != None:
			play = False
		elif left_state != None:
			current -= 1
			if current < 0:
				current = 0
		elif right_state != None:
			current += 1
			if current > len(mySet) - 1:
				current = len(mySet) - 1
		displayProfile(mySet)