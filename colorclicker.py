from tkinter import *
import random
import tkinter.messagebox as msg



# Setup window
root = Tk()
root.title("🎨 Color Clicker Pro")
root.geometry("320x300")
score = 0
current_color = ""

colors = ["green", "blue", "orange", "red", "yellow"]



def colorchange():
    global current_color
    current_color = random.choice(colors)
    button.config(bg = current_color)
    root.after(150, colorchange)

def button_click():
    global score
    if current_color == "red":
        score -= 5
    else:
        score += 1
    if score < -10:
        msg.showinfo("😞😞Game Over😞😞", f"Too many red clicks\nYour final score was {score}")
        root.destroy()
    else:
        lbl.config(text = f"Score:{score}")        














#Score label
lbl = Label(root, text = "Score: 0", font = ("Arial", 16))
lbl.pack(pady=5)




#color button
button = Button(root, text = "Click Me!", font=("Arial",20), command = button_click)
button.pack(pady=5)

colorchange()

mainloop()





