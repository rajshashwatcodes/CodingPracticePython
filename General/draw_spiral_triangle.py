import turtle

def draw_spiral_triangle():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    spiral = turtle.Turtle()
    spiral.speed(0)
    spiral.width(2)
    
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    
    side_length = 10
    for i in range(200):
        spiral.pencolor(colors[i % len(colors)])
        spiral.forward(side_length)
        spiral.left(120)  # This angle creates the triangle
        side_length += 2
    
    turtle.done()

if __name__ == "__main__":
    draw_spiral_triangle()
