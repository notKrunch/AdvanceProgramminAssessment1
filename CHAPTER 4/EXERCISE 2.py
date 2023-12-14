import tkinter as tk
from tkinter import filedialog, messagebox


# Create main window
main = tk.Tk()
main.title("Exercise2-Chapter4")

# Create a function to count all the occurences of the strings in a specific file
def countoccurrences():
    stringcounter = [
        "Hello my name is Peter Parker",
        "I love Python Programming",
        "Love",
        "Enemy"
    ]

    filepath = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])

    if not filepath:
        return

    try:
        with open(filepath, 'r') as file:
            content = file.read()

        occurrences = {string: content.count(string) for string in stringcounter}
        resulttext.config(state=tk.NORMAL)
        resulttext.delete('1.0', tk.END)

        for string, count in occurrences.items():
            resulttext.insert(tk.END, f'{string}: {count} occurrences\n')

        resulttext.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create a frame for the result of file opened
resultframe = tk.Frame(main)
resultframe.pack(padx=10, pady=10)
resulttext = tk.Text(resultframe, height=4, width=100, state=tk.DISABLED)
resulttext.pack()

# Create a button to count all occurences of the strings
tk.Button(main, text="Count Occurrences", command=countoccurrences).pack(pady=10)

# Run the gui
main.mainloop()
