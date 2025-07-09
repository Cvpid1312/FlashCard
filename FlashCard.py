import tkinter as tk
import random
from tkinter import messagebox, filedialog

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

card_label = tk.Label(root, text="Let's get smart!")
card_label.pack(pady=20, padx=45)

user_input = tk.Entry(root)

current_card_index = 0
score = 0

def show_card():

    global current_card_index

    card_label.config(text=cards[current_card_index].question)
    user_input.pack()
    check_button.pack(pady=20)

def show_result():

    card_label.config(text=f"You scored {score}/10. \n\nWould you like to try again?")
    check_button.pack_forget()
    start_button.config(text="TRY AGAIN")
    start_button.pack(pady=40, padx=50)
    user_input.pack_forget()


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

    if current_card_index < len(cards):
        show_card()
    else:
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


    
check_button = tk.Button(root, text="check", command=check_answer)
start_button = tk.Button(root, text="START", command= start_game)

start_button.pack(pady=40, padx=50, anchor="center")

root.mainloop()



