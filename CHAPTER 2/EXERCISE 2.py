from tkinter import *
import random

#gui main window
main = Tk()
#title of gui
main.title('Exercise2-Chapter2')

#labels with text, width and background color
bA = Label( main, text="A", width="12", bg="red", relief=GROOVE, bd=5)
bB = Label( main, text="B", width="12", bg="yellow")
bC = Label( main, text="C", width="12", bg="blue")
bD = Label( main, text="D", width="12", bg="white")

#location of each label in the gui
bA.pack(side='top', fill=X, expand=1)
bB.pack(side='bottom')
bC.pack(side='left', fill=Y, expand=1)
bD.pack(side='right')

#run gui
main.mainloop()