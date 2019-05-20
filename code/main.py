import pygame
import sys
from menu_screen import menuScreen
from my_beast import myBeastScreen
from other_beast import otherBeastScreen
from Beast import Beast
# setting up pygame
pygame.init()

# initializing display and clock
pygame.display.set_caption("Code Challenge")
clock = pygame.time.Clock()

quit = False

# Initializing the sets of beasts
mySet = []
otherSet = []

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
            tempBeast.image = char[8]
            if (counter == 2):
                mySet.append(tempBeast)
            else:
                otherSet.append(tempBeast)

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
        elif gameState == "myBeast":
            quit = myBeastScreen(mySet)
        elif gameState == "otherBeast":
            quit = otherBeastScreen(otherSet)
        # updating display and establishing FPS
        pygame.display.update()
        clock.tick(60)
        print(mySet[0].name)

# calling game loop
game_loop(quit)

# quitting appropriately when done playing
pygame.quit()
sys.exit()