import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)

# Number of circles
num_circles = 36
hue = 0

# Draw the spirals
for i in range(num_circles * 10):
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    spiral.color(color)
    spiral.circle(100)
    spiral.right(10)
    hue += 1/num_circles

# Hide the turtle and display the result
spiral.hideturtle()
turtle.done()
