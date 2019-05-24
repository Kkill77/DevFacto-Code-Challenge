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
text_size = 75


clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
button_size = int((display_width / display_height) * 25)

def checkAppoint(mySet, current):
	for beast in mySet:
		if mySet[current].appointment == beast.appointment and mySet[current].ident != beast.ident:
			return True

def displayProfile(mySet, current, owned):
	gameDisplay.fill(black)
	displayText(mySet[current].name, '../fonts/Antonio-Bold.ttf', text_size, display_width / 8, 400,
                 white, 0)
	displayText(mySet[current].age, '../fonts/Antonio-Bold.ttf', text_size, display_width / 8, 550,
                 white, 0)
	displayText(mySet[current].sex, '../fonts/Antonio-Bold.ttf', text_size, display_width / 8, 700,
                 white, 0)
	displayText(mySet[current].species, '../fonts/Antonio-Bold.ttf', text_size, display_width / 2 + 200, 100,
                 white, 0)
	displayText(mySet[current].bio, '../fonts/Antonio-Bold.ttf', text_size, display_width / 2 + 200, 550,
                 white, 0)
	displayText(mySet[current].med, '../fonts/Antonio-Bold.ttf', text_size, display_width / 2 + 200, 250,
                 white, 0)
	if owned:
		displayText(mySet[current].appointment, '../fonts/Antonio-Bold.ttf', text_size, display_width - 175, display_height - button_size - 200,
                 	white, 0)
	imagePath = os.path.join('../images/', mySet[current].image)
	profilePic = pygame.image.load(imagePath).convert()
	profilePic = pygame.transform.scale(profilePic, (700, 350))
	gameDisplay.blit(profilePic, (10, 10))

def adoption(mySet):
	adopt_state = button("Adopt", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width - 175, display_height - button_size - 100, 50, True)
	return adopt_state

def appointment(mySet, current):
	appoint_state = button("Appointment", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width - 175, display_height - button_size - 100, 50, True)
	if appoint_state:
		previousAppoint = mySet[current].appointment
		date = input("Please enter an appointment date: ")
		mySet[current].appointment = date
		if checkAppoint(mySet, current):
			mySet[current].appointment = previousAppoint

def profileScreen(mySet, owned):
	current = 0
	adopt_state = None
	play = True
	while play:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
		# creating the buttons
		return_state = button("Return", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 2, display_height - button_size - 100, 50, True)
		left_state = button("Previous", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 18, display_height - button_size - 100, 50, True)
		right_state = button("Next", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 5, display_height - button_size - 100, 50, True)
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
		displayProfile(mySet, current, owned)
		if not owned:
			adopt_state = adoption(mySet)
			if adopt_state:
				play = False
		else:
			appointment(mySet, current)

	if adopt_state:
		return mySet[current].ident