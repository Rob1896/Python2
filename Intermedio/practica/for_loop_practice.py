import turtle

turtle.bgcolor('green')

tess = turtle.Turtle()
tess.color('red')

tess.speed(1)

for i in range(5):
    tess.forward(100)
    tess.forward(100)
    tess.left(144)

turtle.exitonclick()