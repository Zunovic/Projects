from tkinter import *


window = Tk()
window.title("Passwort Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
bg_picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_picture)
canvas.grid(column=1, row=0)

website_label = Label(text="Webseite:")
website_label.grid(column=0, row=1)
username_label = Label(text="Benutzername:")
username_label.grid(column=0, row=2)
password_label = Label(text="Passwort:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2,columnspan=2, sticky="w")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, sticky="w")

gen_pw_button = Button(text="Generiere Passwort")
gen_pw_button.grid(column=2, row=3, sticky="ew", padx=(2, 0))
save_pw_button = Button(text="Speichern")
save_pw_button.grid(column=1, row=4, columnspan=2, pady=2, sticky="ew")

window.mainloop()
