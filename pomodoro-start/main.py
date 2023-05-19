from tkinter import *
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
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title.config(text="TIMER")
    check_mark.config(text=" ")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    sbreak_sec = SHORT_BREAK_MIN*60
    lbreak_sec = LONG_BREAK_MIN*60

    if reps%2 != 0:
        set_countdown(work_sec)
        title.config(text="Work Time", fg=GREEN)
    elif reps%8 == 0:
        set_countdown(lbreak_sec)
        title.config(text = "Long Break", fg=RED)
    else:
        set_countdown(sbreak_sec)
        title.config(text="Short Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def set_countdown(count):
    global reps, timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count>0:
       timer = window.after(1000, set_countdown, count-1)
    else:
        start_timer()
        if reps%2 == 0:
            check_mark.config(text="✔")
        else:
            check_mark.config(text=" ")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=214, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/Vijay kumar/Downloads/pomodoro-start/tomato.png")
canvas.create_image(100, 100, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
sbutton = Button(text="Start", command=start_timer)
rbutton=Button(text="Reset", command=reset_timer)
check_mark=Label(text=" ", fg=GREEN, font=(FONT_NAME), bg=YELLOW)

title.grid(column=1, row=0)
sbutton.grid(column=0, row=2)
rbutton.grid(column=2, row=2)
check_mark.grid(column=1, row=3)


window.mainloop()