from tkinter import *

#function for login event
def login():
    user = entry1.get()
    pw = entry2.get()

    if user == "ryan123" and pw == "ryan123":
        status.config(text="Login successful! Welcome back, Ryan!", fg="green")
    else:
        status.config(text="Incorrect Username or Password!", fg="red")

#gui main window
main = Tk()
#title of gui
main.title("Exercise3-Chapter2")
#size of gui
main.geometry("250x150")
#gui is no longer resizable
main.resizable(0, 0)
#label and entry widgets for username and password
label1 = Label(main, text="USERNAME:")
label2 = Label(main, text="PASSWORD:")
entry1 = Entry(main)
entry2 = Entry(main, show="*")  # Show '*' for pw entry

#login button
button = Button(main, text="Login", command=login)

#login status
status = Label(main, text="", fg="black")

#labels to change the positioning of widgets
label1.grid(row=0, column=0, padx=10, pady=5, sticky="E")
entry1.grid(row=0, column=1, padx=10, pady=5)
label2.grid(row=1, column=0, padx=10, pady=5, sticky="E")
entry2.grid(row=1, column=1, padx=10, pady=5)
button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
status.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

#run gui
main.mainloop()