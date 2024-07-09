import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Basket settings
BASKET_WIDTH = 100
BASKET_HEIGHT = 20
BASKET_SPEED = 10

# Apple settings
APPLE_SIZE = 20
APPLE_FALL_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Apples")

# Load basket image
basket_image = pygame.image.load("basket.png")
basket_image = pygame.transform.scale(basket_image, (BASKET_WIDTH, BASKET_HEIGHT))

# Load apple image
apple_image = pygame.image.load("apple.png")
apple_image = pygame.transform.scale(apple_image, (APPLE_SIZE, APPLE_SIZE))

# Basket position
basket_x = SCREEN_WIDTH // 2 - BASKET_WIDTH // 2
basket_y = SCREEN_HEIGHT - BASKET_HEIGHT - 10

# Apple position
apple_x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
apple_y = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= BASKET_SPEED
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - BASKET_WIDTH:
        basket_x += BASKET_SPEED

    # Move the apple
    apple_y += APPLE_FALL_SPEED

    # Check for collision
    if (apple_y + APPLE_SIZE > basket_y and
        apple_x + APPLE_SIZE > basket_x and
        apple_x < basket_x + BASKET_WIDTH):
        score += 1
        apple_x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
        apple_y = 0

    # Reset apple if it falls below the screen
    if apple_y > SCREEN_HEIGHT:
        apple_x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
        apple_y = 0

    # Draw basket
    screen.blit(basket_image, (basket_x, basket_y))

    # Draw apple
    screen.blit(apple_image, (apple_x, apple_y))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
