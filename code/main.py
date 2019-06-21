# Importing the appropriate files and libraries
import pygame
import sys
from menu_screen import menuScreen
from beast_profile import profileScreen
from Beast import Beast

# Setting up pygame
pygame.init()

# Initializing display and clock
pygame.display.set_caption("Code Challenge")
clock = pygame.time.Clock()

quit = False

# Initializing the arrays of beasts
myBeasts = []
otherBeasts = []

def readFile():
    '''
    The readFile function takes in the data.txt file and creates objects based on its values.
    This function takes in no arguments.
    This function does not return anything.
    '''
    file = open("data.txt", "r")
    counter = 0
    for line in file:
        counter += 1
        if (counter > 1):
            tempBeast = Beast(0, 0, 0, 0, 0, 0, 0, 0, 0)
            char = line.split(",")
            tempBeast.ident = char[0]
            tempBeast.name = char[1]
            tempBeast.species = char[2]
            tempBeast.age = char[3]
            tempBeast.sex = char[4]
            tempBeast.appointment = char[5]
            tempBeast.bio = char[6]
            tempBeast.med = char[7]
            tempBeast.image = char[8].strip('\n')
            if (counter == 2):
                myBeasts.append(tempBeast)
            else:
                otherBeasts.append(tempBeast)

# Reading in the file.
readFile()

def findBeast(id):
    '''
    The findBeast function finds the beast with a matching ID in the otherbeast array.
    The function adds this beast to the owned beast array and removes it from the otherbeast.
    This function takes in one argument.
    id: This is the ID of the selected beast to find.
    This function returns true if a conflict is detected.
    '''
    for beast in otherBeasts:
        if beast.ident == id:
            myBeasts.append(beast)
            otherBeasts.remove(beast)

# Main game loop
def game_loop(quit):
    while not quit:
        # Handling quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        # Default run state is the menu screen
        gameState = menuScreen(None)
        if gameState == "quit":
            quit = True
        elif gameState == "myBeast" and myBeasts:
            quit = profileScreen(myBeasts, True)
        elif gameState == "otherBeast" and otherBeasts:
            quit = profileScreen(otherBeasts, False)
            if quit != True and quit != None:
                findBeast(quit)
                quit = False
        # Updating display and establishing FPS
        pygame.display.update()
        clock.tick(60)

# Calling game loop
game_loop(quit)

# Quitting appropriately when done playing
pygame.quit()
sys.exit()
