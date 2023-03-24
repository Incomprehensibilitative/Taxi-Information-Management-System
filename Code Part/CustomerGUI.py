import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import Validation

window = tk.Tk()
window.title("Data Entry Form")


def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


def enter_data():
    name = name_entry.get()
    phone_num = phone_num_entry.get()
    vehicle_type = vehicle_type_combobox.get()
    if not Validation.is_valid_name(name) or name == "Enter name":
        tkinter.messagebox.showwarning(title="Error", message="Invalid name")
    if not Validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
        tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
    if not Validation.is_valid_vehicle_type(vehicle_type):
        tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle Type")
    else:
        tkinter.messagebox.showinfo(title="Success", message="Yay")
        # Enter to excel
        window.quit()


frame = tk.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tk.LabelFrame(frame, text="Customer")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# name
name_label = tk.Label(user_info_frame, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(user_info_frame)
name_entry.insert(0, "Enter name")
name_entry.configure(state='disabled')
name_entry.grid(row=1, column=0)

# phone number
phone_num_label = tk.Label(user_info_frame, text="Phone Number")
phone_num_label.grid(row=0, column=1)
phone_num_entry = tk.Entry(user_info_frame)
phone_num_entry.insert(0, "0### ### ###")
phone_num_entry.configure(state='disabled')
phone_num_entry.grid(row=1, column=1)

# pick up spot
pick_up_label = tk.Label(user_info_frame, text="Pick up spot")
pick_up_label.grid(row=0, column=2)
pick_up_entry = tk.Entry(user_info_frame)
pick_up_entry.grid(row=1, column=2)

# # age
# age_label = tk.Label(user_info_frame, text="Age")
# age_label.grid(row=2, column=0)
# age_spinbox = tk.Spinbox(user_info_frame, from_=0, to=110)
# age_spinbox.grid(row=3, column=0)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Vehicle info
vehicle_frame = tk.LabelFrame(frame)
vehicle_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

vehicle_type_label = tk.Label(vehicle_frame, text="Type")
vehicle_type_label.grid(row=0, column=0)
vehicle_type_combobox = ttk.Combobox(vehicle_frame, values=["5S", "7S", "9S"])
vehicle_type_combobox.grid(row=1, column=0)

price_label = tk.Label(vehicle_frame, text="Pricing")
price_label.grid(row=0, column=1)
price_for_5S = tk.Label(vehicle_frame, text="5S - 10,000")
price_for_5S.grid(row=1, column=1)
price_for_7S = tk.Label(vehicle_frame, text="7S - 13,000")
price_for_7S.grid(row=2, column=1)
price_for_9S = tk.Label(vehicle_frame, text="9S - 15,000")
price_for_9S.grid(row=3, column=1)

# Button
button = tk.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# disable placeholder
name_focus_in = name_entry.bind('<Button-1>', lambda x: on_focus_in(name_entry))
name_focus_out = name_entry.bind(
    '<FocusOut>', lambda x: on_focus_out(name_entry, 'Enter name'))

phone_num_focus_in = phone_num_entry.bind('<Button-1>', lambda x: on_focus_in(phone_num_entry))
phone_num_focus_out = phone_num_entry.bind(
    '<FocusOut>', lambda x: on_focus_out(phone_num_entry, '0### ### ###'))

window.mainloop()