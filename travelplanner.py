
from tkinter import *
from tkinter.ttk import Combobox



travel = Tk()
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

mainloop()