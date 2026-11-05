from tkinter import *


win = Tk()
win.title("Calculator")
win.config(bg = "#000000")

field_text = ''

def buttn_click(num):
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
    txt.config(state = 'readonly') 
    field_text = ''

#widgets

Title = Label(win, text="Calculator" ,  
           fg = "#000000" , font = ("Comic Sans MS" , 30 , "bold" , "underline") , 
           bg = "#FFFFFF")

Title.grid(pady = 10 ,padx = 20 , columnspan=4)


txt = Entry(win, fg = "#000000" , font = ("Arial" , 20 , "bold") , 
           bg = "#000000", width=30, borderwidth=4, state="readonly")

txt.grid(pady = 10 ,padx = 20, row = 2 , columnspan = 4)


#Column 1(1, 4, 7, 0)------------------------------------
one = Button(win, text = "1" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(1))

one.grid(row = 4, column=0,pady = 10,padx = 20)


four = Button(win, text = "4" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(4))

four.grid(row = 5, column=0,pady = 10,padx = 20)

seven = Button(win, text = "7" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(7))

seven.grid(row = 6, column=0,pady = 10,padx = 20)


zero = Button(win, text = "0" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(0))

zero.grid(row = 7, column=0,pady = 10,padx = 20)


#Column 2(2, 5, 8, .)----------------------------------------------------------------------


two = Button(win, text = "2" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(2))

two.grid(row = 4, column=1,pady = 10,padx = 20)


five = Button(win, text = "5" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(5))

five.grid(row = 5, column=1,pady = 10,padx = 20)

eight = Button(win, text = "8" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click(8))

eight.grid(row = 6, column=1,pady = 10,padx = 20)


clearbttn = Button(win, text = "C" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000" , command = clear)

clearbttn.grid(row = 7, column=1,pady = 10,padx = 20)





#Column 3(3, 6, 9, =)----------------------------------------------------------------------


three = Button(win, text = "3" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000",  command = lambda : buttn_click(3))

three.grid(row = 4, column=2,pady = 10,padx = 20)


six = Button(win, text = "6" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000",  command = lambda : buttn_click(6))

six.grid(row = 5, column=2,pady = 10,padx = 20)

nine = Button(win, text = "9" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000",  command = lambda : buttn_click(9))

nine.grid(row = 6, column=2,pady = 10,padx = 20)


equalbttn = Button(win, text = "=" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000",  command = equal)

equalbttn.grid(row = 7, column=2,pady = 10,padx = 20)




#Column 4(+, -, *, /)----------------------------------------------------------------------


plus = Button(win, text = "+" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000",  command = lambda : buttn_click('+'))

plus.grid(row = 4, column=3,pady = 10,padx = 20)


minus = Button(win, text = "-" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click('-'))

minus.grid(row = 5, column=3,pady = 10,padx = 20)

times = Button(win, text = "*" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000", command = lambda : buttn_click('*'))

times.grid(row = 6, column=3,pady = 10,padx = 20)


divide = Button(win, text = "/" , 
           fg = "#FFFFFF" , font = ("Arial" , 30 , "bold") , 
           bg = "#000000",  command = lambda : buttn_click('/'))

divide.grid(row = 7, column=3,pady = 10,padx = 20)








mainloop()