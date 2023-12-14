import tkinter as tk
from tkinter import messagebox

# Create main window
main = tk.Tk()
main.title("Exercise1-Chapter4")

# Create a function to write the data to the file
def writedata():
    name = nameentry.get()
    age = ageentry.get()
    hometown = hometownentry.get()

    try:
        with open("bio.txt", "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Hometown: {hometown}\n")
        messagebox.showinfo("Success", "Data has been written to the file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create a function to read the data from the file that has been written
def readdata():
    try:
        with open("bio.txt", "r") as file:
            data = file.read()
        messagebox.showinfo("Data from the file", data)
    except FileNotFoundError:
        messagebox.showinfo("Error", "File does not exist.")


# Create frame 
frame = tk.Frame(main)
frame.pack(padx=20, pady=20)

# Create label and entry widgets for name, age, and hometown
namelabel = tk.Label(frame, text="Name:")
namelabel.grid(row=0, column=0)
nameentry = tk.Entry(frame)
nameentry.grid(row=0, column=1)

agelabel = tk.Label(frame, text="Age:")
agelabel.grid(row=1, column=0)
ageentry = tk.Entry(frame)
ageentry.grid(row=1, column=1)

hometownlabel = tk.Label(frame, text="Hometown:")
hometownlabel.grid(row=2, column=0)
hometownentry = tk.Entry(frame)
hometownentry.grid(row=2, column=1)

# Create a write and read button
writebutton = tk.Button(frame, text="Write to file", command=writedata)
writebutton.grid(row=3, column=0, columnspan=2)

readbutton = tk.Button(frame, text="Read from file", command=readdata)
readbutton.grid(row=4, column=0, columnspan=2)

# Run the gui
main.mainloop()
