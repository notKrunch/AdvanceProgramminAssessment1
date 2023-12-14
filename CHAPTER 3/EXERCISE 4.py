import tkinter as tk
from tkinter import ttk

# Create main window
main = tk.Tk()
main.title("Exercise4-Chapter3")
main.resizable(0, 0)

# Create a function for drawing shapes
class DrawShapes:
    def __init__(data, input):
        data.input = input
        data.canvas = tk.Canvas(data.input, width=400, height=400, bg="white")
        data.canvas.pack(pady=10)

        # Shape Options
        data.shapevar = tk.StringVar()
        shapes = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        data.shapevar.set(shapes[0])
        
        # Create a label "Select Shape: "
        shapelabel = ttk.Label(data.input, text="Select Shape:")
        shapelabel.pack(pady=5)

        # Create a dropdown menu
        shapedropdown = ttk.Combobox(data.input, textvariable=data.shapevar, values=shapes[1:], state="readonly")
        shapedropdown.pack(pady=5)

        # Create a button to draw the shape
        button = ttk.Button(data.input, text="Draw Shape", command=data.drawshape)
        button.pack(pady=10)

    # Create a function for drawing the coordinates of selected shape
    def drawshape(data):
        selectedshape = data.shapevar.get()
        data.canvas.delete("all")

        if selectedshape == "Oval":
            data.canvas.create_oval(50, 50, 350, 200, outline="black", width=2  )
        elif selectedshape == "Rectangle":
            data.canvas.create_rectangle(50, 50, 350, 200, outline="black", width=2)
        elif selectedshape == "Square":
            data.canvas.create_rectangle(50, 50, 200, 200, outline="black", width=2)
        elif selectedshape == "Triangle":
            data.canvas.create_polygon(50, 200, 200, 50, 350, 200, outline="black", width=2)


#Run the gui
DrawShapes(main)
main.mainloop()
