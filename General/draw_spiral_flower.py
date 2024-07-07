import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black')

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Function to draw a spiral flower
def draw_spiral_flower():
    n = 72  # Number of color changes
    h = 0   # Starting hue
    for i in range(360):
        color = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        pen.pencolor(color)
        pen.circle(100, steps=4)  # Drawing a square as a petal
        pen.left(10)              # Turning the turtle to form a spiral
        h += 1/n                  # Increment hue for color change

# Draw the spiral flower
draw_spiral_flower()

# Hide the turtle and finish
pen.hideturtle()
turtle.done()
