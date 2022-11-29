#################################################################
# Resources
#################################################################
from turtle import Turtle
#################################################################
# Settings
#################################################################
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#################################################################
# Classes and Objects
#################################################################


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)

    def reset(self):
        """Returns the player turtle to it's starting position."""
        self.goto(STARTING_POSITION)

    def move(self):
        """Moves the player turtle up by it's specified move distance."""
        self.forward(MOVE_DISTANCE)
