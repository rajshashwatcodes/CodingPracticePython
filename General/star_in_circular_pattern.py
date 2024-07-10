import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.width(2)
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
        star_turtle.forward(size)
        star_turtle.right(72 - 144)

# Draw multiple stars
for i in range(30):
    star_turtle.color(colors[i % len(colors)])
    draw_star(100)
    star_turtle.penup()
    star_turtle.goto(0, 0)
    star_turtle.pendown()
    star_turtle.right(12)

# Hide the turtle
star_turtle.hideturtle()

# Keep the window open
turtle.done()
