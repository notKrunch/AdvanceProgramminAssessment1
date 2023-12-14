from tkinter import *

#gui main window
main = Tk()
#title of gui
main.title('Exercise2b-Chapter2')
#size of gui
main.geometry("300x200")
#gui left frame
left_frame = Frame(main, borderwidth=5, relief=RIDGE)
left_frame.pack(side=LEFT, expand=True, fill=BOTH)

#gui right frame
right_frame = Frame(main, borderwidth=5, relief=RIDGE)
right_frame.pack(side=RIGHT, expand=True, fill=BOTH)

# labels with text, border and background color
label_A = Label(left_frame, text="A", border=38, bg="#22263d", fg="white")
label_B = Label(left_frame, text="B", border=38)
label_C = Label(right_frame, text="C", border=38)
label_D = Label(right_frame, text="D", border=38, bg="#22263d", fg="white")


#locate labels inside their designated frames
label_A.pack(side=TOP, expand=True, fill=X)
label_B.pack(side=BOTTOM, expand=True, fill=X)
label_C.pack(side=TOP, expand=True, fill=X)
label_D.pack(side=BOTTOM, expand=True, fill=X)

#run gui
main.mainloop()