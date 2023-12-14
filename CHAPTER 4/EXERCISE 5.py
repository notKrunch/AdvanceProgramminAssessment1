import tkinter as tk
from tkinter import messagebox


# Create the main window
main = tk.Tk()
main.title("Exercise5-Chapter5")
main.geometry("200x100")

# Create a function for the conditions required to validate the password
def enterpassword():
    attempts = 0
    while attempts < 5:
        password = passwordentry.get()

        # The length of the password should not be less than 6 character and more than 12 characters
        # If the password does not meet the required condition, the password attempt will decrease by 1 attempt.
        if (len(password) < 6 or len(password) > 12 or
            not any(pw.islower() for pw in password) or
            not any(pw.isupper() for pw in password) or
            not any(pw.isdigit() for pw in password) or
            not any(pw in '$,#,@' for pw in password)):

            attempts += 1
            messagebox.showerror("Invalid Password",
                                 "The password is not valid. "
                                 f"You have {5-attempts} attempts remaining.")

        else:
            messagebox.showinfo("Valid Password", "The password is valid.")
            break
    # If the attempt reaches 5 the loop will break
    if attempts == 5:
        messagebox.showerror("Max Attempts Reached",
                             "You have exceeded the maximum number of "
                             "password attempts. The authorities have been alerted.")



#  Create a label and entry for password
passwordlabel = tk.Label(main, text="Enter a valid password:")
passwordlabel.pack()
passwordentry = tk.Entry(main)
passwordentry.pack()

# Create a button to validate the password
validatebutton = tk.Button(main, text="Submit", command=enterpassword)
validatebutton.pack()

# Run the gui
main.mainloop()