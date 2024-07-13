import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Define the player object
player_width = 100
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 10

# Define the falling object
object_width = 20
object_height = 20
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height
object_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 55)

# Game loop
running = True
clock = pygame.time.Clock()

def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the object
    object_y += object_speed

    # Check if the object has fallen off the screen
    if object_y > screen_height:
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)
        score -= 1  # Deduct score if object falls off

    # Check for collision
    if (object_y + object_height > player_y and
        object_x > player_x and
        object_x < player_x + player_width):
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)
        score += 1

    # Fill the screen with white
    screen.fill(white)

    # Draw the player
    pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])

    # Draw the object
    pygame.draw.rect(screen, red, [object_x, object_y, object_width, object_height])

    # Show the score
    show_score(10, 10)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)

pygame.quit()
