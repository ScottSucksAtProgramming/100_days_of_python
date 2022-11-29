############################################################
# Resources
############################################################
from turtle import Turtle
import random

# Constants for game settings.
BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_POSITION = (0, 0)
BALL_SPEED = 20
BALL_HEADING = 45
BALL_UP = 10
BALL_DOWN = -10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.speed("slowest")
        self.penup()
        self.goto(BALL_POSITION)
        self.move_y = 10
        self.move_x = 10

    def move(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()

