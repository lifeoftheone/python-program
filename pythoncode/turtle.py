import turtle

myturtle=turtle.Turtle()

def square(length, angle):
    myturtle.forward(length)
    myturtle.left(angle)
    myturtle.forward(length)
    myturtle.left(angle)
    myturtle.forward(length)

for i in range(4):
    square(50,90)