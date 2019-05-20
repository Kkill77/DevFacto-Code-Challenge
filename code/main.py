import pygame
import sys
from menu_screen import menuScreen
from beast_profile import profileScreen
from Beast import Beast
# setting up pygame
pygame.init()

# initializing display and clock
pygame.display.set_caption("Code Challenge")
clock = pygame.time.Clock()

quit = False

# Initializing the arrays of beasts
myBeasts = []
otherBeasts = []

def readFile():
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
            tempBeast.info = char[6]
            tempBeast.med = char[7]
            tempBeast.image = char[8].strip('\n')
            if (counter == 2):
                myBeasts.append(tempBeast)
            else:
                otherBeasts.append(tempBeast)

readFile()

# main game loop
def game_loop(quit):
    while not quit:
        # handling quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        # default run state is the menu screen
        gameState = menuScreen(None)
        if gameState == "quit":
            quit = True
        elif gameState == "myBeast" and myBeasts:
            quit = profileScreen(myBeasts, True)
        elif gameState == "otherBeast" and otherBeasts:
            quit = profileScreen(otherBeasts, False)
        # updating display and establishing FPS
        pygame.display.update()
        clock.tick(60)

# calling game loop
game_loop(quit)

# quitting appropriately when done playing
pygame.quit()
sys.exit()