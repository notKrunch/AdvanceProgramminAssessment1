import tkinter as tk
from math import pi

# Create main window
main = tk.Tk()
main.title("Exercise3-Chapter3")

# Create function to calculate for circle, square, and rectangle
def calculatecircle():
    radius = float(circleradius.get())
    area = pi * radius**2
    circlearea.config(text=f"Area: {area:.2f}")

def calculatesquare():
    side = float(squareside.get())
    area = side * side
    squarearea.config(text=f"Area: {area:.2f}")

def calculaterectangle():
    length = float(rectanglelength.get())
    width = float(rectanglewidth.get())
    area = length * width
    rectanglearea.config(text=f"Area: {area:.2f}")

# Frame for circle, square, and rectangle calculator
circleframe = tk.Frame(main, bg='lightblue')
circleframe.pack(padx=10, pady=5, fill='x')
tk.Label(circleframe, text="Circle Radius:", bg='lightblue').pack(side='left')
circleradius = tk.Entry(circleframe)
circleradius.pack(side='left')
tk.Button(circleframe, text="Calculate Area", command=calculatecircle).pack(side='left')
circlearea = tk.Label(circleframe, text="Area: ", bg='lightblue')
circlearea.pack(side='left')

squareframe = tk.Frame(main, bg='red')
squareframe.pack(padx=10, pady=5, fill='x')
tk.Label(squareframe, text="Square Side:", bg='red').pack(side='left')
squareside = tk.Entry(squareframe)
squareside.pack(side='left')
tk.Button(squareframe, text="Calculate Area", command=calculatesquare).pack(side='left')
squarearea = tk.Label(squareframe, text="Area: ", bg='red')
squarearea.pack(side='left')

rectangleframe = tk.Frame(main, bg='lightgreen')
rectangleframe.pack(padx=10, pady=5, fill='x')
tk.Label(rectangleframe, text="Rectangle Length:", bg='lightgreen').pack(side='left')
rectanglelength = tk.Entry(rectangleframe)
rectanglelength.pack(side='left')
tk.Label(rectangleframe, text="Width:", bg='lightgreen').pack(side='left')
rectanglewidth = tk.Entry(rectangleframe)
rectanglewidth.pack(side='left')
tk.Button(rectangleframe, text="Calculate Area", command=calculaterectangle).pack(side='left')
rectanglearea = tk.Label(rectangleframe, text="Area: ", bg='lightgreen')
rectanglearea.pack(side='left')

# Run the gui
main.mainloop()