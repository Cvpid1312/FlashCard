import tkinter as tk
import random
from tkinter import messagebox, filedialog
from tkinter import ttk 
import json 
import os

class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

cards1 = [
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

cards2 = [
    Card("Who is the father of all new chool rappers?","Lil B"),
    Card("Who is the the rapper that had the biggest potential?","XXX Tentacion"),
    Card("Who is the sexiest rapper?", "Young Thug"),
    Card("Which is the most popular DAW?", "FL Studio"),
]

class Deck:
    def __init__(self, title, cards):
        self.title = title
        self.cards = cards


#deck1 = Deck("Rando", None, cards1)
#deck2 = Deck("Rap", "music", cards2)

    
class DeckManager:
    def __init__(self):
        self.decklist = []

    def load_decks(self):
        path = os.path.join(os.path.dirname(__file__), "Decks")        
        for file in os.listdir(path):
            if file.endswith(".json"):
                file_path = os.path.join(path, file)
                with open(file_path, "r") as f:
                    card_data = json.load(f)
                    deck_data = []
                    for card_dict in card_data:
                        question = card_dict["question"]
                        answer = card_dict["answer"]
                        card = Card(question, answer)
                        deck_data.append(card)
                    title = os.path.splitext(file)[0]
                self.decklist.append(Deck(title, deck_data))
            
                        
                                
                                






root = tk.Tk()
root.geometry("500x450")
root.title("Flash Card Game")

card_label = ttk.Label(root, text="Let's get smart!")
card_label.pack(pady=20, padx=45)

user_input = ttk.Entry(root)
user_input.bind("<Return>", lambda event: check_answer())

current_card_index = 0
score = 0
highscore = 0
cards = None




def show_card():

    global current_card_index

    card_label.config(text=cards[current_card_index].question)
    user_input.pack()
    user_input.focus_set()
    check_button.pack(pady=20, side="right")
    show_button.pack(pady=20, side="left")

def show_result():

    global highscore

    card_label.config(text=f"You scored {score}/10. \n\nWould you like to try again?")
    start_button.config(text="TRY AGAIN", state="normal")
    start_button.pack(pady=40, padx=50)
    if score > highscore:
        highscore = score
        messagebox.showinfo("NEW HIGHSCORE", "You just set a new highscore, well done!")
    highscore_label = ttk.Label(text=f"Highscore: {highscore}")
    highscore_label.pack(pady=34, side="bottom")


def show_answer():

    global current_card_index

    answer = cards[current_card_index].answer
    card_label.config(text=f"The answer is {answer}.")
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
    show_button.pack_forget()

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
            messagebox.showinfo("PERFECT", "You nailed it mate!!!!")
            show_result()
        else:
            messagebox.showinfo("DONE", "That's all for tongight folks!")
            show_result()


def selection(*args):
    
    global cards
    
    title = selected_deck.get()
    for deck in manager.decklist:
        if title == deck.title:
            cards = deck.cards

    start_button.config(state="normal")

def start_game():

    global current_card_index
    global score
    global cards

    random.shuffle(cards)

    for deck in deck_menu:
        deck.pack_forget()

    score = 0
    current_card_index = 0
    start_button.pack_forget()
    show_card()


deck_menu = []
    
check_button = ttk.Button(root, text="check", command=check_answer)
start_button = ttk.Button(root, text="START", command= start_game, state= "disabled")
show_button = ttk.Button(root, text="reveal answer", command=show_answer)

manager = DeckManager()
selected_deck = tk.StringVar()

manager.load_decks()

for deck in manager.decklist:
    rb = ttk.Radiobutton(root, text=deck.title, value=deck.title, variable=selected_deck, command=selection)
    rb.pack()
    deck_menu.append(rb)

start_button.pack(pady=40, padx=50, anchor="center")


root.mainloop()




