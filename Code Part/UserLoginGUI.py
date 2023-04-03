import tkinter as tk
from tkinter import messagebox

import AdminGUI


def user_login(system):
    # creating frame
    window = tk.Tk()
    window.title("User Login")
    window.geometry("400x400")

    frame = tk.Frame()

    # validate username and password command
    def login(system):
        username = "root"
        password = "1"
        if username_entry.get() == username and password_entry.get() == password:
            messagebox.showinfo(title="Login Status", message="You have successfully logged in!")
            window.destroy()
            AdminGUI.main(system)
        else:
            messagebox.showwarning(title="Login Status", message="Incorrect Username or Password! Please Try again!")

    # creating widgets
    login_label = tk.Label(frame, text="Login", font=("defaults", 50))
    username_label = tk.Label(frame, text="Username", font=("defaults", 16))
    username_entry = tk.Entry(frame, font=("defaults", 16))
    password_entry = tk.Entry(frame, show="*", font=("defaults", 16))
    password_label = tk.Label(frame, text="Password", font=("defaults", 16))
    login_button = tk.Button(frame, text="Login", font=("defaults", 20), bg="pink", command=lambda: login(system))

    # display widgets on screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=50)
    username_label.grid(row=1, column=0, padx=10)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0, padx=10)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, )

    frame.pack()
    window.mainloop()
