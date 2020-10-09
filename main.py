import pygame

# Constants
SCREEN_SIZE = (800, 600)
BACKGROUND_COLOR = (70, 70, 70)
FOREGROUND_COLOR = (20, 200, 90)
RADIUS = 20

pygame.init()  # Initialises all the standard pygame modules


def distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5


def main():
    # Set the size of the display, and get the display surface
    display = pygame.display.set_mode(SCREEN_SIZE)
    target_center = (200, 200)  # Coords for the center of the circle

    running = True  # Stores whether the game is running or not

    # Main game loop
    while running:
        for event in pygame.event.get():  # Loop through events
            if event.type == pygame.QUIT:
                running = False  # Game loop is no longer running
                break  # Break the for loop only
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if distance(target_center, event.pos) <= RADIUS:
                    print("Mouse clicked")
        if running:
            display.fill(BACKGROUND_COLOR)
            pygame.draw.circle(display, FOREGROUND_COLOR, target_center, RADIUS)
            pygame.display.update()
    # Unload all pygame modules
    # Makes it IDLE-friendly
    pygame.quit()


main()
