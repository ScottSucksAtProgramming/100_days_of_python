#########################################################
# Resources
#########################################################
from turtle import Turtle, Screen
import random

#########################################################
# Functions
#########################################################


def race_setup(t_list):
    """Will move all turtles to their starting positions."""
    spacer = 0
    for racer in t_list:
        racer.penup()
        x = -225
        y = 155
        racer.goto(x=x, y=y-spacer)
        spacer += 50
    pen = Turtle(shape="turtle")
    pen.color("black")
    pen.pensize(7)
    pen.penup()
    pen.goto(x=226, y=-175)
    pen.pendown()
    pen.goto(x=234, y=-175)
    pen.goto(x=230, y=-175)
    pen.goto(x=230, y=175)
    pen.goto(x=226, y=175)
    pen.goto(x=234, y=175)
    pen.hideturtle()


def start_race(t_list, user_bet):
    """Turtles will race. Winner will be returned."""
    winner = "none"

    while winner == "none":

        for racer in t_list:
            if racer.xcor() >= 210:
                winner = racer.pencolor()
                print(f"{winner.capitalize()}, has won the race!!")
                if winner == user_bet:
                    print("Congratulations, You Won!")
                else:
                    print("Sorry, you lose!")
            racer.forward(random.randint(0, 10))








s = Screen()

s.setup(width=500, height=400)



#########################################################
# Prep
#########################################################

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
racers = []
for turtle_index in range(0, 7):
    t_shape = "turtle"
    t_color = rainbow[turtle_index]
    turtle = Turtle(shape=t_shape)
    turtle.color(t_color)
    racers.append(turtle)


race_setup(racers)
user_bet = s.textinput(title="Make Your Bet!", prompt="Which turtle will win "
                                                      "Red/Orange/Yellow/Green/Blue/Indigo/Violet?: ").lower()
start_race(t_list=racers, user_bet=user_bet)
s.exitonclick()
