##########################################################
# Resources
##########################################################
from turtle import Turtle

# We're gonna build our snake class in here.

STARTING_POSITION = [(0,0), (0, -20), (0, -40)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Builds a snake with each piece starting next to each other. The amount of pieces is determined by
         start_length."""
        for position in STARTING_POSITION:
            self.add_part(position)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(900, 900)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(position)
        self.segments.append(snake_part)

    def extend(self):
        self.add_part(self.segments[-1].pos())

    def move(self):
        """Moves the snake forward at a constant speed."""
        for part in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part - 1].xcor()
            new_y = self.segments[part - 1].ycor()
            self.segments[part].goto(new_x, new_y)
        self.head.forward(SPEED)

    def left(self):
        """Turns snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """Turns snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
