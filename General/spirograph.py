import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Spirograph Pattern")

# Create a turtle
spiro = turtle.Turtle()
spiro.speed(0)  # Fastest speed
spiro.width(2)

# Define colors for the spirograph
colors = ["red", "blue", "green", "orange", "purple", "pink"]

# Function to draw a spirograph
def draw_spirograph(R, r, d):
    angle = 0
    while angle < 360:
        theta = math.radians(angle)
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) / r * theta)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) / r * theta)
        spiro.goto(x, y)
        spiro.color(colors[int(angle / 60) % len(colors)])
        angle += 1

# Main drawing loop
spiro.penup()
spiro.goto(0, 0)
spiro.pendown()

R = 125  # Large circle radius
r = 75   # Small circle radius
d = 125  # Pen distance from center of small circle

draw_spirograph(R, r, d)

# Hide the turtle and display the window
spiro.hideturtle()
turtle.done()
