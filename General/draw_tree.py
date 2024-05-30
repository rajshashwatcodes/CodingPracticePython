import turtle
import random

def draw_tree(branch_length, t):
    if branch_length > 5:
        # Choose a color based on branch length
        if branch_length < 20:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branch_length)
        angle = random.randint(15, 45)
        length_factor = random.uniform(0.6, 0.8)

        # Draw the right branch
        t.right(angle)
        draw_tree(branch_length * length_factor, t)
        
        # Draw the left branch
        t.left(2 * angle)
        draw_tree(branch_length * length_factor, t)
        
        # Go back to the original position
        t.right(angle)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")

    draw_tree(100, t)
    turtle.done()

if __name__ == "__main__":
    main()
