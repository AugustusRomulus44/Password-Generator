from tkinter import *
from tkinter.ttk import *
import random
import pyperclip

# Version 1.1.

root = Tk()


root.title("Password Generator")
root.geometry("400x45")


# All the elements for the password(numbers, uppercase and lowercase letters)
elements = "ABCDEFGHIOUPRSTQXZabcdefghiouprstqxz1234567890"

# creates a password with a length of 12 digits by randomly choosing out of the elements above

def pick_password():
    entry.delete(0, END)

    user_password = ""
    length = 12

    for i in range(0, length):
        user_password = user_password + random.choice(elements)
    return user_password

# calls the function above and inserts it into the entry grid

def generate():
    password1 = pick_password()
    entry.insert(10, password1)

# Copy to clipboard

def copy():
    generated_password = entry.get()
    pyperclip.copy(generated_password)


# Generates a new password and stores it in a text file.

def copy_to_data():
    stored_password = generate()

    filename = "passwords.txt"
    with open(filename, "a") as f:
        f.write(stored_password + "\n")
        f.close()


entry = Entry(root)
entry.grid(row=0, column=1)


# All the buttons for the functions.

generate_button = Button(root, text="Generate", width=15, command=generate)
generate_button.grid(row=0, column=3)

copy_button = Button(root, text="Copy to Clipboard", width=20, command=copy)
copy_button.grid(row=0, column=4)

copy_to_database_button = Button(root, text="Copy to Database", width=20, command=copy_to_data)
copy_to_database_button.grid(row=0, column=5)

root.mainloop()

