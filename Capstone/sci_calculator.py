from tkinter import *
import math

calwin = Tk()
calwin.title("Calculator")
calwin.config(bg = "#000000")

field_text = ''

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

calwin.mainloop()