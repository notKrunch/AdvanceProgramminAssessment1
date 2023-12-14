import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Create main window
main = tk.Tk()
main.title("Exercise1-Chapter5")
main.geometry("200x100")

# Define a class to store basic information and actions for the dog
class Dog:
    def __init__(data, name, birthdate, breed):
        data.name = name
        data.birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        data.breed = breed

    # Create a function to display the name, birthdate, and breed
    def getinfo(data):
        return f"Name: {data.name}\nBirthdate: {data.birthdate.strftime('%Y-%m-%d')}\nBreed: {data.breed}\n"

    # Create a function to calculate the dogs woof based on its age
    def woof(data):
      age = datetime.now().year - data.birthdate.year
      return f"{data.name} says Woof!" if age >= 0 else f"{data.name} is not old enough to woof yet."

# Create a function of the dogs data and to check the oldest dog
def createdogs():
    dogs = [
        Dog("Jack", "2009-10-08", "Golden Retriever"),
        Dog("Buddy", "2023-10-22", "Labrador Retriever")
    ]

    oldestdog = min(dogs, key=lambda bday: bday.birthdate)

    for dog in dogs:
        print(dog.getinfo())

    print(f"The oldest dog is {oldestdog.name} who woofs {oldestdog.woof()}")

# Create a frame for the button
frame = tk.Frame(main)
frame.pack()

# Create a button to Create Dogs
button = tk.Button(frame, text="Create Dogs", command=createdogs)
button.pack(pady=20)

# Run the gui
main.mainloop()
