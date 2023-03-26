import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import Validation
import openpyxl


""" Common functions """
def tuple_to_list(t):
    new_list = []
    for element in t:
        new_list.append(element)
    return new_list
# Placeholder Function
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


# load data from database to print onto GUI
data = openpyxl.load_workbook("Taxi-information.xlsx", data_only=True)
def load_data(window):
    sheet = data['Customer']

    treeFrame = ttk.Frame(window)
    treeFrame.pack()
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    cols = ("id", "name", "phone_num")
    # cols = ("id", "name", "phone_num", "vehicle_id", "salary", "gender", "age")
    treeview = ttk.Treeview(treeFrame, show="headings",
                            yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("name", width=50)
    treeview.column("phone_num", width=100)
    # treeview.column("vehicle_id", width=100)
    # treeview.column("salary", width=100)
    # treeview.column("gender", width=100)
    # treeview.column("age", width=50)
    treeview.pack()
    treeScroll.config(command=treeview.yview)

    list_values = list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, value=value_tuple)







""" New administration windows """


# Driver window
def driver():
    def list_drivers():
        sheet = data['Driver']
        # function that take object list in Management class to print
        driver_list_window = tk.Tk()
        driver_list_window.title("Driver List")
        load_data(driver_list_window)


    # for element in customer_list:
    #     print("{:8} {:<15} {:<15}".format(element.get_id(), element.get_name(), element.get_phone_num()))

    def new_driver():
        def enter_driver_data():
            name = name_entry.get()
            phone_num = phone_num_entry.get()
            vehicle_id = vehicle_id_entry.get()
            salary = salary_entry.get()
            gender = gender_combobox.get()
            age = age_spinbox.get()
            if not Validation.is_valid_name(name) or name == "Enter name":
                tkinter.messagebox.showwarning(title="Error", message="Invalid name")
            if not Validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
                tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
            if not Validation.is_valid_vehicle_id(vehicle_id) or vehicle_id == "V#":
                # need to check whether the vehicle actually exist or available for assignment
                tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle ID")
            if not Validation.is_valid_gender(gender):
                tkinter.messagebox.showwarning(title="Error", message="Invalid Gender")
            # time to add new driver to the database

        new_driver_window = tk.Tk()
        new_driver_window.title("New Driver")
        new_driver_frame = tk.Frame(new_driver_window)
        new_driver_frame.grid(row=0, column=0, padx=20, pady=10)

        # name
        name_label = tk.Label(new_driver_frame, text="Name")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(new_driver_frame)
        name_entry.insert(0, "Enter name")
        name_entry.configure(state='disabled')
        name_entry.grid(row=1, column=0)
        # phone number
        phone_num_label = tk.Label(new_driver_frame, text="Phone Number")
        phone_num_label.grid(row=0, column=1)
        phone_num_entry = tk.Entry(new_driver_frame)
        phone_num_entry.insert(0, "0### ### ###")
        phone_num_entry.configure(state='disabled')
        phone_num_entry.grid(row=1, column=1)
        # vehicle_id
        vehicle_id_label = tk.Label(new_driver_frame, text="Vehicle ID")
        vehicle_id_label.grid(row=0, column=2)
        vehicle_id_entry = tk.Entry(new_driver_frame)
        vehicle_id_entry.insert(0, "V#")
        vehicle_id_entry.configure(state='disabled')
        vehicle_id_entry.grid(row=1, column=2)
        # salary
        salary_label = tk.Label(new_driver_frame, text="Salary")
        salary_label.grid(row=2, column=0)
        salary_entry = tk.Entry(new_driver_frame)
        salary_entry.grid(row=3, column=0)
        # gender
        gender_label = tk.Label(new_driver_frame, text="Gender")
        gender_label.grid(row=2, column=1)
        gender_combobox = ttk.Combobox(new_driver_frame, values=["Male", "Female", "Other"])
        gender_combobox.grid(row=3, column=1)
        # age
        age_label = tk.Label(new_driver_frame, text="Age")
        age_label.grid(row=2, column=2)
        age_spinbox = tk.Spinbox(new_driver_frame, from_=0, to=200)
        age_spinbox.grid(row=3, column=2)
        # Confirm button
        button = tk.Button(new_driver_frame, text="Enter data", command=enter_driver_data)
        button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

        # Disable placeholder
        name_entry.bind('<Button-1>', lambda x: on_focus_in(name_entry))
        name_entry.bind('<FocusOut>', lambda x: on_focus_out(name_entry, 'Enter name'))

        phone_num_entry.bind('<Button-1>', lambda x: on_focus_in(phone_num_entry))
        phone_num_entry.bind('<FocusOut>', lambda x: on_focus_out(phone_num_entry, '0### ### ###'))

        vehicle_id_entry.bind('<Button-1>', lambda x: on_focus_in(vehicle_id_entry))
        vehicle_id_entry.bind('<FocusOut>', lambda x: on_focus_out(vehicle_id_entry, 'V#'))

    # main frame for Driver Admin
    driver_window = tk.Tk()
    driver_window.title("Driver Admin")
    driver_frame = tk.Frame(driver_window)
    driver_frame.grid(row=0, column=0, padx=20, pady=10)

    new_driver_button = tk.Button(driver_frame, text="New Driver", command=new_driver)
    new_driver_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

    driver_list_button = tk.Button(driver_frame, text="Driver List", command=list_drivers)
    driver_list_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    driver_window.mainloop()


# The main window
window = tk.Tk()
window.title("Administration")

frame = tk.Frame(window)
frame.pack()

driver_button = tk.Button(frame, text="Driver Administration", command=driver)
driver_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
