from tkinter import *

from tkinter import ttk

win = Tk()
win.title("Let's Doodle")


#variable
pen_width = 2
current_color = "black"
last_x = None
last_y = None

#---------------------------
def create_btns(parent):
    colors = ["black", "red" , "green", "yellow", "royalblue", "purple", "pink", "magenta", "cyan", 'orange']

    for color in colors:
        button = Button(parent , bg = color , command = lambda c = color: change_color(c))
        button.pack(pady = 2)

def change_color(color):
    global current_color
    current_color = color

def update_pen_width(val):
    global pen_width
    pen_width = int(float(val)) #convert the str to float first thn to int

def paint(event):
    global last_x , last_y
    x , y = event.x , event.y
    if last_x and last_y:
        canvas.create_line(last_x , last_y , x, y, fill = current_color, width = pen_width, capstyle = ROUND , smooth=True)
    
    last_x , last_y = x , y

def reset(event):
    global last_y, last_x
    last_x , last_y = None, None


#DESIGN------------------------------------------------------------________________
canvas = Canvas(win, bg = "white" , width = 800, height = 500)
canvas.pack(side = LEFT, fill = BOTH, expand = True)


btn_frame = Frame(win)
btn_frame.pack(side = RIGHT, fill = Y)

create_btns(btn_frame)

pen_slider = Scale(btn_frame, from_ = 1, to_ = 50, orient = HORIZONTAL, command = update_pen_width)
pen_slider.set(pen_width)
pen_slider.pack(pady = 10)


#EVENT BINDING
canvas.bind("<B1-Motion>" , paint)
canvas.bind("<ButtonRelease-1>" , reset)

mainloop()


