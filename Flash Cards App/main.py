import tkinter as tk
from tkinter import Canvas, PhotoImage
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
current_word = {}
word_list = {}

# Data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    initial_data = pd.read_csv("data/french_words.csv")
    word_list = initial_data.to_dict(orient='records')
else:
    word_list = data.to_dict(orient="records")




def next_word():
    global current_word
    current_word = random.choice(word_list)
    canvas.itemconfig(card_image_item, image=card_front_image)
    canvas.itemconfig(title_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=current_word["French"], fill='black')
    flip_card_after_delay()


def flip_card_after_delay():
    window.after(3000, flip_card)


def flip_card():
    global current_word
    canvas.itemconfig(card_image_item, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")


def right():
    word_list.remove(current_word)
    data = pd.DataFrame(word_list)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_word()


canvas = Canvas(width=800, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_image_item = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, 'italic'), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, 'bold'), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
x_img = PhotoImage(file='./images/wrong.png')
button_wrong = tk.Button(image=x_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
button_wrong.grid(row=1, column=0)

correct_img = PhotoImage(file='./images/right.png')
button_correct = tk.Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
button_correct.grid(row=1, column=1)

next_word()

window.mainloop()
