from tkinter import *
clickerwin = Tk()
clickerwin.title("Clicker Game")
clickerwin.geometry("400x400")
clickerwin.configure(bg = "#f4f9f9")


#Functions
score = 0
clickingpower = 1
upgradecost = 10
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



mainloop()