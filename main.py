import random
from tkinter import *
import  time
import pandas as pd

# Creating a new window and configurations

# _____________________________Constants_____________________________________________#
BG_Colour = "#B1DDC6"
FONT_NAME = "Ariel"
WHITE = "#FFFFFF"
to_learn = {}
# ______________________________Generating random French Words________________________________#
try:
    data = pd.read_csv("words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # ‘records’ : list like [{column -> value}, … , {column -> value}] e.g, [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},
    to_learn = data.to_dict(orient="records")




current_card = {}



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # {'French': 'histoire', 'English': 'history'}
    current_card = random.choice(to_learn)
    random_french_word = current_card["French"]

    canvas.itemconfig(word_text, text=random_french_word, fill = "black")
    canvas.itemconfig(title_text, text="French", fill ="black")
    canvas.itemconfig(image_setup, image = old_image)
    flip_timer= window.after(3000, flip_cards)


#______________________________Flipping Cards______________________________________#
def flip_cards():

#TODO config the card to the card front
    canvas.itemconfig(image_setup, image = new_image)
    english_translation = current_card["English"]

    canvas.itemconfig(word_text, text=english_translation, fill = "white")
    canvas.itemconfig(title_text, text="English", fill="white")


#_______________________Check User's choice____________________________________#

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()









# ---------------------------- UI SETUP ------------------------------------------- #


window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BG_Colour)

flip_timer= window.after(3000, flip_cards)

canvas = Canvas(width=800, height=526, bg=BG_Colour, highlightthickness=0)

# _______ images
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")

image_setup = canvas.create_image(400, 263, image=old_image)
# card_back_setup = canvas.create_image(400, 263, image=card_back)

# ____texts____
# TODO Change text = to var
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))

canvas.grid(column=0, row=0, columnspan=2)

# _________Buttons____________
wrong_button = Button(image=wrong_img, borderwidth=0, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, borderwidth=0, command=is_known, highlightthickness=0)
right_button.grid(row=1, column=1)

next_card()




window.mainloop()
