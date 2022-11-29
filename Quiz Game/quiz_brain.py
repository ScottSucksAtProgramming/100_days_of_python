class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0  # Determines the question number program is currently on.
        self.question_list = q_bank  # Imports the questions from a question bank.
        self.score = 0  # Determines the player's starting score.

    def next_question(self):
        """Asks the next question in the question bank."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(player_answer, current_question.answer)

    def still_has_questions(self):
        """Will return True if there are more questions to be asked. Otherwise returns False."""
        return self.question_number < len(self.question_list)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's right!")
        else:
            print("Sorry, that was incorrect.")
        print(f"The correct answer was {correct_answer}.")
        print(f"You're current score is {self.score}/{self.question_number}.")
