import pygame
import random
import time

pygame.init()

# Set up some constants for the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

# Set up the snake
snake_position = [100, 50]
snake_speed = [20, 0]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set up the apple
apple_position = [random.randrange(1, SCREEN_WIDTH//20)*20, random.randrange(1, SCREEN_HEIGHT//20)*20]
apple_spawn = True

# Set up the score
score = 0

# Set up the level
level = 1

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed = [0, -20]
            elif event.key == pygame.K_DOWN:
                snake_speed = [0, 20]
            elif event.key == pygame.K_LEFT:
                snake_speed = [-20, 0]
            elif event.key == pygame.K_RIGHT:
                snake_speed = [20, 0]

    # Update the snake position
    snake_position[0] += snake_speed[0]
    snake_position[1] += snake_speed[1]

    # Update the snake body
    snake_body.insert(0, list(snake_position))

    # Check if the snake has eaten the apple
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 1
        level = score // 10 + 1
        apple_spawn = False
    else:
        snake_body.pop()

    # Check if the snake has collided with the screen borders or itself
    if (snake_position[0] < 0 or snake_position[0] >= SCREEN_WIDTH or
            snake_position[1] < 0 or snake_position[1] >= SCREEN_HEIGHT):
        running = False
    elif snake_position in snake_body[1:]:
        running = False

    # Spawn a new apple if necessary
    if not apple_spawn:
        apple_position = [random.randrange(1, SCREEN_WIDTH//20)*20, random.randrange(1, SCREEN_HEIGHT//20)*20]
    apple_spawn = True

    # Draw the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, PURPLE, pygame.Rect(segment[0], segment[1], 20, 20))

    # Draw the apple
    pygame.draw.rect(screen, RED, pygame.Rect(apple_position[0], apple_position[1], 20, 20))

    # Update the display
    pygame.display.flip()

    # Pause for a bit
    time.sleep(0.1)

pygame.quit()