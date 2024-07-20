from tkinter import *
from tkinter.ttk import *
import random
import pyperclip


root = Tk()


root.title("Password Generator")
root.geometry("400x45")


elements = "ABCDEFGHIOUPRSTQXZabcdefghiouprstqxz1234567890"


def pick_password():
    entry.delete(0, END)

    user_password = ""
    length = 12

    for i in range(0, length):
        user_password = user_password + random.choice(elements)
    return user_password


def generate():
    password1 = pick_password()
    entry.insert(10, password1)


def copy():
    generated_password = entry.get()
    pyperclip.copy(generated_password)


entry = Entry(root)
entry.grid(row=0, column=1)


generate_button = Button(root, text="Generate", width=15, command=generate)
generate_button.grid(row=0, column=3)

copy_button = Button(root, text="Copy to Clipboard", width=20, command=copy)
copy_button.grid(row=0, column=4)


root.mainloop()

