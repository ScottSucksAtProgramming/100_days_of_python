

# -------------------------- RESOURCES --------------------------#
import tkinter.messagebox
from tkinter import *
import pandas
from random import randint

# --------------------------- CONSTANTS -------------------------#
BACKGROUND_COLOR = "#B1DDC6"

# -------------------------- FUNCTIONS --------------------------#
# This variable is going to be used as a global to make the functions simpler.
# I know this isn't the best way to write a code but it feels simplest to me.
chosen_word = ""


def next_card():
    """Selects a random word from the to_learn dictionary and prints it in
     French on to the card and turns card to the white side. After 3 second activates card_flip."""
    wordlist_length = len(to_learn)
    global chosen_word, flip_timer
    window.after_cancel(flip_timer)
    if wordlist_length > 0:
        chosen_word = to_learn[randint(0, wordlist_length-1)]
        canvas.itemconfig(card_side, image=card_front_img)
        canvas.itemconfig(language_text, fill="black", text="French")
        canvas.itemconfig(word_text, fill="black", text=chosen_word["French"])
        flip_timer = window.after(3000, flip_card)
    else:
        tkinter.messagebox.showinfo(title="No more words.", message="Congrats you learned all your words. "
                                                                    "Take a break and come back later.")
        import os
        os.remove("./data/words_to_learn.csv")
        window.destroy()

# noinspection PyTypeChecker
def flip_card():
    """Prints the english word on the card and sets it to the green side."""
    global chosen_word
    canvas.itemconfig(card_side, image=card_back_img)
    canvas.itemconfig(language_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=chosen_word['English'])


def remove_word():
    global chosen_word
    to_learn.remove(chosen_word)
    next_card()


def on_closing():
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    window.destroy()


# ----------------------------- UI ------------------------------#
# Scott builds a window to house all his magic.
window = Tk()
window.title("Lets Learn Some Shit")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Next up we build a canvas.
canvas = Canvas(width=800, height=540, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_side = canvas.create_image(410, 270, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Red Button
wrong_img = PhotoImage(file="./images/wrong.png")
red_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
red_button.grid(column=0, row=1)

# Green Button
right_img = PhotoImage(file="./images/right.png")
green_button = Button(image=right_img, highlightthickness=0, command=remove_word)
green_button.grid(column=1, row=1)

# ------------------------- MAIN PROGRAM ------------------------#
# Try to open words_to_learn.csv, if FileNotFoundError then open full dictionary.
# Pandas turns csv file into workable dictionary.
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
    

# Flips the first card
flip_timer = window.after(3000, flip_card)
next_card()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
