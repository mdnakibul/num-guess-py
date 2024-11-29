import tkinter as tk
from tkinter import messagebox
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Function to check the guess
def check_guess():
    try:
        user_guess = int(entry.get())
        if user_guess < 1 or user_guess > 100:
            messagebox.showinfo("Invalid Input", "Please enter a number between 1 and 100.")
        elif user_guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif user_guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it! The number was {random_number}.")
            reset_game()
    except ValueError:
        messagebox.showinfo("Invalid Input", "Please enter a valid number.")

# Function to reset the game
def reset_game():
    global random_number
    random_number = random.randint(1, 100)
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

# Heading
heading = tk.Label(root, text="Guess the Number (1-100)", font=("Helvetica", 16))
heading.pack(pady=20)

# Input field
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

# Guess button
guess_button = tk.Button(root, text="Check", font=("Helvetica", 14), command=check_guess)
guess_button.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
