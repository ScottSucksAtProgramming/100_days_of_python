############################################################
# Resources
############################################################
from turtle import Turtle

# Constants for game settings
PANEL_POSITION = [(350, 0), (-350, 0)]
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 25
UP = 270
DOWN = 90

# TODO 2: Build a paddle, instruct it to move with arrow keys.
# Create Paddles Class, inheritance from Turtle Class.


class Paddle(Turtle):
    def __init__(self, paddle_number):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(PANEL_POSITION[paddle_number])

    def up(self):
        """Move right paddle up."""
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def down(self):
        """Move right paddle down."""
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)
