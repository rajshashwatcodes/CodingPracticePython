import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Fractal Tree")
screen.bgcolor("black")

# Create the turtle
tree_turtle = turtle.Turtle()
tree_turtle.color("green")
tree_turtle.speed(0)  # Fastest drawing speed
tree_turtle.hideturtle()
tree_turtle.left(90)  # Point the turtle upwards
tree_turtle.penup()
tree_turtle.goto(0, -250)  # Move turtle to starting position
tree_turtle.pendown()

def draw_branch(t, branch_length, angle, depth):
    if depth == 0:
        return
    # Draw the current branch
    t.forward(branch_length)
    # Draw the left subtree
    t.left(angle)
    draw_branch(t, branch_length * 0.7, angle, depth - 1)
    # Draw the right subtree
    t.right(2 * angle)
    draw_branch(t, branch_length * 0.7, angle, depth - 1)
    # Go back to the previous state
    t.left(angle)
    t.backward(branch_length)

def draw_fractal_tree(t, initial_length, angle, depth):
    draw_branch(t, initial_length, angle, depth)

# Draw the fractal tree
initial_branch_length = 100
branch_angle = 30
tree_depth = 5

draw_fractal_tree(tree_turtle, initial_branch_length, branch_angle, tree_depth)

# Keep the window open until clicked
screen.exitonclick()
