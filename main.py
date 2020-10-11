import random

import pygame

# Constants
SCREEN_SIZE = (800, 600)
BACKGROUND_COLOR = (70, 70, 70)
FOREGROUND_COLOR = (20, 200, 90)
RADIUS = 20
INITIAL_TIME_LIMIT = 2000

pygame.init()  # Initialises all the standard pygame modules


def distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5


def random_target_center():
    x = random.randint(RADIUS, SCREEN_SIZE[0] - RADIUS)
    y = random.randint(RADIUS, SCREEN_SIZE[1] - RADIUS)
    return (x, y)


def main():
    # Set the size of the display, and get the display surface
    display = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()  # Allows timekeeping
    target_center = (200, 200)  # Coords for the center of the circle
    time_limit = INITIAL_TIME_LIMIT
    time_elapsed = 0

    running = True  # Stores whether the game is running or not

    # Main game loop
    while running:
        for event in pygame.event.get():  # Loop through events
            if event.type == pygame.QUIT:
                running = False  # Game loop is no longer running
                break  # Break the for loop only
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if distance(target_center, event.pos) <= RADIUS:
                    target_center = random_target_center()
                    time_elapsed = 0
        if running:
            display.fill(BACKGROUND_COLOR)

            millis = clock.tick()  # Get number of milliseconds since last call
            time_elapsed += millis
            if time_elapsed >= time_limit:
                print("Game over")
                running = False
            pygame.draw.circle(display, FOREGROUND_COLOR, target_center, RADIUS)
            pygame.display.update()
    # Unload all pygame modules
    # Makes it IDLE-friendly
    pygame.quit()


main()
