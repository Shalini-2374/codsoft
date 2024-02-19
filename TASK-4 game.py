import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Label and OptionMenu for user choice
user_choice_label = tk.Label(root, text="Choose:")
user_choice_label.pack()
user_choice_var = tk.StringVar(root)
user_choice_var.set(choices[0])
user_choice_menu = tk.OptionMenu(root, user_choice_var, *choices)
user_choice_menu.pack()

# Button to play the game
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Start the application
root.mainloop()
