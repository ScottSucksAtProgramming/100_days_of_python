###############################################################
# Resources
###############################################################
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

###############################################################
# Prep
###############################################################
question_bank = []
number_of_questions = len(question_data)

# Creates a question object for each question in the data.py dictionary and stores it as
# an item in the list question_bank
for item in range(0, number_of_questions):
    append = question = Question(question_data[item]['question'], question_data[item]["correct_answer"])
    question_bank.append(append)

# Initializes the quiz and pulls in the question bank that was just created.
quiz = QuizBrain(question_bank)

###############################################################
# Game Loop
###############################################################

# Loop continues as long as there are more questions to be asked, then asks the next
# question.
while quiz.still_has_questions():
    quiz.next_question()

# When the quiz is over, end the game and return the player's score.
print("Congratulations. You've completed the quiz!")
print(f"Your total score was {quiz.score} out of a possible {quiz.question_number}.")
