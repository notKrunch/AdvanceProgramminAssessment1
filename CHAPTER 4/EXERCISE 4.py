import tkinter as tk
from tkinter import filedialog


# Create the main window
main = tk.Tk()
main.title("Exercise4-Chapter4")
main.geometry("200x100")

# Create a function to read the file 
def readfile():
    # Create a function to open the specific file to be read
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    filecontent = file.read()

    # Entry to get the letter to search for
    letter = letterentry.get()

    # Count the occurrences of the letter that has been typed
    count = filecontent.count(letter)

    # Create a function to display the count of letter occurences
    countlabel.config(text=f"The letter '{letter}' occurs {count} times.")

# Create a label saying "Enter a character: "
filelabel = tk.Label(main, text="Enter a character:")
filelabel.pack()

# Create an entry for typing a letter
letterentry = tk.Entry(main)
letterentry.pack()

# Create a button to read the file you want to open
readbutton = tk.Button(main, text="Read File", command=readfile)
readbutton.pack()

# Create a label of the count of letter occurences
countlabel = tk.Label(main, text="")
countlabel.pack()

# Run the gui
main.mainloop()