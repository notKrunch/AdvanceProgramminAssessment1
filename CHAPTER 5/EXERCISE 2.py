import tkinter as tk
from tkinter import messagebox


# Create main window
main = tk.Tk()
main.title("Exercise2-Chapter5")
main.geometry("200x100")

# Define a class to store the marks of the student and calculate for the average
class Student:
    def __init__(data, name, mark1, mark2, mark3):
        data.name = name
        data.mark1 = mark1
        data.mark2 = mark2
        data.mark3 = mark3

    def calcGrade(data):
        return (data.mark1 + data.mark2 + data.mark3) / 3

    def display(data):
        grade = data.calcGrade()
        messagebox.showinfo("Student Info", f"Name: {data.name}\nGrade: {grade}")

# Create a function to create a variable with data and variable to input data
def createstudent():
    student1 = Student("Krunch", 99, 94, 97)
    student2 = Student("", 0, 0, 0)

    name = input("Enter student name: ")
    mark1 = int(input("Enter student mark 1: "))
    mark2 = int(input("Enter student mark 2: "))
    mark3 = int(input("Enter student mark 3: "))

    student2.name = name
    student2.mark1 = mark1
    student2.mark2 = mark2
    student2.mark3 = mark3
    student1.display()
    student2.display()
    
# Create a frame for the button
frame = tk.Frame(main)
frame.pack()

# Create a button to create student
button = tk.Button(frame, text="Create Student", command=createstudent)
button.pack(pady=20)

# Run the gui
main.mainloop()