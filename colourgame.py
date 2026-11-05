from tkinter import *
import random

win = Tk()
win.title("Colour Game")
win.configure(bg="Black")
win.geometry('400x700')


def set_target_color():
    global colors, target_color
    target_color = random.choice(colors)
    whatcolorlbl.config(text=f'Click {target_color}!', fg=target_color )

def check_color(selected_color):
    global score
    if selected_color == target_color:
        score += 1
        scorelbl.config(text=f'Correct! Your Score: {score}')
    else:
        score -= 1
        scorelbl.config(text = f'Wrong! Your score: {score}')
    set_target_color()

    







colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"]
score = 0
#design--------------------------------------------------------------------------------------------

#What Color to click
whatcolorlbl = Label(win, text = '', font = ('Comic Sans MS', 10))
whatcolorlbl.pack(pady = 10)
#Score Label
scorelbl = Label(win, text = 'Score = 0', font = ('Comic Sans MS', 16),fg = "#FFFFFF", bg = 'black')
scorelbl.pack(pady=10)




for color in colors:
    color_button = Button(win, text=color.capitalize(), bg = color, fg = 'white', width=30, height = 2,
                          command = lambda color=color: check_color(color))
    color_button.pack(pady=5)



#Start with setting the target color.
set_target_color()






#Start the TKinter loop.

win.mainloop()