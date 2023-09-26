import pandas as pd
from tkinter import*
import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
card = None
with open("./flash card (2)/french_words.csv", "r") as file:
    data = pd.read_csv(file)
    to_learn = data.to_dict(orient='records')


def next_card():
    global card
    card = random.choice(to_learn)
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=card["French"])
    window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=card["English"])


def is_known():
    global to_learn
    to_learn.remove(card)
    next_card()


def countdown(n): #timer
    if n>0:
        window.after(1000, countdown, n-1)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=528, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="../flash card/flash card (3)/card_back.png")
card_front = PhotoImage(file="../flash card/flash card (3)/card_front.png")
image = canvas.create_image(400, 528/2, image=card_back)
canvas.grid(column=0, row=0, columnspan=2)


check = PhotoImage(file="../flash card/flash card (3)/right.png")
correct = Button(image=check, highlightthickness=0, command=next_card)
correct.grid(column=1, row=1)
cross = PhotoImage(file="../flash card/flash card (3)/wrong.png")
wrong = Button(image=cross, highlightthickness=0)
wrong.grid(column=0, row=1)

title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))







window.mainloop()