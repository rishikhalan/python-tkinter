from tkinter import *


win = Tk()
win.geometry("800x500") #width x height
win.title("Lets learn Tkinter")
win.config(bg = "#EBF9C2")

#widget

l1 = Label(win, text = "Welcome to GUI Windows in Python" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold" , "underline") , 
           bg = "#F4DB80")

l1.pack(pady = 10 ,padx = 20 , fill = X)



l2 = Label(win, text = "It is Tkinter" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold" , "underline") , 
           bg = "#F4DB80")

l2.pack(pady = 10 , ipady = 30) # pady = vertical padding .... ipady = vertical internal padding


b1 = Button(win, text = "Click Me.." , 
           fg = "#040B47" , font = ("Comic Sans MS" , 30 , "bold" , ) , 
           bg = "#09FF00")

b1.pack(pady = 10 ,padx = 10)






mainloop()