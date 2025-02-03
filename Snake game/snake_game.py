import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Game window settings
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and food
snake_block = 20
snake_speed = 15
clock = pygame.time.Clock()

def game_loop():
    game_over = False
    x, y = width // 2, height // 2
    dx, dy = 0, 0
    food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
    snake_body = []
    snake_length = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != snake_block:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT and dx != -snake_block:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP and dy != snake_block:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN and dy != -snake_block:
                    dx, dy = 0, snake_block

        # Boundary check
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        x += dx
        y += dy
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check self-collision
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(window, green, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        # Eat food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()