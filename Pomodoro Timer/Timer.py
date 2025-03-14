from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = "00:00"


def set_window_defaults():
    # Sets all labels to their default value
    canvas.itemconfig(timer_text, text= "00:00")
    timer.config(text="", fg= GREEN)
    check_marks.config(text= "")
    global REPS
    REPS = 0


def reset_timer():
    # Timer resets using the after_cancel method from tkinter
    window.after_cancel(TIMER)
    set_window_defaults()


def start_timer():
    global REPS
    REPS += 1

    count_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        # After 8 reps long break will start
        count_down(long_break)
        timer.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"))
        timer.grid(column=1, row=0)

    elif REPS % 2 == 0:
        # After every learning cycle a short break will start
        count_down(short_break)
        timer.config(text="Pause", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, "bold"))
        timer.grid(column=1, row=0)

    else:
        # Start the learning timer if we're not in a break
        count_down(count_seconds)
        timer.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
        timer.grid(column=1, row=0)


def count_down(count):
    minute_count = math.floor(count / 60)
    if minute_count < 10:
        # Minutes smaller than 10 start with a 0 instead
        minute_count = f"0{math.floor(count/ 60)}"
    seconds_count = count % 60

    if seconds_count < 10:
        # Seconds smaller than 10 start with a 0 instead
        seconds_count = f"0{seconds_count}"
    canvas.itemconfig(timer_text, text=f"{minute_count}:{seconds_count}")

    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
        # Counting down until we hit 0

    else:
        start_timer()
        saved_marks = ""
        solved_intervals = math.floor(REPS/2)
        # Every 2 learning periods adds a checkmark
        for _ in range(solved_intervals):
            saved_marks += "✔"
        check_marks.config(text=saved_marks)


# Initialize the window
window = Tk()
window.title("Pomodoro Lernen")
window.config(padx=100, pady=50, bg=YELLOW)

# Initialize  canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Initialize labels
timer = Label()
timer.config(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label()
check_marks.config(fg=GREEN, bg=YELLOW, text="", font=(FONT_NAME, 10))
check_marks.grid(column=1, row=3)

# Tkinter loop for window
window.mainloop()
