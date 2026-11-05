from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as msg
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import random
import math


#LOGIN SCREEN--*----*----*----*----*----*----*----*----*----*----*----*--
root = Tk()
root.geometry("400x430") #width x height
root.title("Multitasker")
root.config(bg = "#000000")


#functions----------------------------------------------

#LOGIN-------------------------
def login():
    username = 'abc'
    password = '12345'

    if userentry.get() == username and passwordentry.get() == password:
        messagebox.showinfo(title = "Login Success" , message = f"You are successfully logged in. \nWelcome {username}")
        login_frame.pack_forget()
        select_game.pack(pady = 10)
    else:
        messagebox.showerror(title = "Login Error" , message = 'Security breach... Invalid Credientials...')

#TIC TAC TOE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#variables tic tac toe
count = 0
mark = ''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
panels = ['panel'] * 10



#score variables tic tac toe
score_x = IntVar(value=0)
score_o = IntVar(value=0)





#TIC TAC TOE------------------------------------------------------------------------------------------------
def tic_tac_toe():






    def win(panels , sign): # CHECKER FOR ALL WINNING CONDITITONS
        return((panels[1] == panels[2] == panels[3] == sign)
            or (panels[4] == panels[5] == panels[6] == sign)
            or (panels[7] == panels[8] == panels[9] == sign)
            or (panels[1] == panels[4] == panels[7] == sign)
            or (panels[2] == panels[5] == panels[8] == sign)
            or (panels[3] == panels[6] == panels[9] == sign)
            or (panels[1] == panels[5] == panels[9] == sign)
            or (panels[3] == panels[5] == panels[7] == sign))






    def checker(digit):
        global count, mark, digits , x , o 

        if digit in digits:
            digits.remove(digit)
            mark = 'X' if count % 2 == 0 else 'O'
            panels[digit] = mark
            count += 1
            eval(f'button{digit}.config(text = mark)')
            
            if win(panels, mark):
                if mark == "X":
                    score_x.set(score_x.get() + 1)
                    msg.showinfo("Result", f"{p1_name} Wins!")
                else:
                    score_o.set(score_o.get() + 1)
                    msg.showinfo("Result", f"{p2_name} Wins!")
                reset_game()
                return
            if count >= 9:
                msg.showinfo("Result" , "Match Tied")
                reset_game()



    def reset_game():
        global count, digits, mark, panels
        count = 0
        mark = ''
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        panels = ['panel'] * 10
        for i in range(1, 10):
            eval(f'button{i}.config(text = mark)')
            






        '''
        #check which btn is clicked
        if digit == 1 and digit in digits:
            digits.remove(digit)

            if count % 2 == 0:
                mark = 'X'
                panels[digit] = mark
            elif count % 2!= 0:
                mark = '0'
                panels[digit] = mark
            
            button1.config(text = mark)
            count += 1
            sign = mark
            
            if (win(panels, sign) and sign == 'X'):
                score_x.set(score_x.get()+1)
                msg.showinfo('Result', 'Player 1 Wins')
            
            
            elif (win(panels, sign) and sign == 'O'):
                score_x.set(score_o.get()+1)
                msg.showinfo('Result', 'Player 2 Wins')
        '''






    def start_game():
        global p1_name, p2_name
        p1_name = player1.get()
        p2_name = player2.get()

        if not p1_name or not p2_name:# if only one name is entered...
            msg.showerror(title='Input Error', message = 'Please enter names of both the players!')
            return
        tictactoewindow.destroy()
        create_game_screen()



    #Game screen
    def create_game_screen():
        gamescreen = Toplevel(root)
        gamescreen.title('Tic Tac Toe Game')
        gamescreen.config(bg = 'white')

        global x , o , score_x, score_o, button1, button2, button3, button4, button5, button6, button7, button8, button9    
        #Buttons 
        button1 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(1))
        button1.grid(row=2, column=1, padx = 3, pady = 3)
        button2 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(2))
        button2.grid(row=2, column=2, padx = 3, pady = 3)
        button3 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7,  command=lambda: checker(3))
        button3.grid(row=2, column=3, padx = 3, pady = 3)
        button4 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(4))
        button4.grid(row=3, column=1)
        button5 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(5))
        button5.grid(row=3, column=2)
        button6 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(6))
        button6.grid(row=3, column=3)
        button7 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(7))
        button7.grid(row=4, column=1)
        button8 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7, command=lambda: checker(8))
        button8.grid(row=4, column=2)
        button9 = Button(gamescreen, text = '',font=('Times 16 bold')
        ,fg = '#000000', bg = '#ffffff', height = 3, width = 7 , command=lambda: checker(9))
        button9.grid(row=4, column=3)
        

        Label(gamescreen, text = f"{p1_name}", bg = '#ffffff', fg = "#0015FF", font = ('Comic Sans MS', 15, 'bold')).grid(row = 0, column = 1, padx = 5, pady = 5)
        Label(gamescreen, text = f"{p2_name}", bg = '#ffffff', fg = "#FF0000", font = ('Comic Sans MS', 15, 'bold')).grid(row = 0, column = 3, padx = 5, pady = 5)




        x = Label(gamescreen, text = score_x ,textvariable=score_x, bg = '#ffffff', fg = "#0015FF", font = ('Comic Sans MS', 15, 'bold'))
        x.grid(row = 1, column = 1, padx = 5, pady = 5)
        o = Label(gamescreen, text = score_o , textvariable=score_o, bg = '#ffffff', fg = "#FF0000", font = ('Comic Sans MS', 15, 'bold'))
        o.grid(row = 1, column = 3, padx = 5, pady = 5)
        
        
        reset = Button(gamescreen, text = 'Reset',font=('Times 20 bold')
        ,fg = "#FFFFFF", bg = "#ef0e0e", command = reset_game).grid(row=5, column=1, columnspan=3, pady = 10)



    #DESIGN TIC TAC TOE----------------------------------------------------------------------------------------------
    tictactoewindow = Toplevel(root)
    #tictactoewindow.geometry()
    tictactoewindow.title('Tic Tac Toe')
    tictactoewindow.config(bg = "#960000")


    #Title
    Label(tictactoewindow, text = 'Tic Tac Toe\nPlease enter the player names.', font = ('Times', 15, 'bold')
        ,fg = '#ffffff', bg = '#960000').pack(pady = 10)


    #Player 1
    Label(tictactoewindow, text = 'Player 1(X)', font = ('Times', 15, 'bold')
        ,fg = '#ffffff', bg = '#960000').pack(pady = 10)


    #Player 1 entry
    player1 = Entry(tictactoewindow, font = ('Times', 15, 'bold')
        ,fg = '#000000')
    player1.pack(pady = 10)


    #Player 2
    Label(tictactoewindow, text = 'Player 2(O)', font = ('Times', 15, 'bold')
        ,fg = '#ffffff', bg = '#960000').pack(pady = 10)


    #Player 2 entry
    player2 = Entry(tictactoewindow, font = ('Times', 15, 'bold')
        ,fg = '#000000')
    player2.pack(pady = 10)


    start_game_btn = Button(tictactoewindow, text = 'Start Game',font=('Times 15 bold')
        ,fg = "#000000", bg = "#00FCEB", command = start_game).pack(pady = 10)



