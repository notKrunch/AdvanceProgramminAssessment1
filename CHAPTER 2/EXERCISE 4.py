import tkinter as tk
from tkinter import ttk, PhotoImage

# Create main window
main = tk.Tk()
main.title("Student Management System")
main.geometry("550x900")

# Create a style for the frame
style = ttk.Style()
style.configure("TFrame", background="#f4f4f6")

# Create an image on top of the window
imagelogo = PhotoImage(file="C:/Users/mrlum/Desktop/L5 ADVANCED PROGRAMMING 1ST SEM/ASSESSMENT 1/CHAPTER 2/logo.png")
imagelogolabel = ttk.Label(main, image=imagelogo)
imagelogolabel.pack(pady=(20, 0))

# Create header text
headerlabel1 = ttk.Label(main, text="Student Management System", font=("Helvetica", 20, "bold"))
headerlabel1.pack(pady=(20, 10))

headerlabel2 = ttk.Label(main, text="New Student Registration", font=("Helvetica", 16, "bold"))
headerlabel2.pack(pady=(0, 20))
# Create a Frame
frame = ttk.Frame(main, padding="50", style="TFrame")
frame.pack()

# Create Entry widgets for the student form
nameentry = ttk.Entry(frame)
nameentry.grid(row=0, column=1, padx=10, pady=10)

mobileentry = ttk.Entry(frame)
mobileentry.grid(row=1, column=1, padx=10, pady=10)

emailentry = ttk.Entry(frame)
emailentry.grid(row=2, column=1, padx=10, pady=10)

homeaddressentry = ttk.Entry(frame)
homeaddressentry.grid(row=3, column=1, padx=10, pady=10)

gendervar = tk.StringVar()
gendercombobox = ttk.Combobox(frame, textvariable=gendervar)
gendercombobox.grid(row=4, column=1, padx=10, pady=10)
gendercombobox['values'] = ('Male', 'Female', 'Other')

coursevar = tk.StringVar()
coursecombobox = ttk.Combobox(frame, textvariable=coursevar)
coursecombobox.grid(row=5, column=1, padx=10, pady=10)
coursecombobox['values'] = ('BSc CC', 'BSc CY', 'BSc PSY', 'BA & BM')

languagevar = tk.StringVar()
languagecombobox = ttk.Combobox(frame, textvariable=languagevar)
languagecombobox.grid(row=6, column=1, padx=10, pady=10)
languagecombobox['values'] = ('English', 'Tagalog', 'Hindi / Urdu')

# Create Label widgets for the student form
namelabel = ttk.Label(frame, text="Student Name")
namelabel.grid(row=0, column=0, padx=10, pady=10)

mobilelabel = ttk.Label(frame, text="Mobile Number")
mobilelabel.grid(row=1, column=0, padx=10, pady=10)

emaillabel = ttk.Label(frame, text="Email Id")
emaillabel.grid(row=2, column=0, padx=10, pady=10)

homeaddresslabel = ttk.Label(frame, text="Home Address")
homeaddresslabel.grid(row=3, column=0, padx=10, pady=10)

genderlabel = ttk.Label(frame, text="Gender")
genderlabel.grid(row=4, column=0, padx=10, pady=10)

courselabel = ttk.Label(frame, text="Course Enrolled")
courselabel.grid(row=5, column=0, padx=10, pady=10)

languagelabel = ttk.Label(frame, text="Language Known")
languagelabel.grid(row=6, column=0, padx=10, pady=10)

# Create a label for rating the english communication skills
englishratinglabel = ttk.Label(frame, text="Rate your English communication skills")
englishratinglabel.grid(row=7, column=0, padx=10, pady=10)

# Scroll rate for the english communication skills
englishrating = ttk.Scale(frame, from_=0, to=10, orient=tk.HORIZONTAL, length=100)
englishrating.grid(row=7, column=1, padx=10, pady=10)


# Create a Button for Submit and Clear
style = ttk.Style()
style.configure("TButton", background="#22263d")

addbutton = ttk.Button(frame, text="Submit", style="TButton")
addbutton.grid(row=8, column=0, padx=20, pady=50)
clearbutton = ttk.Button(frame, text="Clear", style="TButton")
clearbutton.grid(row=8, column=1, padx=20, pady=50)

# Run the gui 
main.mainloop()