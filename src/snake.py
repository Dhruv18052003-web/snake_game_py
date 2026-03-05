import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Game settings
display_width = 800
display_height = 600
block_size = 10
snake_speed = 15

# Font for displaying the score
font_style = pygame.font.SysFont(None, 25)

# Function to display the score
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], block_size, block_size])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # Generate random food position
    foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # Event handling
        while game_close == True:
            dis.fill(black)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [display_width / 6, display_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Movement controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Boundary check
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update snake's position
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, block_size, block_size])

        # Snake body mechanics
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw and update the snake
        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snake_length += 1

        # Control game speed
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()
    quit()

# Game window setup
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Start the game loop
game_loop()