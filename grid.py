from tkinter import *



win = Tk()
win.geometry("800x300") #width x height
win.title("Lets learn Tkinter")
win.config(bg = "#EBF9C2")

#ROW 1------------------------------------------------------

l1 = Label(win, text = "Hello!" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l1.grid(row = 0, column=0,pady = 10,padx = 20)

l2 = Label(win, text = "Bonjour!" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l2.grid(row = 0, column=1,pady = 10,padx = 20)

l3 = Label(win, text = "Hola!" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l3.grid(row = 0, column=2,pady = 10,padx = 20)




#ROW 2------------------------------------------------------

l4 = Label(win, text = "Hallo!" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l4.grid(row = 1, column=0,pady = 10,padx = 20)

l5 = Label(win, text = "Hej!" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l5.grid(row = 1, column=1,pady = 10,padx = 20)

l6 = Label(win, text = "Dia Duit!" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l6.grid(row = 0, column=2,pady = 10,padx = 20)




#Row 3-----------------------
l7 = Label(win, text = "Last Row" , 
           fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

l7.grid(row = 2, column=0,pady = 10,padx = 20, columnspan = 3)



#Row 4-----------------------
enter = Entry(win , fg = "#044712" , font = ("Comic Sans MS" , 30 , "bold") , 
           bg = "#F4DB80")

enter.grid(row = 3, column=0,pady = 10,padx = 20, columnspan = 3)

mainloop()