#################################################################
# Resources
#################################################################

from color_info import color_list
from turtle import Turtle, Screen
import random

#################################################################
# Functions
#################################################################

def paint_dots():
    for _ in range(60):
        hirst.dot(5, random.choice(color_list))
        hirst.forward(12)

def next_line():
    hirst.hideturtle()
    hirst.goto(-350, hirst.ycor()+12)
    hirst.showturtle()

#################################################################
# Prep
#################################################################

hirst = Turtle()
my_screen = Screen()
my_screen.colormode(255)
hirst.shape("turtle")
hirst.penup()
hirst.speed(300)
hirst.hideturtle()
hirst.goto(-350,-350)
hirst.showturtle()

#################################################################
# Make Art
#################################################################

for _ in range (60):
    paint_dots()
    next_line()

my_screen.exitonclick()


