from tkinter import *
import math

#functions -------------------------------------------
def find_avr():
    hours_amt = float(hours_ent.get())
    minutes_amt = float(hours_ent.get())
    dist_amt = float(dist_ent.get())

    avr = dist_amt / (hours_amt + (minutes_amt / 60))
    display_label.config(text = f"{avr:.2f}km/h")




#DESIGN---------------------------------------
win = Tk()
win.title("Average Speed Calculator")
win.config(bg = "#3D3B3B")
win.geometry('290x320')





#Title
title = Label(win , text = "Average Speed Calculator" , font = ("Helvetica 16 bold"), fg = "#fff" , bg = "#3d3b3b")
title.grid(pady = 10 , padx = 5, columnspan = 2 , row = 0)


#Hours Label
hours = Label(win , text = "Hours" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
hours.grid(column = 0, padx = 5 , row = 1, pady = 10)

#hours entry
hours_amt = IntVar()
hours_ent = Entry(win , text = "" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
hours_ent.grid(column = 1, padx = 5, row = 1, pady = 10)


#Minutes Label
minutes = Label(win , text = "Minutes" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
minutes.grid(column = 0, padx = 5 , row = 2, pady = 10)

#Minutes entry
minutes_amt = IntVar()
minutes_ent = Entry(win , text = "" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
minutes_ent.grid(column = 1, padx = 5, row = 2, pady = 10)


#dist Label
dist = Label(win , text = "Distance In Km" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
dist.grid(column = 0, padx = 5, row = 3, pady = 10)

#dist entry
dist_amt = IntVar()
dist_ent = Entry(win , text = "" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
dist_ent.grid(column = 1, padx = 5 , row = 3, pady = 10)


#Average Button
average = Button(win , text = "Average" , font = ("Helvetica 16 bold") , command = find_avr , fg = "#aeebff" , bg = "#000")
average.grid(columnspan = 2 , row = 4 , padx = 20, pady = 5)


#Label for displaing avr
display_label = Label(win , text = "" , font = ("Helvetica 10 bold"), fg = "#fff" , bg = "#3d3b3b")
display_label.grid(columnspan = 2, padx = 10, row = 5, pady = 5)







mainloop()
