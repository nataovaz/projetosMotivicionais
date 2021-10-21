import turtle
turtle.bgcolor("black")

t = turtle.Turtle()
t.speed(20)
t.pencolor("yellow")
t.pensize(1)

for i in range(700):
    t.forward(i)
    t.left(150)