
from tkinter import *
import random


win = Tk()
win.title("4x4 grid with labels")
win.config(bg = "#333333")


colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow',
        'lightpink', 'lightgrey', 'lightcyan', 'lightyellow',
        'lightsteelblue', 'lightseagreen', 'lightsalmon', 'lightgreen',
        'lightblue', 'lightcoral', 'lightgoldenrodyellow', 'lightpink']

for row in range(4):
    for col in range(4):
        l1 = Label(win , text = f"Row: {row} Col: {col}", bg=colors[random.randint(0,12)] , borderwidth = 2, relief = 'solid', 
                   fg = 'black', width = 12 , height=2)
        l1.grid(row = row, column=col, padx=10, pady=20)
mainloop()