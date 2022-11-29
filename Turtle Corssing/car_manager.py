#################################################################
# Resources
#################################################################
from turtle import Turtle
import random
#################################################################
# Settings
#################################################################
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.2

#################################################################
# Classes and Objects
#################################################################


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.travel_distance = STARTING_MOVE_DISTANCE


class Car(CarManager):
    def __init__(self):
        super().__init__()
        self.goto(x=random.randint(-280, 280), y=random.randint(-240, 240))

    def move(self):
        """Moves a car forward by it's specified speed."""
        new_y = self.ycor()
        new_x = self.xcor() - self.travel_distance
        self.goto(x=new_x, y=new_y)

    def reset(self):
        """Returns a car to the right side of the screen at a new random position."""
        self.goto(x=300, y=random.randint(-240, 240))

    def increase_speed(self):
        self.travel_distance *= MOVE_INCREMENT
