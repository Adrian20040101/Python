import turtle
from turtle import *

#setup(500, 500)
#Screen()
t = turtle.Pen()
turtle.speed(3)
hideturtle()

def up():
    t.up()

def down():
    t.down()

def forward():
    t.forward(10)

def backward():
    t.backward(10)

def left():
    t.left(45)

def right():
    t.right(45)

listen()
onkey(up, 'f')
onkey(down, 'g')
onkey(forward, 'w')
onkey(backward, 's')
onkey(left, 'a')
onkey(right, 'd')

mainloop()