#doodle variables

#variable
pen_width = 2
current_color = "black"
last_x = None
last_y = None



#DOODLE--*----*----*----*----*----*----*----*----*----*----*--
def doodle():
    win = Toplevel(root)
    win.title("Let's Doodle")



    #---------------------------
    def open_color_picker():
        global current_color
        color_code = askcolor(color=current_color) [1] #index num1 gives you hexadecimal value  # ((255 ,0 , 0), "#ff0000")
        if color_code:
            current_color = color_code
            color_picker_button.config(bg=color_code)

    def update_pen_width(val):
        global pen_width
        pen_width = int(float(val)) #convert the str to float first then to int

    def paint(event): 
        global last_x , last_y
        x , y = event.x , event.y
        if last_x and last_y:
            canvas.create_line(last_x , last_y , x, y, fill = current_color, width = pen_width, capstyle = ROUND , smooth=True)
        
        last_x , last_y = x , y

    def reset(event):
        global last_y, last_x
        last_x , last_y = None, None


    #DESIGN DOODLE ------------------------------------------------------------________________
    canvas = Canvas(win, bg = "white" , width = 800, height = 500)
    canvas.pack(side = LEFT, fill = BOTH, expand = True)


    btn_frame = Frame(win)
    btn_frame.pack(side = RIGHT, fill = Y)


    color_picker_button = Button(btn_frame , text = "Pick A Color" , font = ("Comic Sans MS" , 15)
                ,fg = 'white', bg = '#A4067A', command=open_color_picker)
    color_picker_button.pack(pady = 20)

    pen_slider = Scale(btn_frame, from_ = 1, to_ = 50, orient = HORIZONTAL, command = update_pen_width)
    pen_slider.set(pen_width)
    pen_slider.pack(pady = 10)


    #EVENT BINDING
    canvas.bind("<B1-Motion>" , paint)
    canvas.bind("<ButtonRelease-1>" , reset)



