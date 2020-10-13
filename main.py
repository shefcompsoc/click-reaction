import random

import pygame

# Constants
SCREEN_SIZE = (800, 600)
BACKGROUND_COLOR = (70, 70, 70)
FOREGROUND_COLOR = (20, 200, 90)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
RADIUS = 20
INITIAL_TIME_LIMIT = 2000

pygame.init()  # Initialises all the standard pygame modules

FONT = pygame.font.SysFont("", 40)


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
    game_over = False
    score = 0

    running = True  # Stores whether the game is running or not

    # Main game loop
    while running:
        for event in pygame.event.get():  # Loop through events
            if event.type == pygame.QUIT:
                running = False  # Game loop is no longer running
                break  # Break the for loop only
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if distance(target_center, event.pos) <= RADIUS:
                    target_center = random_target_center()
                    time_elapsed = 0
                    time_limit *= 0.99  # Reduces time limit by 1% each time
                    score += 1
            elif event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    time_limit = INITIAL_TIME_LIMIT
                    time_elapsed = 0
                    game_over = False
                    score = 0
                    target_center = random_target_center()
        if running:
            display.fill(BACKGROUND_COLOR)

            millis = clock.tick()  # Get number of milliseconds since last call
            time_elapsed += millis
            if time_elapsed >= time_limit:  # Time limit has been exceeded
                target_color = RED
                game_over = True
            else:
                target_color = FOREGROUND_COLOR
            # Draw the target
            pygame.draw.circle(display, target_color, target_center, RADIUS)

            # Drawing the score
            text = "Score: " + str(score)  # Need to convert int to str
            text_surface = FONT.render(text, True, WHITE)  # Render the text
            display.blit(text_surface, (0, 0))  # Blit the text onto the display

            pygame.display.update()
    # Unload all pygame modules
    # Makes it IDLE-friendly
    pygame.quit()


main()
