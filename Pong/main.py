############################################################
# Resources
############################################################
from turtle import Screen
from paddle import Paddle
from ball import Ball
from sboard import Scoreboard, MiddleLine
import time

############################################################
# Prepare The Game
############################################################

# TODO 1: Create Screen 600x800; black background, stay on screen until clicked.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("It's Fucking Pong, My Guy!")
screen.tracer(0)

r_paddle = Paddle(paddle_number=0)
l_paddle = Paddle(paddle_number=1)
ball = Ball()

vertical_direction = 10
horizontal_direction = 10

middle_line = MiddleLine()
scoreboard = Scoreboard()

speed = 0.06
############################################################
# Game Code
############################################################
game_is_on = True

while game_is_on:

    # Start the game
    screen.update()
    time.sleep(speed)
    ball.move()

    # Bounce ball off of top or bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Bounce ball off paddles.
    if ball.xcor() > 320 and ball.distance(r_paddle) < 40 or ball.xcor() < -320 and ball.distance(l_paddle) < 40:
        ball.bounce_x()
        speed -= 0.005

    # Right paddle misses.
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
        speed = .06
        # screen.update()
        # time.sleep(0.5)

    # Left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        speed = .06
        # screen.update()
        # time.sleep(0.5)

    # TODO 2a: Panel Movement
    screen.listen()
    screen.onkey(r_paddle.up, key="Up")
    screen.onkey(r_paddle.down, key="Down")
    screen.onkey(l_paddle.up, key="w")
    screen.onkey(l_paddle.down, key="s")


screen.exitonclick()

