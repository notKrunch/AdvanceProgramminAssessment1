import tkinter as tk
from tkinter import messagebox



# Create the main window
main = tk.Tk()
main.title("Exercise3-Chapter5")

# Define a class to make the default values and set data for the employees
class Employees:
    def __init__(data):
        data.name = ""
        data.position = ""
        data.salary = 0.0
        data.id = 0

    def setData(data, name, position, salary, id):
        data.name = name
        data.position = position
        data.salary = salary
        data.id = id

    def getData(data):
        return f"{data.name}\t{data.position}\t{data.salary}\t{data.id}"

# Function to add an employee to the list
def addemployee():
    name = entryname.get()
    position = entryposition.get()
    salary = float(entrysalary.get())

    global idcounter
    idcounter += 1
    employeeid = idcounter

    employee = Employees()
    employee.setData(name, position, salary, employeeid)

    employees.append(employee)
    clearentries()

# Create a function to display the employee information
def displayemployees():
    resulttext.config(state="normal")
    resulttext.delete("1.0", tk.END) 

    resulttext.insert(tk.END, "Name\tPosition\tSalary\tID\n")

    # Display employee details
    for employee in employees:
        resulttext.insert(tk.END, employee.getData() + "\n")

    resulttext.config(state="disabled")

# Create a function to clear the entry typed
def clearentries():
    entryname.delete(0, tk.END)
    entryposition.delete(0, tk.END)
    entrysalary.delete(0, tk.END)



# Create labels and entry for name, position, and salary
labelname = tk.Label(main, text="Name:")
entryname = tk.Entry(main)

labelposition = tk.Label(main, text="Position:")
entryposition = tk.Entry(main)

labelsalary = tk.Label(main, text="Salary:")
entrysalary = tk.Entry(main)

# Create buttons to add employees and display employees
addbutton = tk.Button(main, text="Add Employee", command=addemployee)
displaybutton = tk.Button(main, text="Display Employees", command=displayemployees)

# Create text to show the results
resulttext = tk.Text(main, height=10, width=40)
resulttext.config(state="disabled")

# Create grids for the label and entry
labelname.grid(row=0, column=0, sticky="w")
entryname.grid(row=0, column=1)

labelposition.grid(row=1, column=0, sticky="w")
entryposition.grid(row=1, column=1)

labelsalary.grid(row=2, column=0, sticky="w")
entrysalary.grid(row=2, column=1)

addbutton.grid(row=3, column=0, columnspan=2, pady=10)
displaybutton.grid(row=4, column=0, columnspan=2, pady=10)

resulttext.grid(row=5, column=0, columnspan=2, pady=10)

# Initialize variables
employees = []
idcounter = 0

# Run the gui
main.mainloop()
