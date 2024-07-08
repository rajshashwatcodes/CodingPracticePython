import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Colors
black = (0, 0, 0)

# Ball properties
ball_radius = 20
ball_color = [random.randint(0, 255) for _ in range(3)]
ball_position = [random.randint(ball_radius, width - ball_radius), random.randint(ball_radius, height - ball_radius)]
ball_velocity = [random.choice([-4, 4]), random.choice([-4, 4])]

# Function to change ball color
def change_color():
    return [random.randint(0, 255) for _ in range(3)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_velocity[0] = -ball_velocity[0]
                ball_velocity[1] = -ball_velocity[1]

    # Move the ball
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # Bounce the ball off the walls
    if ball_position[0] <= ball_radius or ball_position[0] >= width - ball_radius:
        ball_velocity[0] = -ball_velocity[0]
        ball_color = change_color()
    if ball_position[1] <= ball_radius or ball_position[1] >= height - ball_radius:
        ball_velocity[1] = -ball_velocity[1]
        ball_color = change_color()

    # Clear the screen
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
