import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    title_label.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 > 0:
        count_down(work_sec)
        title_label.config(text="Work")
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text="Relax", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Relax", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    # Math trickery. First we divide the min
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
            checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# In which Scott creates a happy little window.
window = tkinter.Tk()
window.title("Get Shit Done With Pomodoro, You Lazy Fuck")
window.config(padx=100, pady=50, bg=YELLOW)


# Where Scott places a plump tomato dead center into the window. That's right.
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# Here Scott sets the txt to a variable so it can be fucked with.
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Where scott adds two friendly labels.
title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 55, "normal"))
title_label.grid(column=1, row=0)

checkmark_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmark_label.grid(column=1, row=3)

# Here we see Scott place two jovial buttons. How nice.
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
