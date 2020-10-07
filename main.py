import pygame

# Constants
SCREEN_SIZE = (800, 600)

pygame.init()  # Initialises all the standard pygame modules


def main():
    # Set the size of the display, and get the display surface
    display = pygame.display.set_mode(SCREEN_SIZE)

    running = True  # Stores whether the game is running or not

    # Main game loop
    while running:
        for event in pygame.event.get():  # Loop through events
            if event.type == pygame.QUIT:
                running = False  # Game loop is no longer running
                break  # Break the for loop only
    # Unload all pygame modules
    # Makes it IDLE-friendly
    pygame.quit()


main()
