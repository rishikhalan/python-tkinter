
from tkinter import *
from tkinter import messagebox



win = Tk()
win.geometry("400x340") #width x height
win.title("Login")
win.config(bg = "#000000")


#function----------------------------------------------
def login():
    username = 'abc'
    password = '12345'

    if userentry.get() == username and passwordentry.get() == password:
        messagebox.showinfo(title = "Login Success" , message = f"You are successfully logged in. \nWelcome {username}")
    else:
        messagebox.showerror(title = "Login Error" , message = 'Security breach... Invalid Credientials...')

















#DESIGN------------------------------------------------------------------------------------------------------

#"Login Here!"
login1 = Label(win, text = "Login Here!" , 
           fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

login1.grid(row = 0, column=0, columnspan=3)




#username
user1 = Label(win, text = "Username:" , 
           fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

user1.grid(row = 1, column=0,pady = 20,padx = 20)

userentry = Entry(win, fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

userentry.grid(row = 1, column=1,pady = 20,padx = 5)


#password
password1 = Label(win, text = "Password" , 
           fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000")

password1.grid(row = 2, column=0,pady = 20,padx = 20)

passwordentry = Entry(win, fg = "#00FFFF" , font = ("Arial" , 15 , "bold") , 
           bg = "#000000", show='*')

passwordentry.grid(row = 2, column=1,pady = 20,padx = 5)



#login button(lb)
b1 = Button(win, text = "Login" , 
           fg = "#00FFFF" , font = ("Arial" , 20 , "bold"), 
           bg = "#000000",
           command = login)

b1.grid(row = 4 ,column=0 ,columnspan=2)







mainloop()