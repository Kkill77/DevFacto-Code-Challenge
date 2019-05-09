import pygame
import sys
from menu_screen import menuScreen
from my_beast import myBeastScreen
from other_beast import otherBeastScreen
# setting up pygame
pygame.init()

# initializing display and clock
pygame.display.set_caption("Code Challenge")
clock = pygame.time.Clock()

quit = False

# main game loop
def game_loop(quit):
    while not quit:
        # handling quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # We can add an "Are you sure you would like to quit" window later...
                quit = True
        # default run state is the menu screen
        gameState = menuScreen(None)

        if gameState == "quit":
            quit = True
        elif gameState == "myBeast":
            # running tutorial screen
            quit = myBeastScreen()
        elif gameState == "otherBeast":
            # running play game
            quit = otherBeastScreen()
        # updating display and establishing FPS
        pygame.display.update()
        clock.tick(60)

# calling game loop
game_loop(quit)

# quitting appropriately when done playing
pygame.quit()
sys.exit()