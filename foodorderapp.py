from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("Food Order App")
#root.geometry("400x400")
root.configure(bg="#ffffff")


#FUNCTIONS-----------------------------------------------------------------------
#Submit
def submit():
    meal = meal_pref.get()
    food = food_var.get()
    drink = drink_var.get()


    addons = []

    if var_soup.get():
        addons.append("Soup")
    if var_bruschetta.get():
        addons.append("Bruschetta")
    if var_springrolls.get():
        addons.append("Spring Rolls")

    if var_sandwich.get():
        addons.append("Sandwich")
    if var_burger.get():
        addons.append("Burger")
    if var_pasta.get():
        addons.append("Pasta")

    if var_icecream.get():
        addons.append("Ice Cream")
    if var_cake.get():
        addons.append("Cake")
    if var_brownie.get():
        addons.append("Brownie")
    if food == 'Select a Dish':
        food = "No Dish Selected"
    if drink == "Select a Drink":
        drink = "No Drink Selected"
    
    
    if addons:
        display_str = '--*--'.join(addons)
    else:
        display_str = "No additional items selected..."

    lblresult.config(text = f"Your order summary: \n\nPreferred Meal: {meal} \nMain Dish: {food} \n "
                     f"Additional Items: {display_str} \nDrink: {drink}")

#DESIGN------------------------------------------------------------------------------------
Label(root, text = 'Welcome to the Food Order App', font = ('Comic Sans MS', 16, 'bold'), 
      fg = '#ffffff', bg = "#107400").pack(pady = 10, fill = X)

Label(root, text = 'Select Your Meal Preference:', font = ('Comic Sans MS', 10, 'bold'), 
      fg = "#000000", bg = "#FFFFFF").pack(pady = 10, fill = X)

meal_pref = StringVar(value = "Veg")
#veg/veg with egg/nonveg
Radiobutton(root , text = "Veg", variable=meal_pref, value= "Veg" ,font = ("Helvetica" , 9 , "bold") ,
            fg = "#000000").pack(anchor= W , padx = 30)

Radiobutton(root , text = "Veg with Egg" ,variable=meal_pref, value= "Veg with Egg" ,font = ("Helvetica" , 9 , "bold") ,
            fg = "#000000").pack(anchor= W , padx = 30)


Radiobutton(root , text = "Nonveg",variable=meal_pref,  value= "Nonveg" ,font = ("Helvetica" , 9 , "bold") ,
            fg = "#000000").pack(anchor= W , padx = 30)




#Order dropdown
Label(root, text = 'What would you like to order?', font = ('Comic Sans MS', 10, 'bold'), 
      fg = "#000000", bg = "#FFFFFF").pack(pady = 10, fill = X)


food_var = StringVar()
food = Combobox(root, values = ["Select a Dish", "Pizza", "Lasagna", "Curry", "Dosa"] ,textvariable = food_var, font = ("Comic Sans MS" , 10 , "bold"))
food.pack(fill = X, padx = 5)


#Starters

Label(root, text = 'Starters', font = ('Comic Sans MS', 10, 'bold'), 
      fg = '#000000', bg = "#2CBBE7").pack(pady = 10, fill = X)

var_soup = IntVar()
var_bruschetta = IntVar()
var_springrolls = IntVar()

Checkbutton(root, text = 'Soup', variable=var_soup, font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)
Checkbutton(root, text = 'Bruschetta', variable=var_bruschetta,font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)
Checkbutton(root, text = 'Spring Rolls',variable=var_springrolls,  font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)


#Main Course

Label(root, text = 'Main Course', font = ('Comic Sans MS', 10, 'bold'), 
      fg = '#000000', bg = "#2CBBE7").pack(pady = 10, fill = X)

var_sandwich = IntVar()
var_burger = IntVar()
var_pasta = IntVar()

Checkbutton(root, text = 'Sandwich', variable=var_sandwich, font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)
Checkbutton(root, text = 'Burger', variable=var_burger, font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)
Checkbutton(root, text = 'Pasta', variable=var_pasta ,font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)


#Dessert

Label(root, text = 'Desserts', font = ('Comic Sans MS', 10, 'bold'), 
      fg = '#000000', bg = "#2CBBE7").pack(pady = 10, fill = X)

var_icecream = IntVar()
var_cake = IntVar()
var_brownie = IntVar()

Checkbutton(root, text = 'Ice Cream', variable=var_icecream, font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)
Checkbutton(root, text = 'Cake', variable=var_cake, font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)
Checkbutton(root, text = 'Brownie',variable=var_brownie, font = ('Comic Sans MS', 9), fg = '#000000').pack(anchor=W)


#Drink dropdown
Label(root, text = 'What would you like to drink?', font = ('Comic Sans MS', 10, 'bold'), 
      fg = "#000000", bg = "#FFFFFF").pack(pady = 10, fill = X)


drink_var = StringVar()
drink = Combobox(root, textvariable = drink_var, values = ["Select a Drink", "Thumbs Up", "Coke", "Sprite", "Lemonade"] ,font = ("Comic Sans MS" , 10 , "bold"))
drink.pack(fill = X, padx = 5)



#Submit Button

Button(root , text = "Submit" ,  font = ("Comic Sans MS" , 10 , "bold"), 
      command = submit, bg = "#007202" , fg = "#FFFFFF").pack(fill = X , padx = 10 , pady = 10)



#Result label
lblresult = Label(root, text = "", font= ("Helvetica", 14), wraplength = 500, bg = '#f0f4f7', fg = '#333' )
lblresult.pack(pady=20)



mainloop()
