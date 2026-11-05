from tkinter import *
from tkinter import messagebox
#Event Binding is the process of connecting a specific event
#(like mouse click or key press) to a function, so that when the event occurs, 
#the function automatically executes.

root = Tk()
root.geometry("500x400")
root.title("Fun Event Binding Exercise")
root.config(bg = "#333333")

#----------------

def on_enter(event):
    lbl.config(text = f"You pressed Enter. \nInput: {entry.get()}" , fg = 'green')
    entry.delete(0, END)

def mouse_click(event):
    lbl.config(text = f"Mouse clicked at {event.x} , {event.y}" , fg = "orange")


def mouse_move(event):
    lbl.config(text = f"Mouse at {event.x} , {event.y}" , fg = "purple")

#Messagebox asking the question
def win_close():
    if messagebox.askokcancel("Quit" , "Do you really want to close the window?"):
        root.destroy()


frame = Frame(root, bg = "#ffffff")
frame.pack(padx = 20 , pady = 20)

entry = Entry(frame , font = ("Times 18"), bg = '#000000' , fg = '#ffffff')
entry.pack(pady = 20)

lbl = Label(frame, font = ("Times 18 bold") , bg = "white" , fg = 'blue' , bd = 5)
lbl.pack(pady = 20)

btn = Button(frame, text = "Click Me", font = ("Times 18 bold") , bg = "yellow" , fg = 'blue', bd = 5 , relief = RAISED)
btn.pack(pady = 20 , padx = 20)




#binding the function with enter press event 
entry.bind("<Return>" , on_enter)

root.bind("<Motion>" , mouse_move)

btn.bind("<Button-1>" , mouse_click)

root.protocol("WM_DELETE_WINDOW" , win_close)


mainloop()