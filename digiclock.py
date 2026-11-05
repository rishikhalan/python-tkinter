
from tkinter import *
from tkinter import font
from datetime import datetime

win = Tk()
win.title("Digital Clock, to the second!")

custom_font = font.Font(family = "Digital-7" , size = 40 , weight = "bold")

def update_clock():
    now  = datetime.now()
    #format the time as 12-hour format with AM/PM
    current_time = now.strftime("%H:%M:%S")
    label_clock.config(text = current_time)

    label_clock.after(1000 , update_clock)






label_clock = Label(win , font = custom_font , fg = "cyan" , bg = "black")
label_clock.pack(padx = 10 , pady = 10)


update_clock()

mainloop()