#clicker variables
score = 0
clickingpower = 1
upgradecost = 10

def clicker():
    clickerwin = Toplevel(root)
    clickerwin.title("Clicker Game")
    clickerwin.geometry("400x400")
    clickerwin.configure(bg = "#f4f9f9")


    #Functions
    def clicker():
        global score
        score += clickingpower
        Labelscore.config(text = f"Score: {score}")

    def showupgrade():
        upgradeframe.pack(pady = 5, fill = BOTH , expand = True)
        
    def buyupgrade():
        global score, clickingpower, upgradecost
        if score >= upgradecost:
            score = score - upgradecost
            clickingpower = clickingpower+1
            upgradecost *= 2
            Labelscore.config(text = f"Score: {score}")
            clickp.config(text = f"Clicking Power: {clickingpower}")
            upgradec.config(text = f"Upgrade Cost: {upgradecost}")
            not_enough_points.config(text = "")
        else:
            not_enough_points.config(text = "Not enough points!")

    def reset():
        global score, clickingpower, upgradecost
        score = 0
        clickingpower = 1
        upgradecost = 10
        Labelscore.config(text = f"Score: {score}")
        clickp.config(text = f"Clicking Power: {clickingpower}")
        upgradec.config(text = f"Upgrade Cost: {upgradecost}")
        not_enough_points.config(text = "")
        upgradeframe.pack_forget()


    #Design-------------------------------------------------------------------------
    #First Frame--------------------------------------------------
    clicker_frame = Frame(clickerwin ,bg = "#f4f9f9")
    clicker_frame.pack(pady = 5, fill = BOTH , expand = True)



    #Score label
    Labelscore = Label(clicker_frame, text = f"Score = 0" , 
            fg = "#000000" , font = ("Comic Sans MS" , 16 , "bold") , 
            bg = "#f4f9f9")
    Labelscore.pack(pady=5)
    #Click Me Button
    clickerb = Button(clicker_frame, text="Click Me!", fg = "#f0f0f0",bg = "#1E7413" ,font= ("Comic Sans MS", 10, "bold"), command = clicker)
    clickerb.pack(pady=5)
    #Show Upgrades Button
    showupgrades = Button(clicker_frame, text="Show Upgrades", fg = "#f0f0f0",bg = "#09505A" ,font= ("Comic Sans MS", 10, "bold"), command=showupgrade)
    showupgrades.pack(pady = 5)

    #Reset Button
    resetb = Button(clicker_frame, text="Reset", fg = "#f0f0f0",bg = "#FF0000" ,font= ("Comic Sans MS", 10, "bold"), command=reset)
    resetb.pack(pady=5)

    #Label not enough points
    not_enough_points = Label(clicker_frame, text = "" , 
            fg = "#C60000" , font = ("Comic Sans MS" , 7 , "bold") , 
            bg = "#f4f9f9")
    not_enough_points.pack(pady=5)


    #Second frame(upgrade frame)----------------------------------------------
    upgradeframe = Frame(clickerwin ,bg = "#f4f9f9")
    #upgradeframe.pack(pady = 5, fill = BOTH , expand = True)




    #clicking power
    clickp = Label(upgradeframe, text = "Clicking Power: 1" , 
            fg = "#000000" , font = ("Comic Sans MS" , 10 , "bold") , 
            bg = "#F4F9F9")
    clickp.pack(pady=5)

    #upgrade cost
    upgradec = Label(upgradeframe, text = "Upgrade Cost: 10" , 
            fg = "#000000" , font = ("Comic Sans MS" , 10 , "bold") , 
            bg = "#F4F9F9")
    upgradec.pack(pady=5)

    #Buy upgrade
    buyup = Button(upgradeframe, text="Buy Upgrade", fg = "#f0f0f0",bg = "#FF890C" ,font= ("Comic Sans MS", 10, "bold"), command=buyupgrade)
    buyup.pack(pady=5)




