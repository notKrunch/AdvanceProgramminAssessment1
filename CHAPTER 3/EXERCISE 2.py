import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage

# Create main window
main = tk.Tk()
main.title("Exercise2-Chapter3")

# Create images on top of the window
image1 = PhotoImage(file="C:/Users/mrlum/Desktop/L5 ADVANCED PROGRAMMING 1ST SEM/ASSESSMENT 1/CHAPTER 3/cappuccino.png")
image2 = PhotoImage(file="C:/Users/mrlum/Desktop/L5 ADVANCED PROGRAMMING 1ST SEM/ASSESSMENT 1/CHAPTER 3/flat white.png")
image3 = PhotoImage(file="C:/Users/mrlum/Desktop/L5 ADVANCED PROGRAMMING 1ST SEM/ASSESSMENT 1/CHAPTER 3/spanish latte.png")
image4 = PhotoImage(file="C:/Users/mrlum/Desktop/L5 ADVANCED PROGRAMMING 1ST SEM/ASSESSMENT 1/CHAPTER 3/americano.png")
imagelabel1 = ttk.Label(main, image=image1)
imagelabel2 = ttk.Label(main, image=image2)
imagelabel3 = ttk.Label(main, image=image3)
imagelabel4 = ttk.Label(main, image=image4)
imagelabel1.grid(row=0, column=0, padx=5, pady=5)
imagelabel2.grid(row=0, column=1, padx=5, pady=5)
imagelabel3.grid(row=0, column=2, padx=5, pady=5)
imagelabel4.grid(row=0, column=3, padx=5, pady=5)

# Define coffee options
coffeeoptions = [
    "Cappuccino",
    "Flat White",
    "Spanish Latte",
    "Black Coffee",
]

# Define additional options
additionaloptions = [
    "Add Sugar",
    "No Sugar",
    "Add Milk",
    "No Milk",
    "None",
]

def selection():
    selectedcoffee = coffee.get()
    selectedadditional = additional.get()

    if selectedcoffee == "Select a Coffee" or selectedadditional == "Select Additional":
        messagebox.showerror("Error", "Please select a coffee and an option.")
    else:
        messagebox.showinfo("Order Details", f"Coffee: {selectedcoffee}/nAdditional Options: {selectedadditional}")



# Create coffee selection drop-down menu
coffee = tk.StringVar(main)
coffee.set("Select a Coffee")
coffeemenu = tk.OptionMenu(main, coffee, *coffeeoptions)
coffeemenu.grid(row=1, column=2, padx=5, pady=5)

# Create additional options drop-down menu
additional = tk.StringVar(main)
additional.set("Select Additional")
additionaloptionsmenu = tk.OptionMenu(main, additional, *additionaloptions)
additionaloptionsmenu.grid(row=2, column=2, padx=5, pady=5)


# Create order button
orderbutton = tk.Button(main, text="Order", command=selection)
orderbutton.grid(row=3, column=2, padx=5, pady=5)





# Run the gui
main.mainloop()