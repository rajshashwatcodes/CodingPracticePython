import turtle

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("Drawing Application")
screen.bgcolor("white")

# Initialize the turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

# Function to move the turtle forward
def move_forward():
    pen.forward(10)

# Function to move the turtle backward
def move_backward():
    pen.backward(10)

# Function to turn the turtle left
def turn_left():
    pen.left(15)

# Function to turn the turtle right
def turn_right():
    pen.right(15)

# Function to clear the screen
def clear_screen():
    pen.clear()

# Function to change color
def change_color(color):
    pen.color(color)

# Function to change pen size
def change_pen_size(size):
    pen.pensize(size)

# Key bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")

# Color and size controls
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to set color and size using number keys
def set_color_and_size():
    for i, color in enumerate(colors):
        screen.onkey(lambda c=color: change_color(c), str(i + 1))
    for i, size in enumerate(sizes):
        screen.onkey(lambda s=size: change_pen_size(s), str(i + 1 + len(colors)))

set_color_and_size()

# Start the turtle graphics loop
turtle.mainloop()