def travelplanner():
    travel = Toplevel(root)
    travel.title("Travel Planner")
    travel.geometry("600x700")
    travel.configure(bg="#B3F3E7")

    #function

    def submit():
        trip = trip_type.get()
        dest = dest_var.get()
        transport = tran_var.get()

        extra = []
        if var_hotel.get():extra.append('Hotel Booking')
        if var_pickup.get(): extra.append("Airport")
        if var_insurance.get(): extra.append("Travel Insurance")

        extra_str = ", ".join(extra) if extra else "No additional Services Selected"

        lbl_output.config(text = f"🧑🧑🧒🧒Trip Type: {trip}\n🏞️Destination: {dest}\n✈️Transport: {transport}\n✨Extras: {extra_str}" , fg = "#054d4c")








    #Design ---------------------------------------

    #title
    Label(travel , text = "✈️Plan Your Trip" , font = ("Helvetica" , 20 , "bold"), 
        bg = "#07473B" , fg = "white").pack(fill = X , padx = 10 , pady = 10)

    #trip type
    Label(travel , text = "Choose Trip Type" , font = ("Helvetica" , 10 , "bold") ,
        bg = "#B3F3E7" , fg = "#07473B").pack(pady = 10)

    #radio Btns
    trip_type = StringVar(value = "Solo")
    """
    Radiobutton(travel , text = "Solo" ,variable= trip_type , value= "Solo" ,font = ("Helvetica" , 16 , "bold") ,
                bg = "#B3F3E73" , fg = "#07473B").pack(anchor= W , padx = 30)
    Radiobutton(travel , text = "Couple" ,variable= trip_type , value= "Couple" ,font = ("Helvetica" , 16 , "bold") ,
                bg = "#B3F3E73" , fg = "#07473B").pack(anchor= W , padx = 30)
    Radiobutton(travel , text = "Family" ,variable= trip_type , value= "Family" ,font = ("Helvetica" , 16 , "bold") ,
                bg = "#B3F3E73" , fg = "#07473B").pack(anchor= W , padx = 30)
    """
    for text in ["Solo" , "Couple" , "Family"]:
        Radiobutton(travel , text = text ,variable= trip_type , value= text ,font = ("Helvetica" , 10 , "bold") ,
                    bg = "#B3F3E7" , fg = "#07473B").pack(anchor= W , padx = 30,pady = 5)


    #Destination

    Label(travel , text = "Choose Your Destination" , font = ("Helvetica" , 10, "bold"), 
        bg = "#B3F3E7" , fg = "#07473B").pack(fill = X , padx = 10 , pady = 10)

    dest_var = StringVar(value = "Select")
    dest_menu = Combobox(travel, textvariable=dest_var , values = ["Paris" , "Singapore" , "Goa" , "New York" , "Dubai"] ,font = ("Helvetica" , 10 , "bold"))
    dest_menu.pack(pady = 10 , fill = X , padx = 100)

    #Transport 
    Label(travel , text = "Choose Your Transport" , font = ("Helvetica" , 10 , "bold"), 
        bg = "#B3F3E7" , fg = "#07473B").pack(fill = X , padx = 10 , pady = 10)


    tran_var = StringVar(value = "Flight")
    trans_menu = Combobox(travel, textvariable=tran_var , values = ["Car🚗" , "Flight✈️" , "Train🚇" , "Bus🚌"] ,font = ("Helvetica" , 10 , "bold"))
    trans_menu.pack(pady = 10 , fill = X , padx = 100)


    #additional services
    Label(travel , text = "Additional Services" , font = ("Helvetica" , 10 , "bold"), 
        bg = "#B3F3E7" , fg = "#07473B").pack(fill = X , padx = 10 , pady = 10)

    var_hotel = IntVar()
    var_pickup = IntVar()
    var_insurance = IntVar()

    Checkbutton (travel, text = "🏨Hotel Booking" , variable= var_hotel ,  font = ("Helvetica" , 10 , "bold"), 
        bg = "#B3F3E7" , fg = "#07473B").pack(fill = X , padx = 30 , pady = 5, anchor = W)

    Checkbutton (travel, text = "🚕Airport Pickup" , variable= var_pickup ,  font = ("Helvetica" , 10 , "bold"), 
        bg = "#B3F3E7" , fg = "#07473B").pack(fill = X , padx = 30 , pady = 5, anchor = W)

    Checkbutton (travel, text = "💰Travel Insurance" , variable= var_insurance ,  font = ("Helvetica" , 10 , "bold"), 
        bg = "#B3F3E7" , fg = "#07473B").pack(fill = X , padx = 30 , pady = 5 , anchor = W)

    Button(travel , text = "Plan My Trip" ,  font = ("Helvetica" , 10 , "bold"), 
        bg = "#B3F3E7" , fg = "#07473B", command = submit).pack(fill = X , padx = 10 , pady = 10)


    # Output Label
    lbl_output = Label(travel, text="", font=("Helvetica", 10), bg="#B3F3E7")
    lbl_output.pack(pady=10)


