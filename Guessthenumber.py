from tkinter import *
from tkinter import messagebox
import random



def start_game():
    global secret_num , attempts
    secret_num = random.randint(1, 100)
    attempts = 0
    instruction_label.config(text = f"Guess the number between 1 and 100\n You have 10 attempts")
    entry.delete(0, END)


def clear_feedback():
    feedback_label.config(text="")

def check_guess():
    global attempts , secret_num
    input = entry.get()

    if input.isdigit():
        guess = int(input)

    else:
        messagebox.showerror("Invalid Input" , "Please enter a valid number.")
        entry.delete(0, END)
        return
    attempts += 1

    if guess < secret_num:
        feedback_label.config(text = f"{guess}... Too low!! Try Again")
        instruction_label.config(text = f"Guess the number between 1 and 100\n You have {10 - attempts} attempts")
        entry.delete(0, END)

    elif guess > secret_num:
        feedback_label.config(text = f"{guess}... Too High!! Try Again")
        instruction_label.config(text = f"Guess the number between 1 and 100\n You have {10 - attempts} attempts")
        entry.delete(0, END)

    else:
        feedback_label.config(text = f"Congratulations! You guessed the number right in {attempts} attempts!" , fg = "green")
        messagebox.showinfo("Win" , "Congratulations! You win the game!")
        entry.delete(0, END)
        root.after(2000, clear_feedback)

    if attempts > 10:
        feedback_label.config(text = f"Game over! The correct number was {secret_num}!" , fg = "red")
        messagebox.showinfo("Game Over" , "Game over!! You lost the game!")
        entry.delete(0, END)
        root.after(2000, clear_feedback)

    root.after(2000, clear_feedback)


#------------------------------------------Design---------------------------------------

root = Tk()
root.title("Guess the Number Game")
root.geometry("400x300")
root.configure(bg="orange")

title_label = Label(root, text="Guess the Number!", font=("Comic Sans MS", 20, "bold"), bg="orange")
title_label.pack(pady=10)

# Instruction label
instruction_label = Label(root, text="", font=("Arial", 14), bg="orange")
instruction_label.pack(pady=5)

# Entry for user's guess
entry = Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Submit button
submit_button = Button(root, text="Submit", command=check_guess, font=("Arial", 14), bg="#09555c", fg="white", relief="raised")
submit_button.pack(pady=5)

# Feedback label
feedback_label = Label(root, text="", font=("Arial", 14), bg="orange")
feedback_label.pack(pady=10)

#Start the game
start_game()



mainloop()