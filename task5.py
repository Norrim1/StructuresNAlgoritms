import turtle
import random

def tree(branchLen, t):
 if branchLen > 5:
    first =  random.randint(15, 45)
    random_minus = first =  random.randint(5, 30)
    second = random.randint(15, 45)
    total = first + second
    t.pensize(branchLen / 5)
    t.forward(branchLen)
    t.right(first)
    tree(branchLen - random_minus, t)
    t.left(total)
    tree(branchLen - random_minus, t)
    t.right(second)
    t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()

main()
