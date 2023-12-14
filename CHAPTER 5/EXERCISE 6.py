import tkinter as tk
from tkinter import ttk


 # Create main window
main = tk.Tk()
main.title("Exercise6-Chapter5")

class ArithmeticOperations:
    def __init__(data, main):
        # Create StringVar to show result
        data.result = tk.StringVar()
        data.result.set("Result: ")

        # Create label and entry for the 2 numbers
        data.label_num1 = ttk.Label(main, text="Enter Number 1:")
        data.entry_num1 = ttk.Entry(main)

        data.label_num2 = ttk.Label(main, text="Enter Number 2:")
        data.entry_num2 = ttk.Entry(main)

        # Create combobox for selecting arithmetic operation
        data.label_operation = ttk.Label(main, text="Select Operation:")
        data.operations = ttk.Combobox(main, values=["Addition", "Subtraction", "Multiplication", "Division"])
        data.operations.set("Addition")

        # Create Button to calculate
        data.calculate_button = ttk.Button(main, text="Calculate", command=data.calculate)

        # Create Label to show the result
        data.result_label = ttk.Label(main, textvariable=data.result)

        # Create grids for the label and entry
        data.label_num1.grid(row=0, column=0, padx=10, pady=10)
        data.entry_num1.grid(row=0, column=1, padx=10, pady=10)

        data.label_num2.grid(row=1, column=0, padx=10, pady=10)
        data.entry_num2.grid(row=1, column=1, padx=10, pady=10)

        data.label_operation.grid(row=2, column=0, padx=10, pady=10)
        data.operations.grid(row=2, column=1, padx=10, pady=10)

        data.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        data.result_label.grid(row=4, column=0, columnspan=2, pady=10)


    # Create a function to alculate the arithmetic operation
    def calculate(data):
        try:
            num1 = float(data.entry_num1.get())
            num2 = float(data.entry_num2.get())
            operation = data.operations.get()

            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                result = num1 / num2
            else:
                result = "Invalid operation"


            data.result.set(f"Result: {result}")

        except ValueError:
            data.result.set("Invalid input. Please enter valid numbers.")


# Run the gui
app = ArithmeticOperations(main)
main.mainloop()
