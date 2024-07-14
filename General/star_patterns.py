import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Star Pattern")

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.speed(0)

# List of colors
colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan"]

# Function to draw a star
def draw_star(size, color):
    star_turtle.color(color)
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
        star_turtle.forward(size)
        star_turtle.left(72)

# Draw multiple stars
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(20, 100)
    color = random.choice(colors)
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    draw_star(size, color)

# Hide the turtle
star_turtle.hideturtle()

# Keep the window open
turtle.done()
