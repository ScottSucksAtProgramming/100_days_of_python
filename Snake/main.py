##########################################################
# Resources
##########################################################
from turtle import Screen
import time
from snake import Snake
from food import Food
from sboard import ScoreKeeper
##########################################################
# Functions
##########################################################


##########################################################
# Prep
##########################################################

# First we the background using screen with dimensions 600x600 and color it black.
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("It's Snake Bitch!!")
scr.tracer(0)  # Turn off tracer mode. The screen will only refresh when the update command is given.

score = 0
snake = Snake()
food = Food()
scorekeeper = ScoreKeeper()
scr.update()

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.07)

    if snake.head.distance(food) < 20:
        food.refresh()
        scorekeeper.update_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scorekeeper.reset()
        snake.snake_reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scorekeeper.reset()
            snake.snake_reset()


    snake.move()

    scr.onkey(fun=snake.left, key="Left")
    scr.onkey(fun=snake.right, key="Right")
    scr.onkey(fun=snake.up, key="Up")
    scr.onkey(fun=snake.down, key="Down")
    scr.listen()

scr.exitonclick()