#RPS variables
choices = ["r", "p", "s"]#list
name = {"r" : "Rock", 
        "p" : "Paper",
        "s" : "scissors"}#dictionary = storing data in key:value format

player_score = 0
comp_score = 0


def rps():

    rpswin = Toplevel(root)
    rpswin.title("Rock Paper Scissors")
    rpswin.geometry("500x500")
    rpswin.configure(bg="lightblue")

    def reset():
        global player_score, comp_score
        player_score = 0
        comp_score = 0
        lbl_p_score.config(text="Player Score: 0")
        lbl_c_score.config(text="Computer Score: 0")
        lbl_player.config(text="")
        lbl_comp.config(text="")
        lbl_result.config(text="")

    def play(user_choice):
        global player_score, comp_score

        computer = random.choice(choices)

        lbl_player.config(text=f"Player: {name[user_choice]}")
        lbl_comp.config(text=f"Computer: {name[computer]}")

        if user_choice == computer:
            lbl_result.config(text="It's a Tie!")
        elif (user_choice == "r" and computer == "s") or \
             (user_choice == "p" and computer == "r") or \
             (user_choice == "s" and computer == "p"):

            player_score += 1
            lbl_result.config(text="Player Wins!")

        else:
            comp_score += 1
            lbl_result.config(text="Computer Wins!")

        lbl_p_score.config(text=f"Player Score: {player_score}")
        lbl_c_score.config(text=f"Computer Score: {comp_score}")

    # IMAGE LOADER
    def load_image(filename):
        img = Image.open(filename)
        img = img.resize((120,120))
        return ImageTk.PhotoImage(img)

    rock_img = load_image("rock.png")
    paper_img = load_image("paper.png")
    scissors_img = load_image("scissors.png")

    # TITLE
    Label(rpswin, text="Rock Paper Scissors",
          bg="lightblue", fg="black",
          font=("Comic Sans MS",20,"bold")
    ).grid(row=0, column=0, columnspan=3, pady=20)

    # BUTTONS
    rock_btn = Button(rpswin, image=rock_img, text="Rock",
                      compound=TOP, bg="lightcoral",
                      command=lambda: play("r"))
    rock_btn.grid(row=1, column=0, padx=10, pady=10)
    rock_btn.image = rock_img

    paper_btn = Button(rpswin, image=paper_img, text="Paper",
                       compound=TOP, bg="lightyellow",
                       command=lambda: play("p"))
    paper_btn.grid(row=1, column=1, padx=10, pady=10)
    paper_btn.image = paper_img

    scissors_btn = Button(rpswin, image=scissors_img, text="Scissors",
                          compound=TOP, bg="lightgreen",
                          command=lambda: play("s"))
    scissors_btn.grid(row=1, column=2, padx=10, pady=10)
    scissors_btn.image = scissors_img

    # RESULT
    lbl_result = Label(rpswin, text="",
                       font=("Comic Sans MS",16,"bold"),
                       bg="lightblue", fg="red")
    lbl_result.grid(row=2, column=0, columnspan=3, pady=10)

    # PLAYER CHOICE
    lbl_player = Label(rpswin, text="",
                       font=("Comic Sans MS",14,"bold"),
                       bg="lightblue")
    lbl_player.grid(row=3, column=0, columnspan=3)

    # COMPUTER CHOICE
    lbl_comp = Label(rpswin, text="",
                     font=("Comic Sans MS",14,"bold"),
                     bg="lightblue")
    lbl_comp.grid(row=4, column=0, columnspan=3)

    # SCORES
    lbl_p_score = Label(rpswin, text="Player Score: 0",
                        font=("Comic Sans MS",14,"bold"),
                        bg="lightblue")
    lbl_p_score.grid(row=5, column=0, pady=10)

    lbl_c_score = Label(rpswin, text="Computer Score: 0",
                        font=("Comic Sans MS",14,"bold"),
                        bg="lightblue")
    lbl_c_score.grid(row=5, column=2, pady=10)

    # RESET BUTTON
    Button(rpswin, text="Reset",
           bg="orangered", fg="white",
           font=("Arial",12,"bold"),
           command=reset
    ).grid(row=6, column=0, columnspan=3, pady=15)


