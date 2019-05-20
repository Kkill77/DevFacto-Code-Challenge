import pygame
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

# initializing menu screen start up
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

background = pygame.image.load('../images/scary_sully.png')
background = pygame.transform.scale(background, (1000, 500))
button_size = int((display_width / display_height) * 25) 


def menuScreen(state):
    # The menuScreen function takes in the paramater 'state' and returns the 
    # next selected state that the user wishes to play. It is responsible for
    # displaying the buttons to the screen and navigating between the states.
    gameDisplay.fill(black)
    gameDisplay.blit(background, (500, 300))
    displayText("BeastKeeper", '../fonts/Antonio-Bold.ttf', 200, display_width / 2, (display_height / 5),
                 white, 0)

    # creating the buttons
    my_state = button("My Beasts", '../fonts/Antonio-Regular.ttf', button_size, white, green, 
                        hovergreen, display_width / 5, display_height - button_size, 50, "myBeast")
    other_state = button("Other Beasts", '../fonts/Antonio-Regular.ttf', button_size, white, blue,
                             hoverblue, display_width / 2, display_height - button_size, 50, 
                             "otherBeast")
    quit_state = button("Quit", '../fonts/Antonio-Regular.ttf', button_size, white, red, hoverred,
                        (4*display_width) / 5, display_height - button_size, 50, "quit")

    # returning the state selected
    if my_state != state:
        return my_state
    elif quit_state != state:
        return quit_state
    elif other_state != state:
        return other_state