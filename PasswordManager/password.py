from tkinter import *
import random

# ---------------------------- PASSWORD FUNCTION ------------------------------- #

def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "e", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!","§","$","%","&","/","="]
    capital_letters = [i.capitalize() for i in letters]
    random_password = ""

    for i in range(7):
        letter = random.choice(letters)
        random_password += letter
        symbol = random.choice(symbols)
        random_password += symbol
        cap_letter = random.choice(capital_letters)
        random_password += cap_letter

    "".join(random.sample(random_password, len(random_password)))

    passwords_entry.insert(0, str(random_password))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    username = user_name_entry.get()
    password = passwords_entry.get()
    page = website_entry.get()

    with open("data.txt", "a") as savefile:
        savefile.write(f"{username} | {password} | {page} \n")

    user_name_entry.delete(0, END)
    passwords_entry.delete(0, END)
    website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=3)

website = Label(text="Webseite:")
website.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", pady=2)

user_name = Label(text="Benutzername:")
user_name.grid(column=0, row=2)

user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

passwords = Label(text="Passwort:")
passwords.grid(column=0, row=3)

# Password-Stars can be disabled by removing the 'show' attribute maybe per Button in the future
passwords_entry = Entry(width=21, show="*",)
passwords_entry.grid(column=1, row=3, sticky="ew")

password_button = Button(text="Passwort generieren",  command=generate_password)
password_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Hinzufügen", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")


window.mainloop()
