from tkinter import *
from tkinter.ttk import *
import random
import pyperclip

# Version 1.2.

root = Tk()


root.title("Password Generator")
root.geometry("550x70")

image_icon = (PhotoImage(file="Lock icon.png"))
root.iconphoto(False, image_icon)

elements = "ABCDEFGHIOUPRSTQXZabcdefghiouprstqxz1234567890%%&?!*+-_.,"


def pick_password():
    entry1.delete(0, END)

    user_password = ""
    length = 12

    for i in range(0, length):
        user_password = user_password + random.choice(elements)
    return user_password


def generate():
    password1 = pick_password()
    entry1.insert(10, password1)
    return password1


def copy():
    generated_password = entry1.get()
    pyperclip.copy(generated_password)


def copy_to_data():
    stored_password = generate()

    filename = "passwords.txt"
    with open(filename, "a") as location:
        location.write(entry2.get() + ":" + " ")
    with open(filename, "a") as f:
        f.write(stored_password + "\n")
        f.close()


entry1 = Entry(root)
entry1.grid(row=0, column=1)

entry2 = Entry(root)
entry2.grid(row=3, column=1, ipadx=30)

label1 = Label(root, text="What is this password for?")
label1.grid(row=4, column=1)

generate_button = Button(root, text="Generate", width=15, command=generate)
generate_button.grid(row=0, column=3)

copy_button = Button(root, text="Copy to Clipboard", width=20, command=copy)
copy_button.grid(row=0, column=4)

copy_to_database_button = Button(root, text="Copy to Database", width=20, command=copy_to_data)
copy_to_database_button.grid(row=0, column=5)

root.mainloop()

