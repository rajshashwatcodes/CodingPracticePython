import turtle
import colorsys

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    spiral = turtle.Turtle()
    spiral.speed(0)  # Fastest speed
    spiral.width(2)
    
    num_colors = 360
    for i in range(num_colors):
        color = colorsys.hsv_to_rgb(i/num_colors, 1.0, 1.0)
        spiral.pencolor(color)
        spiral.forward(i * 2)
        spiral.right(59)
    
    turtle.done()

if __name__ == "__main__":
    draw_spiral()
