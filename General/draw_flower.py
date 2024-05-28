import turtle
import colorsys

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    flower = turtle.Turtle()
    flower.speed(0)
    flower.width(2)
    
    num_petals = 36
    hue = 0
    
    for i in range(num_petals):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        flower.pencolor(color)
        flower.fillcolor(color)
        
        flower.begin_fill()
        flower.circle(100, steps=3)
        flower.end_fill()
        
        flower.right(360 / num_petals)
        hue += 1 / num_petals

    flower.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_flower()
