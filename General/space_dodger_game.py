import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Space Dodger")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Asteroids
asteroidImg = pygame.image.load('asteroid.png')
asteroidX = random.randint(0, screen_width - 64)
asteroidY = -64
asteroidY_change = 5

# Background
background = pygame.image.load('space_background.jpg')

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def asteroid(x, y):
    screen.blit(asteroidImg, (x, y))

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(background, (0, 0))  # Draw the background image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update player position
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= screen_width - 64:
        playerX = screen_width - 64

    # Update asteroid position
    asteroidY += asteroidY_change

    # Collision detection
    if playerY < asteroidY + 64 and (playerX < asteroidX + 64 and playerX + 64 > asteroidX):
        asteroidY = 2000
        game_over_text()
        running = False

    # Respawn asteroid
    if asteroidY > screen_height:
        asteroidY = -64
        asteroidX = random.randint(0, screen_width - 64)
        score_value += 1

    player(playerX, playerY)
    asteroid(asteroidX, asteroidY)
    show_score(textX, textY)

    pygame.display.update()
