import tkinter as tk
from tkinter import messagebox

# Create main window
main = tk.Tk()
main.title("Exercise4-Chapter5")
main.geometry("200x150")

# Define the main class Shape
class Shape:
    def __init__(data):
        data.sides = []

    def inputSides(data):
        # Input sides based on the number of sides the shape has
        for i in range(data.numsides):
            data.sides.append(float(input(f"\nEnter side {i+1}: ")))

# Create circle class which acquires shape class
class Circle(Shape):
    def __init__(data):
        super().__init__()
        data.numsides = 1
        data.radius = None

    def inputSides(data):
        # Input the radius for the circle
        data.radius = float(input("\nEnter radius: "))

    def area(data):
        # Calculate and return the area of the circle
        return 3.14159 * data.radius * data.radius

# Create rectangle class which acquires shape class
class Rectangle(Shape):
    def __init__(data):
        super().__init__()
        data.numsides = 2

    def area(data):
        # Calculate and return the area of the rectangle
        return data.sides[0] * data.sides[1]

# Create triangle class which acquires shape class
class Triangle(Shape):
    def __init__(data):
        super().__init__()
        data.numsides = 3

    def area(data):
        # Calculate and return the area of the triangle 
        return  (data.sides[0] + data.sides[1] + data.sides[2]) / 2
        

# Create a function to calculate and display the area of a circle 
def calculatecirclearea():
    shape = Circle()
    shape.inputSides()
    area = shape.area()
    messagebox.showinfo("Result", f"The area of the circle is {area}")

# Function to calculate and display the area of a rectangle 
def calculaterectanglearea():
    shape = Rectangle()
    shape.inputSides()
    area = shape.area()
    messagebox.showinfo("Result", f"The area of the rectangle is {area}")

# Function to calculate and display the area of a triangle 
def calculatetrianglearea():
    shape = Triangle()
    shape.inputSides()
    area = shape.area()
    messagebox.showinfo("Result", f"The area of the triangle is {area}")

# Create a label for choosing a shape
label = tk.Label(main, text="Choose a shape:")
label.pack()

# Create buttons for each shape
circle_button = tk.Button(main, text="Circle", command=calculatecirclearea)
circle_button.pack()

rectangle_button = tk.Button(main, text="Rectangle", command=calculaterectanglearea)
rectangle_button.pack()

triangle_button = tk.Button(main, text="Triangle", command=calculatetrianglearea)
triangle_button.pack()

# Run the gui
main.mainloop()
