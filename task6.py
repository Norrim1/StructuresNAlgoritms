import turtle

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

def koh_line(iter, length):
    if iter == 0:
        turtle.forward(length)
    else:
        koh_line(iter - 1, length)
        turtle.left(60)
        koh_line(iter - 1, length)
        turtle.right(120)
        koh_line(iter - 1, length)
        turtle.left(60) 
        koh_line(iter - 1, length)

koh_line(4, 5)

turtle.mainloop()