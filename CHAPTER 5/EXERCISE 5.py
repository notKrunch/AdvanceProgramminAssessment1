import tkinter as tk
from tkinter import messagebox

# Create  main main
main = tk.Tk()
main.title("Exercise5-Chapter5")
main.geometry("200x400")

# Define Animal class
class Animal:
    def __init__(data, Type, Name, Color, Age, Weight, Noise):
        data.Type = Type
        data.Name = Name
        data.Color = Color
        data.Age = Age
        data.Weight = Weight
        data.Noise = Noise

    def sayHello(data):
        print(f"Hello, my name is {data.Name}")

    def makeNoise(data):
        print(f"{data.Name} says {data.Noise}")

    def animalDetails(data):
        print(f"Animal Details:\nType: {data.Type}\nName: {data.Name}\nColor: {data.Color}\nAge: {data.Age}\nWeight: {data.Weight}\nNoise: {data.Noise}")

# Create a function to create the details of the animal
def createanimal():
    Type = entryType.get()
    Name = entryName.get()
    Color = entryColor.get()
    Age = entryAge.get()
    Weight = entryWeight.get()
    Noise = entryNoise.get()

    # Instantiate a new Animal object
    newanimal = Animal(Type, Name, Color, Age, Weight, Noise)

    # Create buttons for the newly created animal
    buttonsayHello = tk.Button(main, text="Say Hello", command=newanimal.sayHello)
    buttonsayHello.pack()

    buttonmakeNoise = tk.Button(main, text="Make Noise", command=newanimal.makeNoise)
    buttonmakeNoise.pack()

    buttonanimalDetails = tk.Button(main, text="Animal Details", command=newanimal.animalDetails)
    buttonanimalDetails.pack()

# Create label and entry for animal type, name, Color, age, weight, and noise
labelType = tk.Label(main, text="Animal Type:")
labelType.pack()
entryType = tk.Entry(main)
entryType.pack()

labelName = tk.Label(main, text="Name:")
labelName.pack()
entryName = tk.Entry(main)
entryName.pack()

labelColor = tk.Label(main, text="Color:")
labelColor.pack()
entryColor = tk.Entry(main)
entryColor.pack()

labelAge = tk.Label(main, text="Age:")
labelAge.pack()
entryAge = tk.Entry(main)
entryAge.pack()

labelWeight = tk.Label(main, text="Weight:")
labelWeight.pack()
entryWeight = tk.Entry(main)
entryWeight.pack()

labelNoise = tk.Label(main, text="Noise:")
labelNoise.pack()
entryNoise = tk.Entry(main)
entryNoise.pack()

# Create a button to create animal with the inputs
buttoncreate = tk.Button(main, text="Create Animal", command=createanimal)
buttoncreate.pack()

# Run the gui
main.mainloop()
