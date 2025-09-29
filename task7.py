import turtle 

def draw_triangle(length): 
    for _ in range(3): 
        turtle.forward(length) 
        turtle.left(120) 

def fractal_triangle(length, depth): 
    if depth == 0: 
        draw_triangle(length) 
    else: 
        for _ in range(3): 
            fractal_triangle(length / 2, depth - 1) 
            turtle.forward(length) 
            turtle.left(120) 

turtle.speed(0)
turtle.penup() 
turtle.goto(-100, -100)
turtle.pendown() 
fractal_triangle(200, 4)
turtle.penup() 