#################################################################
# Resources
#################################################################
from turtle import Turtle

#################################################################
# Setting
#################################################################
FONT = ("Courier", 24, "normal")

#################################################################
# Classes and Methods
#################################################################


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.increase_score()

    def increase_score(self):
        """Increases the level number and prints it on the top of the screen."""
        self.clear()
        self.level += 1
        self.goto(-230, 270)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", align="center", font=("courier", 25, "normal"))
