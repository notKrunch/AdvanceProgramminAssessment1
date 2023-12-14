from tkinter import *

#gui main window
main = Tk()
#title of gui
main.title('Exercise1-Chapter2')
#size of gui
main.geometry('300x300')
#gui is no longer resizable
main.resizable(0, 0)
#gui background color
main.configure(bg='lightblue')
#label greeting the user with bold font
l = Label(main, text="Hello user, How are you?", font=('Times New Roman', 15, 'bold'))

#location of label in the gui
l.pack(side='top')

#run gui
main.mainloop()