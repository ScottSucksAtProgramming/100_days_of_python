from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #Build the window.
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Build the canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 200,
            text="Question Text Goes Here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))

        # Score Label
        self.score = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Build some buttons
        true_button = PhotoImage(file="./images/true.png")
        false_button = PhotoImage(file="./images/false.png")
        self.true = Button(image=true_button, highlightthickness=0,
                           command=self.true_pressed)
        self.true.grid(column=0, row=2)
        self.false = Button(image=false_button, highlightthickness=0,
                            command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz. How did you do?")
            self.true.destroy()
            self.false.destroy()

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)
        print(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)
        print(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.after(250, self.get_next_question)

        else:
            self.canvas.config(bg="red")
            self.canvas.after(250, self.get_next_question)
