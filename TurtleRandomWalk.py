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

tim.pensize(10)
tim.pencolor()
tim.pendown()
duration = 1

while duration <60:
    tim.color(random.choice(colours))
    angle = random.randint(-359, 360)

    tim.right(angle)
    tim.forward(20)
    duration += 1



screen = Screen()
screen.exitonclick()


