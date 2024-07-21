import pygame
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
BALL_RADIUS = 15
PAD_WIDTH = 20
PAD_HEIGHT = 100
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PADDLE_SPEED = 10

# Ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = BALL_RADIUS
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with top and bottom walls
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.speed_y = -self.speed_y

        # Ball collision with left and right walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def draw(self):
        pygame.draw.circle(WINDOW, WHITE, (self.x, self.y), self.radius)

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PAD_WIDTH
        self.height = PAD_HEIGHT
        self.speed = 0

    def move(self):
        self.y += self.speed

        # Paddle collision with walls
        if self.y < 0:
            self.y = 0
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(WINDOW, WHITE, (self.x, self.y, self.width, self.height))

# Initialize game objects
ball = Ball()
left_paddle = Paddle(10, HEIGHT // 2 - PAD_HEIGHT // 2)
right_paddle = Paddle(WIDTH - PAD_WIDTH - 10, HEIGHT // 2 - PAD_HEIGHT // 2)

# Game loop
def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    left_paddle.speed = -PADDLE_SPEED
                if event.key == K_s:
                    left_paddle.speed = PADDLE_SPEED
                if event.key == K_UP:
                    right_paddle.speed = -PADDLE_SPEED
                if event.key == K_DOWN:
                    right_paddle.speed = PADDLE_SPEED
            if event.type == KEYUP:
                if event.key in (K_w, K_s):
                    left_paddle.speed = 0
                if event.key in (K_UP, K_DOWN):
                    right_paddle.speed = 0

        ball.move()
        left_paddle.move()
        right_paddle.move()

        # Ball collision with paddles
        if ball.x - ball.radius < left_paddle.x + left_paddle.width and \
           left_paddle.y < ball.y < left_paddle.y + left_paddle.height:
            ball.speed_x = -ball.speed_x

        if ball.x + ball.radius > right_paddle.x and \
           right_paddle.y < ball.y < right_paddle.y + right_paddle.height:
            ball.speed_x = -ball.speed_x

        # Drawing
        WINDOW.fill(BLACK)
        ball.draw()
        left_paddle.draw()
        right_paddle.draw()
        pygame.display.update()

        # Frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
