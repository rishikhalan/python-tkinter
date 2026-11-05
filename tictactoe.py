from tkinter import *
import tkinter.messagebox as msg



#variables
count = 0
mark = ''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
panels = ['panel'] * 10





def win(panels , sign):
    return((panels[1] == panels[2] == panels[3] == sign)
           or (panels[4] == panels[5] == panels[6] == sign)
           or (panels[7] == panels[8] == panels[9] == sign)
           or (panels[1] == panels[4] == panels[7] == sign)
           or (panels[2] == panels[5] == panels[8] == sign)
           or (panels[3] == panels[6] == panels[9] == sign)
           or (panels[1] == panels[5] == panels[9] == sign)
           or (panels[3] == panels[5] == panels[7] == sign))






def checker(digit):
    global count, mark, digits

    if digit in digits:
        digits.remove(digit)
        mark = 'X' if count % 2 == 0 else 'O'
        panels[digit] = mark
        count += 1
        eval(f'button{digit}.config(text = mark)')

        if win(panels,mark):
            if mark == "X":
                score_x.set(score_x.get() +1)
                msg.showinfo("Result" , f"{p1_name} Wins!")
            else:
                score_o.set(score_o.get() +1)
                msg.showinfo("Result" , f"{p2_name} Wins!")
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

     if not p1_name or not p2_name:
         msg.showerror(title='Input Error', message = 'Please enter names of both the players!')
         return
     tictactoewindow.destroy()
     create_game_screen()













#Game screen
def create_game_screen():
    gamescreen = Tk()
    gamescreen.title('Tic Tac Toe Game')
    gamescreen.config(bg = 'white')

    global score_x, score_o, button1, button2, button3, button4, button5, button6, button7, button8, button9    
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


    #score variables
    score_x = IntVar(value = 0)
    score_o = IntVar(value = 0)

    Label(gamescreen, textvariable=score_x, bg = '#ffffff', fg = "#0015FF", font = ('Comic Sans MS', 15, 'bold')).grid(row = 1, column = 1, padx = 5, pady = 5)
    Label(gamescreen, textvariable=score_o, bg = '#ffffff', fg = "#FF0000", font = ('Comic Sans MS', 15, 'bold')).grid(row = 1, column = 3, padx = 5, pady = 5)
    
    
    reset = Button(gamescreen, text = 'Reset',font=('Times 20 bold')
     ,fg = "#FFFFFF", bg = "#ef0e0e", command = reset_game).grid(row=5, column=1, columnspan=3, pady = 10)



#Home Screen----------------------------------------------------------------------------------------------
tictactoewindow = Tk()
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

mainloop()
