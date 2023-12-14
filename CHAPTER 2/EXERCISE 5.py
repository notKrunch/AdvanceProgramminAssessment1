from tkinter import *

# Function for calculation of addition, subtraction, multiplication, divison, and remainder
def calculator(operation):
    try:
        num1 = float(num1entry.get())
        num2 = float(num2entry.get())

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2
        elif operation == "Remainder":
            result = num1 % num2
        else:
            raise ValueError("Invalid operation")

        resultlabel.config(text=f"Result: {result: }", fg="green")
    except ValueError as e:
        resultlabel.config(text=f"Error: {str(e)}", fg="red")

# Create main window
main = Tk()
main.title("Exercise5-Chapter2")
main.geometry('250x280')
main.resizable(0, 0)

# Labels and entry for entering the 2 numbers
Label(main, text="Enter a number:").grid(row=0, column=0, padx=10, pady=5, sticky="E")
num1entry = Entry(main)
num1entry.grid(row=0, column=1, padx=10, pady=5)

Label(main, text="Enter a number:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
num2entry = Entry(main)
num2entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons for choosing the arithmetic operation you want to calculate
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Remainder"]
for i, operation in enumerate(operations):
    Button(main, text=operation, command=lambda op=operation: calculator(op)).grid(row=i + 2, column=0, columnspan=2, padx=10, pady=5)

resultlabel = Label(main, text="Result:", fg="black")
resultlabel.grid(row=len(operations) + 2, column=0, columnspan=2, padx=10, pady=5)

# Run the gui
main.mainloop()

