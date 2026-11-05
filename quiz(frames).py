from tkinter import *


win = Tk()
win.geometry("500x400")
win.title("QUIZ")
win.configure(bg='#f0f0f0')


score = 0

frame1_color = "#DDF885"
frame2_color = "#72F5D7"
frame3_color = "#EAAAF7"
score_frame_color = "#08BC9E"
text_color = "#000000"
btn_color = "#F28545"
correct_color = "#105107"
wrong_color = "#F50505"

#----------------------------Function===========
def update_score(points):
    global score
    score += points
    return score


#--------------QUES 1
def chk_ans():
    global score
    if a1.get() == 'Paris':
        result1.config(text = "Correct Answer !" , fg = correct_color)
        submit1.config(state = DISABLED)
        next1.config(state = NORMAL)
        update_score(10)
    else:
        result1.config(text = 'Wrong Answer !' , fg = wrong_color)
        submit1.config(state = DISABLED)
        next1.config(state = NORMAL)


def next_1():
    frame1.pack_forget()
    frame2.pack(padx = 20, pady = 20, fill = BOTH , expand = True)

#===================== FRAME 1 - QUES 1 =====================

frame1 = Frame(win, bg = frame1_color)
frame1.pack(padx = 20, pady = 20, fill = BOTH , expand = True)

#ques 1

q1 = Label(frame1, text = "What is the capital of France?", 
           fg = text_color , bg = frame1_color , font = ('Arial' , 18))
q1.pack(padx = 10 , pady=10)

a1 = StringVar() #to store the answer

option1 = Radiobutton(frame1 , text = "Paris", variable = a1 , value = 'Paris' ,fg = text_color , bg = frame1_color)
option1.pack(padx = 10, pady = 10, anchor= W)
option2 = Radiobutton(frame1 , text = "Milan", variable = a1 , value = 'Milan' ,fg = text_color , bg = frame1_color)
option2.pack(padx = 10, pady = 10, anchor= W)
option3 = Radiobutton(frame1 , text = "Barcelona", variable = a1 , value = 'Barcelona', fg = text_color , bg = frame1_color)
option3.pack(padx = 10, pady = 10, anchor= W)

submit1 = Button(frame1, text = 'Submit' ,bg = btn_color, fg = text_color , font = ('Arial' , 15, 'bold'), command=chk_ans)
submit1.pack(padx = 10, pady = 10)

next1 = Button(frame1, text = 'Next' , state = DISABLED, bg = btn_color, fg = text_color , font = ('Arial' , 15, 'bold'), command = next_1)
next1.pack(padx = 10, pady = 10)

result1 = Label(frame1, bg = frame1_color , font = ('Arial' , 12, 'bold'))
result1.pack(padx = 10, pady = 10)


#===================== FRAME 2 - QUES 2 =====================
frame2 = Frame(win, bg = frame2_color)

#--------------QUES 2
def chk_ans2():
    global score
    if a2.get() == 'New Delhi':
        result2.config(text = "Correct Answer !" , fg = correct_color)
        submit2.config(state = DISABLED)
        next2.config(state = NORMAL)
        update_score(10)
    else:
        result2.config(text = 'Wrong Answer !' , fg = wrong_color)
        submit2.config(state = DISABLED)
        next2.config(state = NORMAL)


def next_2():
    frame2.pack_forget()
    frame3.pack(padx = 20, pady = 20, fill = BOTH , expand = True)

#ques 2

q2 = Label(frame2, text = "What is the capital of India?", 
           fg = text_color , bg = frame1_color , font = ('Arial' , 18))
q2.pack(padx = 10 , pady=10)

a2 = StringVar() #to store the answer

option4 = Radiobutton(frame2 , text = "Kolkata", variable = a2 , value = 'Kolkata' ,fg = text_color , bg = frame2_color)
option4.pack(padx = 10, pady = 10, anchor= W)
option5 = Radiobutton(frame2 , text = "New Delhi", variable = a2 , value = 'New Delhi' ,fg = text_color , bg = frame2_color)
option5.pack(padx = 10, pady = 10, anchor= W)
option6 = Radiobutton(frame2 , text = "Bangalore", variable = a2 , value = 'Bangalore', fg = text_color , bg = frame2_color)
option6.pack(padx = 10, pady = 10, anchor= W)

submit2 = Button(frame2, text = 'Submit' ,bg = btn_color, fg = text_color , font = ('Arial' , 15, 'bold'), command=chk_ans2)
submit2.pack(padx = 10, pady = 10)

next2 = Button(frame2, text = 'Next' , state = DISABLED, bg = btn_color, fg = text_color , font = ('Arial' , 15, 'bold'), command = next_2)
next2.pack(padx = 10, pady = 10)

result2 = Label(frame2, bg = frame2_color , font = ('Arial' , 12, 'bold'))
result2.pack(padx = 10, pady = 10)



#===================== FRAME 3 - QUES 3 =====================
frame3 = Frame(win, bg = frame3_color)

#--------------QUES 3
def chk_ans3():
    global score
    if a3.get() == 'Hanoi':
        result3.config(text = "Correct Answer !" , fg = correct_color)
        submit3.config(state = DISABLED)
        next3.config(state = NORMAL)
        update_score(10)
    else:
        result3.config(text = 'Wrong Answer !' , fg = wrong_color)
        submit3.config(state = DISABLED)
        next3.config(state = NORMAL)


def next_3():
    frame3.pack_forget()
    frame4.pack(padx = 20, pady = 20, fill = BOTH , expand = True)
    end.config(text = f"Hope you enjoyed the quiz! \nYour total score is {score}")

#ques 3

q3 = Label(frame3, text = "What is the capital of Vietnam?", 
           fg = text_color , bg = frame3_color , font = ('Arial' , 18))
q3.pack(padx = 10 , pady=10)

a3 = StringVar() #to store the answer

option7 = Radiobutton(frame3 , text = "Hanoi", variable = a3 , value = 'Hanoi' ,fg = text_color , bg = frame3_color)
option7.pack(padx = 10, pady = 10, anchor= W)
option8 = Radiobutton(frame3 , text = "Laos", variable = a3 , value = 'Laos' ,fg = text_color , bg = frame3_color)
option8.pack(padx = 10, pady = 10, anchor= W)
option9 = Radiobutton(frame3 , text = "I dunno", variable = a3 , value = 'I dunno', fg = text_color , bg = frame3_color)
option9.pack(padx = 10, pady = 10, anchor= W)

submit3 = Button(frame3, text = 'Submit' ,bg = btn_color, fg = text_color , font = ('Arial' , 15, 'bold'), command=chk_ans3)
submit3.pack(padx = 10, pady = 10)

next3 = Button(frame3, text = 'Next' , state = DISABLED, bg = btn_color, fg = text_color , font = ('Arial' , 15, 'bold'), command = next_3)
next3.pack(padx = 10, pady = 10)

result3 = Label(frame3, bg = frame3_color , font = ('Arial' , 12, 'bold'))
result3.pack(padx = 10, pady = 10)


#===================== FRAME 4 - End =====================
frame4 = Frame(win, bg = score_frame_color)



#ques 3

end = Label(frame4, 
           fg = text_color , bg = frame1_color , font = ('Arial' , 18))
end.pack(padx = 10 , pady=50)











mainloop()