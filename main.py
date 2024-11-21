from tkinter import *
import string
import time
import keyboard


# --------- Possible Constants -----------------
FONT_NAME = ("Helvetica-Narrow-Bold", 25, "bold")
sec = 10
allowed_characters = string.ascii_lowercase + string.digits + string.punctuation + " "
# ---------- Functions ------------------------


def start_writing():
    start_typing_time = time.time()
    start_time = time.time()
    while True:
        time.sleep(0.1)
        count_down(10)
        text_space.update()
        if is_typing():
            count_down(10)
            start_time = time.time()
            if time.time() > start_typing_time + 300:
                print("saving text")
                save_text()
                exit()
        else:
            count_down(sec)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 10:
                clear_screen()


def save_text():
    text_file = open("Text.txt", "w")
    text_file.write(text_space.get(1.0, END))
    text_file.close()


def clear_screen():
    text_space.delete(1.0, END)

def is_typing():
    for c in allowed_characters:
        if keyboard.is_pressed(c):
            return True
    return False



#-------------------UI---------------------------
window = Tk()
window.title("Text Disappearing App")
window.minsize(height=100, width=500)
window.config(padx=20, pady=20, bg="black")

canvas = Canvas(width=200, height=224, bg="black", highlightthickness=0)
canvas.grid(column=1, row=1)
timer_text = Label(text="You Have 10 Seconds Before The Text Disappears!", fg="white", bg="black",
                   font=(FONT_NAME, 35, "bold"))
timer_text.grid(column=1, row=2)
timer_text = Label(text="Click the 'start button', No writers block for you!", fg="white", bg="black",
                   font=(FONT_NAME, 35, "bold"))
timer_text.grid(column=1, row=3)


title = Label(text="Text Disappearing App", bg="black", fg="white", font=FONT_NAME)
title.grid(column=1, row=0)

text_space = Text(window, height=4, width=80, wrap="word", font=("Roboto", 20, "bold"))
text_space.grid(column=1, row=4, pady=(100, 100), padx=(30, 30))

start_button = Button(text="start", width=7, highlightthickness=0, command=start_writing)
start_button.grid(column=1, row=5)

window.mainloop()
