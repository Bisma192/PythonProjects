from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["red" , "green",  "blue" , "yellow" , "pink", "violet"]

tim.shape("turtle")
tim.color(random.choice(colours))


sides = 4
angle = 360 / sides
tim.shape("classic")
tim.pensize(2)
shape = 1

while shape <11:
    for _ in range (sides):
        tim.pencolor()
        tim.pendown()
        tim.forward(50)
        tim.right(angle)
        tim.forward(50)
    sides = sides + 1
    angle = 360 / sides
    shape = shape + 1
    tim.color(random.choice(colours))

screen = Screen()
screen.exitonclick()


