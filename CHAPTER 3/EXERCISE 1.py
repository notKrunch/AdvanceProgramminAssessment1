import tkinter as tk
from tkinter import ttk

# Create main window
main = tk.Tk()
main.title("Exercise1-Chapter3")
main.resizable(0,0)

# Create a function for making the Input and Display Frame
class GreetingApp:
    def __init__(data, input):
        data.input = input

        # Create Input Frame
        data.inputframe = tk.Frame(data.input, bg='blue', padx=10, pady=10)
        data.inputframe.pack(padx=10, pady=10, side=tk.LEFT)

        tk.Label(data.inputframe, text="Personalized Greeting", font=('Helvetica', 14, 'bold'), fg='blue', bg='lightblue').grid(row=0, column=0, columnspan=2, pady=(0, 10))
        tk.Label(data.inputframe, text="Enter your name:", bg='white').grid(row=1, column=0, sticky='w', pady=5)

        data.nameentry = tk.Entry(data.inputframe)
        data.nameentry.grid(row=1, column=1, pady=5)

        tk.Label(data.inputframe, text="Select color:", bg='white').grid(row=2, column=0, sticky='w', pady=5)

        data.colorvar = tk.StringVar()
        data.colorvar.set("black")
        ttk.Combobox(data.inputframe, textvariable=data.colorvar, values=["black", "red", "green", "blue"]).grid(row=2, column=1, pady=5)

        tk.Button(data.inputframe, text="Update Greeting", command=data.greetingupdate).grid(row=3, column=0, columnspan=2, pady=10)

        # Create Display Frame 
        data.displayframe = tk.Frame(data.input, bg='lightgreen', padx=10, pady=10)
        data.displayframe.pack(padx=10, pady=10, side=tk.RIGHT)

        data.greetinglabel = tk.Label(data.displayframe, text="", font=('Helvetica', 14, 'bold'))
        data.greetinglabel.pack()

    def greetingupdate(data):
        name = data.nameentry.get()
        color = data.colorvar.get()
        greeting = f"Hello, {name}!"
        data.greetinglabel.config(text=greeting, fg=color)


# Run the gui
GreetingApp(main)
main.mainloop()