#Sci cal variables
field_text = ''

#CALCULATOR-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cal():



    calwin = Tk()
    calwin.title("Calculator")
    calwin.config(bg = "#000000")



    def click(num):
        global field_text
        field_text = field_text + str(num)
        txt.config(state = 'normal')
        txt.delete(0, END)
        txt.insert(0, field_text)
        txt.config(state = 'readonly')

    def clear():
        global field_text
        field_text = ''
        txt.config(state = 'normal')#temporarily set to normal to insert the new text
        txt.delete(0, END)
        txt.config(state = 'readonly')

    def equal():
        global field_text
        result = str(eval(field_text))#evaluate the string as an arthmetic equation
        txt.config(state = 'normal')
        txt.delete(0, END)#delete all the text frm entry
        txt.insert(0, result)#insert the text in entry
        field_text = str(result)
        txt.config(state = 'readonly') 


    def sci(func):
        global field_text
        num = float(field_text)
        if func == "sin":
            result = math.sin(math.radians(num))
        elif func == "tan":
            result = math.tan(math.radians(num))
        elif func == "cos":
            result = math.cos(math.radians(num))
        elif func == "log":
            result = math.log10(num)
        elif func == "sqrt":#SQUARE ROOT
            result = math.sqrt(num)
        elif func == "cbrt":#CUBE ROOT
            result = num ** (1/3)
        txt.config(state = 'normal')
        txt.delete(0, END)#delete all the text frm entry
        txt.insert(0, result)#insert the text in entry
        field_text = str(result)
        txt.config(state = 'readonly') 
        











    # -------- DISPLAY -------- #

    txt = Entry(calwin,font=("Arial",22),width=22,
                justify="right",borderwidth=6,state="readonly")
    txt.grid(row=0,column=0,columnspan=5,padx=12,pady=10)

    # -------- SCIENTIFIC ROW 1 -------- #
    Button(calwin,text="sin",bg="#6c5ce7",fg="white", width = 10,
                    command=lambda:sci("sin")).grid(row=1,column=0, pady = 2)

    Button(calwin,text="cos",bg="#6c5ce7",fg="white", width = 10,
                    command=lambda:sci("cos")).grid(row=1,column=1)

    Button(calwin,text="tan",bg="#6c5ce7",fg="white", width = 10,
                    command=lambda:sci("tan")).grid(row=1,column=2)

    Button(calwin,text="log",bg="#6c5ce7",fg="white", width = 10,
                    command=lambda:sci("log")).grid(row=1,column=3)

    Button(calwin,text="π",bg="#6c5ce7",fg="white", width = 10,
                    command=lambda:click(str(math.pi))).grid(row=1,column=4)

    # -------- SCIENTIFIC ROW 2 -------- #
    Button(calwin,text="√",bg="#6c5ce7",fg="white",width = 10,
                    command=lambda:sci("sqrt")).grid(row=2,column=0, pady = 2)

    Button(calwin,text="∛",bg="#6c5ce7",fg="white",width = 10,
                    command=lambda:sci("cbrt")).grid(row=2,column=1)

    Button(calwin,text="xʸ",bg="#6c5ce7",fg="white",width = 10,
                    command=lambda:click("**")).grid(row=2,column=2)

    Button(calwin,text="(",bg="#6c5ce7",fg="white",width = 10,
                    command=lambda:click("(")).grid(row=2,column=3)

    Button(calwin,text=")",bg="#6c5ce7",fg="white",width = 10,
                    command=lambda:click(")")).grid(row=2,column=4)

    # -------- NUMBERS AND OPERATORS-------- #
    Button(calwin,text="7",bg="#4da6ff",width = 10,
                    command=lambda:click(7)).grid(row=3,column=0, pady = 2)

    Button(calwin,text="8",bg="#4da6ff",width = 10,
                    command=lambda:click(8)).grid(row=3,column=1)

    Button(calwin,text="9",bg="#4da6ff",width = 10,
                    command=lambda:click(9)).grid(row=3,column=2)

    Button(calwin,text="/",bg="#ff944d",width = 10,
                    command=lambda:click("/")).grid(row=3,column=3)

    Button(calwin,text="*",bg="#ff944d",width = 10,
                    command=lambda:click("*")).grid(row=3,column=4)



    Button(calwin,text="4",bg="#4da6ff",width = 10,
                    command=lambda:click(4)).grid(row=4,column=0, pady = 2)

    Button(calwin,text="5",bg="#4da6ff",width = 10,
                    command=lambda:click(5)).grid(row=4,column=1)

    Button(calwin,text="6",bg="#4da6ff",width = 10,
                    command=lambda:click(6)).grid(row=4,column=2)

    Button(calwin,text="-",bg="#ff944d",width = 10,
                    command=lambda:click("-")).grid(row=4,column=3)

    Button(calwin,text="+",bg="#ff944d",width = 10,
                    command=lambda:click("+")).grid(row=4,column=4)
    Button(calwin,text="1",bg="#4da6ff",width = 10,
                    command=lambda:click(1)).grid(row=5,column=0)

    Button(calwin,text="2",bg="#4da6ff",width = 10,
                    command=lambda:click(2)).grid(row=5,column=1, pady = 2)

    Button(calwin,text="3",bg="#4da6ff",width = 10,
                    command=lambda:click(3)).grid(row=5,column=2)

    Button(calwin,text="0",bg="#4da6ff",width = 10,
                    command=lambda:click(0)).grid(row=5,column=3)

    Button(calwin,text=".",bg="#4da6ff",width = 10,
                    command=lambda:click(".")).grid(row=5,column=4)
    # -------- BOTTOM -------- #

    Button(calwin,text="CLEAR",bg="#e74c3c",fg="white",
                    width=20,command=clear).grid(row=6,column=0,columnspan=2,pady=5,padx=5)

    Button(calwin,text="=",bg="#27ae60",fg="white",
                    width=30,command=equal).grid(row=6,column=2,columnspan=3,padx=5)



