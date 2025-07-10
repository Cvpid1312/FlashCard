import tkinter as tk
import random
from tkinter import messagebox, filedialog
from tkinter import ttk

class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

cards = [
    Card("What is the capital of France?", "Paris"),
    Card("What is 2 + 2?", "4"),
    Card("What is the largest planet in our solar system?", "Jupiter"),
    Card("What is the boiling point of water?", "100 degrees Celsius"),
    Card("What is the chemical symbol for gold?", "Au"),
    Card("What is the currency of Japan?", "Yen"),
    Card("What is the main ingredient in guacamole?", "Avocado"),
    Card("What is the largest mammal?", "Blue Whale"),
    Card("What is the capital of Japan?", "Tokyo"),
    Card("What is the name of our closest star besides the Sun?", "Proxima Centauri")
]

    



root = tk.Tk()
root.geometry("500x450")
root.title("Flash Card Game")

card_label = ttk.Label(root, text="Let's get smart!")
card_label.pack(pady=20, padx=45)

user_input = ttk.Entry(root)
user_input.bind("<Return>", lambda event: check_answer())

current_card_index = 0
score = 0
highscore1 = None
highscore2 = None
highscore3 = None


def show_card():

    global current_card_index

    card_label.config(text=cards[current_card_index].question)
    user_input.pack()
    user_input.focus_set()
    check_button.pack(pady=20, side="right")
    show_button.pack(pady=20, side="left")

def show_result():

    card_label.config(text=f"You scored {score}/10. \n\nWould you like to try again?")
    start_button.config(text="TRY AGAIN")
    start_button.pack(pady=40, padx=50)

def show_answer():

    global current_card_index

    answer = cards[current_card_index].answer
    card_label.config(text=f"The right answer is {answer}.")
    check_button.config(text="next", command=next_question)
    user_input.pack_forget()
    show_button.config(state="disabled")

    current_card_index += 1


def check_answer():

    global score
    global current_card_index
    answer = user_input.get()
    correct = cards[current_card_index].answer

    user_input.delete(0, tk.END)

    if answer.strip().lower() == correct.strip().lower():
        messagebox.showinfo("CORRECT", "Right you are!")
        score += 1

    else:
        messagebox.showinfo("FALSE", "Nope, better luck next time...")
    
    current_card_index += 1
    next_question()


def next_question():

    if current_card_index < len(cards):
        show_button.config(state="normal")
        show_card()
    else:
        user_input.pack_forget()
        check_button.pack_forget()
        card_label.config(text="")

        if score == 10:
            messagebox.showinfo("PERFECT", "You fucking nailed it mate!!!!")
            show_result()
        else:
            messagebox.showinfo("DONE", "That's all for tongight folks!")
            show_result()


def start_game():

    global current_card_index
    global score

    random.shuffle(cards)

    score = 0
    current_card_index = 0
    start_button.pack_forget()
    show_card()


    
check_button = ttk.Button(root, text="check", command=check_answer)
start_button = ttk.Button(root, text="START", command= start_game)
show_button = ttk.Button(root, text="reveal answer", command=show_answer)

start_button.pack(pady=40, padx=50, anchor="center")

root.mainloop()



