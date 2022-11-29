#################################################################
# Todo list
#################################################################
# DONE 1: Create player turtle and get it to move with keypress.
# DONE 2: Get turtle to reset to stating position when it hits the goal.
# DONE 3: Create Car Objects, get them to move across the screen.
# DONE 4: When car gets to end of screen have it respawn at the beginning of the screen again.
# DONE 5: Create Scoreboard, display current level, increase level each time player reaches goal.
# DONE 6: Increase speed of car each time level increases.
# TODO 7: Add in player and car collision. Reset the player back to its starting position.
#################################################################
# Resources
#################################################################
import time
from turtle import Screen
from player import Player
from car_manager import Car
from sboard import Scoreboard

#################################################################
# Game Settings
#################################################################
NUMBER_OF_CARS = 25
#################################################################
# Prepare the Game
#################################################################
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Fuck CrossyRoad!!")

# Initialize Player Turtle, move to starting position
player = Player()
player.reset()

# Create multiple cars at random locations.
list_of_cars = []

for _ in range(NUMBER_OF_CARS):
    new_car = Car()
    list_of_cars.append(new_car)

# Initialize the Score Board
scoreboard = Scoreboard()
# Variable for continuous game.
game_is_on = True
#################################################################
# Game Loop
#################################################################
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Get turtle to move with Up Arrow key press.
    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    # Reset turtle to starting position when it reaches goal line.
    if player.ycor() >= 280:
        player.reset()
        scoreboard.increase_score()
        for car_index in range(len(list_of_cars)):
            list_of_cars[car_index].increase_speed()

    # Get cars to move
    for car_index in range(len(list_of_cars)):
        list_of_cars[car_index].move()
        if list_of_cars[car_index].xcor() <= -350:
            list_of_cars[car_index].reset()
        # Collision
        if player.distance(list_of_cars[car_index].pos()) <= 20:
            player.reset()
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
