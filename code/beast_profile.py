# Importing the appropriate files and libraries
import pygame
import os
from util import displayText, button

# Declaring global variables
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

# Defining useful pygame variables
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
button_size = int((display_width / display_height) * 25)

def checkAppoint(mySet, current):
	'''
	The checkAppoint function sees if the new appointment conflicts with another appointment date.
	This function takes in two arguments.
	mySet: This is the set of beats currently in use.
	current: This is index of the currently selected beast.
	This function returns true if a conflict is detected.
	'''
	for beast in mySet:
		if mySet[current].appointment == beast.appointment and mySet[current].ident != beast.ident:
			return True

def displayProfile(mySet, current, owned):
	'''
	The displayProfile function takes all the information on the current beast and displays it to the screen.
	This function takes in three arguments.
	mySet: This is the set of beats currently in use.
	current: This is index of the currently selected beast.
	owned: This is a boolean value that says if the set is owned or not.
	This function does not return anything.
	'''
	# Setting the screen initialy black.
	gameDisplay.fill(black)
	# Displaying all the info...
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
	# Only owned beasts can have an appointment date set.
	if owned:
		displayText(mySet[current].appointment, '../fonts/Antonio-Bold.ttf', text_size, display_width - 175, display_height - button_size - 200,
                 	white, 0)
	# Loading, scaling, and displaying the profile picture of the beast.
	imagePath = os.path.join('../images/', mySet[current].image)
	profilePic = pygame.image.load(imagePath).convert()
	profilePic = pygame.transform.scale(profilePic, (700, 350))
	gameDisplay.blit(profilePic, (10, 10))

def adoption(mySet):
	'''
	The adoption function makes a button appear on the profile of not owned beasts that if clicked adopts that beast.
	This function takes in one argument.
	mySet: This is the set of beats currently in use.
	This function returns the current state of the button (adopted == True, else == None).
	'''
	adopt_state = button("Adopt", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width - 175, display_height - button_size - 100, 50, True)
	return adopt_state

def appointment(mySet, current):
	'''
	The appointment function creates a button on the proflie of owned beasts that if clicked allows the user to enter an appointment date in the terminal.
	This function takes in two arguments.
	mySet: This is the set of beats currently in use.
	current: This is index of the currently selected beast.
	This function does not return anything.
	'''
	# Creating button.
	appoint_state = button("Appointment", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width - 175, display_height - button_size - 100, 50, True)
	# Checking if button is pressed.
	if appoint_state:
		# Saving previous appointment date incase of conflict.
		previousAppoint = mySet[current].appointment
		date = input("Please enter an appointment date: ")
		mySet[current].appointment = date
		# If there is a conflict of dates then the previous appointment date is reset.
		if checkAppoint(mySet, current):
			mySet[current].appointment = previousAppoint

def profileScreen(mySet, owned):
	'''
	The profileScreen function manages the states of this page.
	This is done by creating buttons that allow the user see the profile of the next or previous beast.
	This function also has a return button that lets the user go back to the menu.
	This function takes in two arguments.
	mySet: This is the set of beats currently in use.
	owned: This is a boolean value that says if the set is owned or not.
	This function returns the ID of the adopted beast in order to add it to the owned beast set.
	'''
	# Setting local variables
	current = 0
	adopt_state = None
	play = True
	while play:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
		# Creating the buttons
		return_state = button("Return", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 2, display_height - button_size - 100, 50, True)
		left_state = button("Previous", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 18, display_height - button_size - 100, 50, True)
		right_state = button("Next", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred, display_width / 5, display_height - button_size - 100, 50, True)
		pygame.display.update()
		# Returning the state selected
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