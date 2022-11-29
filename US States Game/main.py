##################################################################
# Todos
##################################################################
# DONE 1: Convert the guess to Title Case.
# DONE 2: Check if the guess is among the 50 States
# DONE 3: Write correct guess on map
# DONE 4: Use a loop to allow the user to keep guessing.
# DONE 5: Record the correct guesses in a list.
# DONE 6: Keep Track of the Score.
##################################################################
# Resources
##################################################################
import turtle
import pandas as pd

##################################################################
# Functions
##################################################################
# Check if the guess is among the 50 States


def check_for_state(guess):
    """Will return true if the guess is one of the states."""
    for state_index in range(len(states.state)):
        if answer == states.state[state_index]:
            return True


def place_answer_on_map(guess):
    """Will place the name of the state at the correct location on the map."""
    state_cords = (int(states[states.state == answer]["x"]), int(states[states.state == answer]["y"]))
    writer.goto(state_cords)
    writer.write(arg=guess)

##################################################################
# Prep
##################################################################


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
the_map = turtle.Turtle()
the_map.shape(image)

writer = turtle.Turtle()
writer.shape("turtle")
writer.hideturtle()
writer.penup()
writer.color("Black")

game_is_on = True
score = 0
answer_list = []
states = pd.read_csv("50_states.csv")
# Convert the guess to Title Case.
while len(answer_list) < 50:
    answer = screen.textinput(title=f"{score}/50 States Guessed", prompt="Guess another states' name.").title()

    if answer == "Exit":
        missing_states = []
        if check_for_state(answer):
            place_answer_on_map(answer)
            if answer not in answer_list:
                answer_list.append(answer)
            score = len(answer_list)
        break


screen.exitonclick()