#DESIGN------------------------------------------------------------------------------------------------------


#LOGIN SCREEN
login_frame = Frame(root , bg = "#000")
login_frame.pack(pady = 10)

#"Login Here!"
login1 = Label(login_frame, text = "Login Here!" , 
           fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

login1.grid(row = 0, column=0, columnspan=3)




#username
user1 = Label(login_frame, text = "Username:" , 
           fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

user1.grid(row = 1, column=0,pady = 20,padx = 20)

userentry = Entry(login_frame, fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

userentry.grid(row = 1, column=1,pady = 20,padx = 5)


#password
password1 = Label(login_frame, text = "Password" , 
           fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

password1.grid(row = 2, column=0,pady = 20,padx = 20)

passwordentry = Entry(login_frame, fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000", show='*')

passwordentry.grid(row = 2, column=1,pady = 20,padx = 5)








#login button(lb)
b1 = Button(login_frame, text = "Login" , 
           fg = "#00FFFF" , font = ("Arial" , 20 , "bold"), 
           bg = "#000000",
           command = login)

b1.grid(row = 4 ,column=0 ,columnspan=2)



#SELECT GAME WINDOW----------------------------------
select_game = Frame(root , bg = "#000") # Have packed in function

#TITLE-----------------------------------------------
title = Label(select_game , text = "Multitasker\nWe have a wide selection of activites.\nPlease pick one." , font = ("Helvetica 16 bold") , fg = "#0AFFDA" , bg = "#000")
title.pack(pady = 5)

#tic tac toe btn
tictactoebtn = Button(select_game , text = "Tic Tac Toe" , font = ("Helvetica 16 bold") , bg = "#1B75CF" , fg = "#000" , command = tic_tac_toe)
tictactoebtn.pack(pady = 5)


#Doodle Button

doodlebtn = Button(select_game , text = "Doodle" , font = ("Helvetica 16 bold") , bg = "#CF481B" , fg = "#000" , command = doodle)
doodlebtn.pack(pady = 5)


#CLICKER button
clickerbtn = Button(select_game , text = "Clicker Game" , font = ("Helvetica 16 bold") , bg = "#2DCF1B" , fg = "#000" , command = clicker)
clickerbtn.pack(pady = 5)



travelbtn = Button(select_game , text = "Travel Planner" , font = ("Helvetica 16 bold") , bg = "#10FFD3" , fg = "#000" , command = travelplanner)
travelbtn.pack(pady = 5)

rpsbtn = Button(select_game , text = "Rock Paper Scissors" , font = ("Helvetica 16 bold") , bg = "#ff9100" , fg = "#000" , command = rps)
rpsbtn.pack(pady = 5)

calbtn = Button(select_game , text = "Scientific Calculator" , font = ("Helvetica 16 bold") , bg = "#831fff" , fg = "#000" , command = cal)
calbtn.pack(pady = 5)



mainloop()