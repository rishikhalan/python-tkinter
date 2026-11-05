from tkinter import *
from tkinter.colorchooser import askcolor


#function
def pick_color():
    color = askcolor(title = 'Choose a color')[1]# RGB - ((255 ,0 , 0)---\\\\\\//////---HEXADECIMAL - "#ff0000"
    print(color)

    if color :
        color_label.config(bg = color, text = f"Selected Color: {color}")


#Create main window
root = Tk()
root.title("Color Picker Tool")
root.geometry("400x400")
root.configure(bg="#333333")

title = Label(root , text = "Color Picker Tool" , font = ("Comic Sans MS" , 20, 'bold')
              ,fg = 'white', bg = '#333333')
title.pack(pady = 20)

pick_btn = Button(root , text = "Pick A Color" , font = ("Comic Sans MS" , 15)
              ,fg = 'white', bg = '#A4067A', command=pick_color)
pick_btn.pack(pady = 20)

color_label = Label(root , text = "Selected Color : None" , font = ("Comic Sans MS" , 15, 'bold')
              ,fg = 'black', bg = '#ffffff', width = 20 , height = 3, relief = 'raised')
color_label.pack(pady = 20)



mainloop()