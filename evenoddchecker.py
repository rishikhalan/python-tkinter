from tkinter import *


#functions -----------------------
def checker():
    num = int(float(entry.get()))
    if num % 2 == 0:
        display_label.config(text = "Even!")
    else:
        display_label.config(text = "Odd!")



#Design -------------------------------------------
win = Tk()
win.title("Even Odd Checker")
win.config(bg = "#000000")
win.geometry('200x200')


#title
title = Label(win , text = "Even Odd Checker" , font = ("Helvetica 16 bold"), fg = "#fff" , bg = "#000000")
title.pack(pady = 10 , fill = X)

#entry
num = IntVar()
entry = Entry(win, text = "Enter a Number" , font = ("Helvetica 10 bold") , fg = '#fff' , bg = '#000')
entry.pack(pady = 10)

#checker button
check_btn = Button(win, text = "Even or Odd?" , font = ("Helvetica 10 bold") , fg = '#000' , bg = '#fff' , command = checker)
check_btn.pack(pady = 10)

#Display label
display_label = Label(win , text = "" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#000")
display_label.pack(pady = 10)




mainloop()