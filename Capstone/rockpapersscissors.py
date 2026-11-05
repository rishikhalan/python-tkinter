from tkinter import *
from PIL import Image, ImageTk
import random



rpswin = Tk()
rpswin.title("Rock Paper Scissors")
rpswin.geometry("500x470")
rpswin.configure(bg="lightblue")


#variables
choices = ["r", "p", "s"]#list
name = {"r" : "Rock", 
        "p" : "Paper",
        "s" : "scissors"}#dictionary

player_score = 0
comp_score = 0




def reset():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    lbl_p_score.config(text = 'Player Score: 0')
    lbl_c_score.config(text = 'Computer Score: 0')
    lbl_player.config(text='')
    lbl_comp.config(text='')
    lbl_result.config(text='')
    
def play(user_choice):
    global player_score, comp_score, name

    computer = random.choice(choices)

    lbl_player.config(text = f"Player: {name[user_choice]}")
    lbl_comp.config(text=f"Computer: {name[computer]}")

    if user_choice == computer:
        lbl_result.config(text="It's a Tie!")
    elif (user_choice == "r" and computer == "s") or \
        (user_choice == "p" and computer == "r") or \
        (user_choice == "s" and computer == "p"):
        player_score += 1
        lbl_result. config(text="Player Wins!")
    else:
        comp_score += 1
        lbl_result.config(text="Computer Wins!")

    lbl_p_score.config(text="Player Score: " + str(player_score) )
    lbl_c_score.config(text="Computer Score: " + str(comp_score) )




#load images
def load_images(name):
    img = Image.open(name)
    img = img.resize((120, 100))
    return ImageTk.PhotoImage(img)

rock_img = load_images("rock.png")
paper_img = load_images("paper.png")
scissors_img = load_images("scissors.png")


#Design
#row 1
Label(rpswin, text = "Rock Paper Scissors" , 
      bg = "lightblue" , fg = "black", 
      font = ("Comic Sans MS" , 20, "bold")).grid(row = 0, column = 0, columnspan = 3, pady = 20)


#row 2
Button(rpswin, image = rock_img , text = "Rock", compound = TOP, bg = "lightcoral", command=lambda: play("r")).grid(row = 1, column = 0, pady = 10,padx = 10)

Button(rpswin, image = paper_img , text = "Paper", compound = TOP, bg = "lightyellow", command=lambda:play("p")).grid(row = 1, column = 1, pady = 10,padx = 10)

Button(rpswin, image = scissors_img , text = "Scissors", compound = TOP, bg = "lightblue", command=lambda: play("s")).grid(row = 1, column = 2, pady = 10,padx = 10)




#row 3 - result
lbl_result = Label(rpswin, text="", font=("Comic Sans MS", 16, "bold"), bg ="lightblue", fg="red")
lbl_result.grid(row = 2, column=0, columnspan=3, pady=10)


#row 4 - player choice
lbl_player = Label(rpswin, text="", font=("Comic Sans MS", 16, "bold"), bg ="lightblue", fg="black")
lbl_player.grid(row = 3, column=0, columnspan=3, pady=10)

#row 5 - computer choice
lbl_comp = Label(rpswin, text="", font=("Comic Sans MS", 16, "bold"), bg ="lightblue", fg="black")
lbl_comp.grid(row = 3, column=0, columnspan=3, pady=10)


#row 6 - score
lbl_p_score = Label(rpswin, text="Player Score: 0", font=("Comic Sans MS", 16, "bold"), bg ="lightblue", fg="black")
lbl_p_score.grid(row = 3, column=0, pady=10)

lbl_c_score = Label(rpswin, text="Computer Score: 0", font=("Comic Sans MS", 16, "bold"), bg ="lightblue", fg="black")
lbl_c_score.grid(row = 4, column=0, pady=10)


#row 7- Reset Button
Button(rpswin, text="Reset", bg = "orangered", fg = "white", command = reset).grid(row = 6, column = 0, columnspan=3, pady=10)

mainloop()