import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")

# Create a turtle named 'fractal'
fractal = turtle.Turtle()
fractal.color("white")
fractal.speed(0)
fractal.hideturtle()

# Function to draw a fractal tree
def draw_branch(branch_length, angle, depth, color):
    if depth == 0:
        return
    
    fractal.color(color)
    fractal.forward(branch_length)
    fractal.left(angle)
    
    draw_branch(branch_length * 0.67, angle, depth - 1, color)
    
    fractal.right(2 * angle)
    
    draw_branch(branch_length * 0.67, angle, depth - 1, color)
    
    fractal.left(angle)
    fractal.backward(branch_length)

# Function to draw the fractal tree
def draw_fractal_tree():
    fractal.penup()
    fractal.goto(0, -250)
    fractal.pendown()
    fractal.left(90)
    
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    
    draw_branch(100, 30, 7, colors[0])

# Draw the fractal tree
draw_fractal_tree()

# Hide the turtle and display the window
turtle.done()
