import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mandala Pattern")

# Create a turtle
mandala = turtle.Turtle()
mandala.speed(0)  # Fastest speed
mandala.width(2)
colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

# Function to draw a mandala pattern
def draw_mandala(radius):
    for i in range(6):
        mandala.color(colors[i % 6])
        mandala.circle(radius)
        mandala.right(60)

# Main drawing loop
for radius in range(50, 201, 10):
    draw_mandala(radius)
    mandala.right(10)

# Hide the turtle and display the window
mandala.hideturtle()
turtle.done()
