from tkinter import *


def converter():
    USD_TO_POUND = 0.74
    USD_TO_EURO = 0.85
    amt = float(entry.get())
    euro = amt * USD_TO_EURO
    pound = amt * USD_TO_POUND
    result.config(text = f"USD to POUND = {pound} , USD to EURO = {euro}")

win = Tk()
win.title("$$$ Currency Converter $$$")
win.configure(bg="Black")
win.geometry('400x300')

#Design ---------------------------------------------------

#Title
Label(win , text = "Currency Converter" , font = "Times 16 bold"
      ).pack(padx = 10 , pady = 10)

#label
Label(win , text = "Amount in USD" , font = "Times 10").pack(pady = 10)

#Entry
entry = Entry(win , text = "" , font = "Times 10")
entry.pack(pady = 10)

#Button
btn = Button(win , text = "Convert" , font = 'Times 10' , command = converter)
btn.pack(pady = 10)

#Result
result = Label(win , text = "" , font = 'Times 10')
result.pack(pady = 10)



mainloop()