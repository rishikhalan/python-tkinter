from tkinter import *
import calendar



def show_calendar():
    calendar_window = Toplevel()
    calendar_window.config(bg = 'lightblue')
    calendar_window.title("Calendar for the Year")
    #calendar_window.geometry("850x650")

    year = int(year_input.get())

    #generate the calender
    calendar_content = calendar.calendar(year)

    cal_label = Label(calendar_window , text = calendar_content, bg = 'lightblue', 
                      fg = 'black', justify= LEFT , font = ("Courier New" , 14))
    cal_label.pack(padx = 20, pady = 20)









#main window ---------------------------------------------------------------
main = Tk()
main.config(bg = '#333333')
main.title('Calendar App')
main.geometry("300x300")

title = Label(main, text = "Calendar App", bg = '#333333', fg = '#ffffff', 
              font  = ('Times', 20, 'bold'))
title.pack(pady = 20)

lbl = Label(main, text = "Enter Year", bg = '#333333', fg = '#ffffff', 
              font  = ('Times', 15, 'bold'))
lbl.pack(pady = 20)

year_input = Entry(main,  font  = ('Times', 15))
year_input.pack(pady = 10)

Show_btn = Button(main , text = "Show Calendar" , bg = '#B10778', 
                  fg = 'white', font = ('Times', 15), command = show_calendar)
Show_btn.pack(pady = 20)

mainloop()
