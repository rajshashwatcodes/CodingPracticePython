import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_house():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    house = turtle.Turtle()
    house.color("black")
    house.speed(2)

    # Move to the starting position for the base of the house
    house.penup()
    house.goto(-100, -100)  
    house.pendown()

    # Draw the base of the house
    house.begin_fill()
    house.color("blue")
    draw_square(house, 200)
    house.end_fill()

    # Move to the position for the roof
    house.penup()
    house.goto(-100, 100)
    house.pendown()

    # Draw the roof
    house.begin_fill()
    house.color("red")
    draw_triangle(house, 200)
    house.end_fill()

    # Move to the position for the door
    house.penup()
    house.goto(-40, -100)
    house.pendown()

    # Draw the door
    house.begin_fill()
    house.color("brown")
    draw_square(house, 80)
    house.end_fill()

    # Move to the position for a window
    house.penup()
    house.goto(-80, 20)
    house.pendown()

    # Draw a window
    house.begin_fill()
    house.color("yellow")
    draw_square(house, 40)
    house.end_fill()

    # Move to the position for another window
    house.penup()
    house.goto(40, 20)
    house.pendown()

    # Draw another window
    house.begin_fill()
    house.color("yellow")
    draw_square(house, 40)
    house.end_fill()

    # Hide the turtle
    house.hideturtle()

    # Keep the window open until it is closed by the user
    screen.mainloop()

draw_house()

