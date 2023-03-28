import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import Validation
import openpyxl
import database_reader as dr
import random
""" Common functions """
# check existence
def exist_vehicle_id(id):
    driver_list = dr.take_driver_info()
    driver_vehicle_id_list = []
    # Check in driver whether the vehicle already belongs to other driver
    for driver in driver_list:
        driver_vehicle_id_list.append(driver.get_vehicle_id())
    if id in driver_vehicle_id_list:
        return 1
    return 0


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
path = "Test-Taxi-information.xlsx"
workbook = openpyxl.load_workbook(path, data_only=True)


""" New administration windows """
# Customer window
def customer():
    def load_data():
        sheet = workbook['Customer']
        list_values = list(sheet.values)
        print(list_values)
        for col_name in list_values[0]:
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            treeview.insert('', tk.END, values=value_tuple)

    def enter_customer_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()

        if not Validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name")
        if not Validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
        else:
            path = "Test-Taxi-information.xlsx"
            workbook = openpyxl.load_workbook(path, data_only=True)
            customer_sheet = workbook['Customer']
            customer_id = f"D{random.randint(0, 999)}"
            customer_list = dr.take_customer_info()
            customer_id_list = []
            for customer in customer_list:
                customer_id_list.append(customer.get_id())
            while customer_id in customer_id_list:
                customer_id = f"C{random.randint(0, 999)}"

            row_values = [customer_id, name, phone_num]

            customer_sheet.append(row_values)
            workbook.save(path)
            treeview.insert('', tk.END, value=row_values)
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")

    # Saving User Info

    customer_window = tk.Tk()
    customer_window.title("Customer Admin")
    customer_frame = ttk.Frame(customer_window)
    customer_frame.pack()

    user_info_frame = tk.LabelFrame(customer_frame, text="Customer")
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

    # Button
    button = tk.Button(user_info_frame, text="Enter data", command=enter_customer_data)
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # disable placeholder
    name_entry.bind('<Button-1>', lambda x: on_focus_in(name_entry))
    name_entry.bind(
        '<FocusOut>', lambda x: on_focus_out(name_entry, 'Enter name'))

    phone_num_entry.bind('<Button-1>', lambda x: on_focus_in(phone_num_entry))
    phone_num_entry.bind('<FocusOut>', lambda x: on_focus_out(phone_num_entry, '0### ### ###'))

    treeFrame = ttk.Frame(customer_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")
    cols = ("id", "name", "phone_num")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("name", width=100)
    treeview.column("phone_num", width=100)
    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()
    customer_window.mainloop()


# Invoice window
def invoice():
    def load_data():
        sheet = workbook['Invoice']
        list_values = list(sheet.values)
        print(list_values)
        for col_name in list_values[0]:
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            treeview.insert('', tk.END, values=value_tuple)


    def enter_invoice_data():
        id = id_entry.get()
        customer_id = customer_id_entry.get()
        driver_id = driver_id_entry.get()
        date = date_entry.get()
        payment = payment_combobox.get()
        distance = distance_entry.get()
        price = price_combobox.get()
        if not Validation.is_valid_invoice_id(id) or id == "Enter ID":
            tkinter.messagebox.showwarning(title="Error", message="Invalid ID")
        if not Validation.is_valid_customer_id(customer_id) or customer_id == "Enter customer ID":
            tkinter.messagebox.showwarning(title="Error", message="Invalid customer ID")
        if not Validation.is_valid_driver_id(driver_id) or driver_id == "Enter driver ID":
            tkinter.messagebox.showwarning(title="Error", message="Invalid driver ID")
        if not Validation.is_valid_date(date) or date == "Enter date":
            tkinter.messagebox.showwarning(title="Error", message="Invalid date")
        if not Validation.is_valid_distance(distance) or distance == "Enter distance":
            tkinter.messagebox.showwarning(title="Error", message="Invalid distance")
        # time to add new invoice to the database

    invoice_window = tk.Tk()
    invoice_window.title("New invoice")
    invoice_frame = tk.Frame(invoice_window)
    invoice_frame.pack()

    invoice_info_frame = tk.LabelFrame(invoice_frame, text="Invoice info")
    invoice_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # id
    id_label = tk.Label(invoice_info_frame, text="ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(invoice_info_frame)
    id_entry.insert(0, "Enter ID")
    id_entry.configure(state='disabled')
    id_entry.grid(row=1, column=0)

    # customer_id
    customer_id_label = tk.Label(invoice_info_frame, text="Customer ID")
    customer_id_label.grid(row=0, column=1)
    customer_id_entry = tk.Entry(invoice_info_frame)
    customer_id_entry.insert(0, "Enter Customer ID")
    customer_id_entry.configure(state='disabled')
    customer_id_entry.grid(row=1, column=1)

    # driver_id
    driver_id_label = tk.Label(invoice_info_frame, text="Driver ID")
    driver_id_label.grid(row=0, column=2)
    driver_id_entry = tk.Entry(invoice_info_frame)
    driver_id_entry.insert(0, "Enter Driver ID")
    driver_id_entry.configure(state='disabled')
    driver_id_entry.grid(row=1, column=2)

    # date
    date_label = tk.Label(invoice_info_frame, text="Date")
    date_label.grid(row=2, column=0)
    date_entry = tk.Entry(invoice_info_frame)
    date_entry.insert(0, "Enter Date")
    date_entry.configure(state='disabled')
    date_entry.grid(row=3, column=0)

    # Way to payment
    payment_label = tk.Label(invoice_info_frame, text="Payment")
    payment_label.grid(row=2, column=1)
    payment_combobox = ttk.Combobox(invoice_info_frame, values=["Cash", "Banking"])
    payment_combobox.grid(row=3, column=1)

    # Distance
    distance_label = tk.Label(invoice_info_frame, text="Distance")
    distance_label.grid(row=4, column=0)
    distance_entry = tk.Entry(invoice_info_frame)
    distance_entry.insert(0, "Enter distance")
    distance_entry.configure(state='disabled')
    distance_entry.grid(row=5, column=0)

    # Price per km
    price_label = tk.Label(invoice_info_frame, text="Price")
    price_label.grid(row=4, column=1)
    price_combobox = ttk.Combobox(invoice_info_frame, values=["10.000", "13.000", "15.000"])
    price_combobox.grid(row=5, column=1)

    # Confirm button
    button = tk.Button(invoice_info_frame, text="Enter data", command=enter_invoice_data)
    button.grid(row=6, column=0, sticky="news", padx=20, pady=10)

    # Disable placeholder
    id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
    id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, 'Enter ID'))

    customer_id_entry.bind('<Button-1>', lambda x: on_focus_in(customer_id_entry))
    customer_id_entry.bind('<FocusOut>', lambda x: on_focus_out(customer_id_entry, 'Enter Customer ID'))

    driver_id_entry.bind('<Button-1>', lambda x: on_focus_in(driver_id_entry))
    driver_id_entry.bind('<FocusOut>', lambda x: on_focus_out(driver_id_entry, 'Enter Driver ID'))

    date_entry.bind('<Button-1>', lambda x: on_focus_in(date_entry))
    date_entry.bind('<FocusOut>', lambda x: on_focus_out(date_entry, 'Enter Date'))

    distance_entry.bind('<Button-1>', lambda x: on_focus_in(distance_entry))
    distance_entry.bind('<FocusOut>', lambda x: on_focus_out(distance_entry, 'Enter Distance'))

    for widget in invoice_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    treeFrame = ttk.Frame(invoice_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    cols = ("id", "customer_id", "driver_id", "date", "payment_mode", "distance", "price_per_km", "total_fee")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("customer_id", width=50)
    treeview.column("driver_id", width=50)
    treeview.column("date", width=67)
    treeview.column("payment_mode", width=70)
    treeview.column("distance", width=80)
    treeview.column("price_per_km", width=100)
    treeview.column("total_fee", width=70)

    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()


    invoice_window.mainloop()


# Vehicle window
def vehicle():
    def load_data():
        sheet = workbook['Vehicle']
        list_values = list(sheet.values)
        print(list_values)
        for col_name in list_values[0]:
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            treeview.insert('', tk.END, values=value_tuple)

    def enter_vehicle_data():
        type = type_combobox.get()
        regis_num = regis_num_entry.get()
        if not Validation.is_valid_vehicle_id(id) or id == "Enter id":
            tkinter.messagebox.showwarning(title="Error", message="Invalid id")
        if not Validation.is_valid_vehicle_type(type):
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type")
        if not Validation.is_valid_regis_num(regis_num) or regis_num == "Enter regis number":
            tkinter.messagebox.showwarning(title="Error", message="Invalid regis number")
        # Add new vehicle to database
        else:
            path = "Test-Taxi-information.xlsx"
            workbook = openpyxl.load_workbook(path, data_only=True)

            vehicle_sheet = workbook['Vehicle']
            vehicle_id = f"{type}{random.randint(0,999)}"
            vehicle_list = dr.take_vehicle_info()
            vehicle_id_list = []
            price = 0
            for vehicle in vehicle_list:
                vehicle_id_list.append(vehicle.get_id())
            while vehicle_id in vehicle_id_list:
                vehicle_id = f"{type}{random.randint(0, 999)}"
            if type == "5S":
                price = "10,000"
            if type == "7S":
                price = "13,000"
            if type == "9S":
                price = "15,000"

            row_values = [vehicle_id, type, regis_num, price]
            vehicle_sheet.append(row_values)
            workbook.save(path)

            treeview.insert('', tk.END, values=row_values)
            type_combobox.set(type_list[0])
            regis_num_entry.delete(0, "end")


    vehicle_window = tk.Tk()
    vehicle_window.title("New vehicle")
    vehicle_frame = tk.Frame(vehicle_window)
    vehicle_frame.pack()

    vehicle_info_frame = tk.LabelFrame(vehicle_frame, text="Vehicle info")
    vehicle_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # type
    type_list = ["5S", "7S", "9S"]
    type_label = tk.Label(vehicle_info_frame, text="Type")
    type_label.grid(row=0, column=1)
    type_combobox = ttk.Combobox(vehicle_info_frame, values=type_list)
    type_combobox.grid(row=1, column=1)

    # regis number
    regis_num_label = tk.Label(vehicle_info_frame, text="Regis number")
    regis_num_label.grid(row=0, column=0)
    regis_num_entry = tk.Entry(vehicle_info_frame)
    regis_num_entry.insert(0, "29–C1 233.23")
    regis_num_entry.configure(state='disabled')
    regis_num_entry.grid(row=1, column=0)

    # price
    price_label = tk.Label(vehicle_info_frame, text="Price")
    price_label.grid(row=0, column=3)
    price_info_label = tk.Label(vehicle_info_frame, text="5S - 10,000\n7S - 13,000\n9S - 15,000")
    price_info_label.grid(row=1, column=3)
    # Confirm button
    button = tk.Button(vehicle_info_frame, text="Enter data", command=enter_vehicle_data)
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Disable placeholder
    regis_num_entry.bind('<Button-1>', lambda x: on_focus_in(regis_num_entry))
    regis_num_entry.bind('<FocusOut>', lambda x: on_focus_out(regis_num_entry, 'Enter regis number'))

    for widget in vehicle_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    treeFrame = ttk.Frame(vehicle_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")
    cols = ("id", "type", "regis_num", "price")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("type", width=50)
    treeview.column("regis_num", width=100)
    treeview.column("price", width=70)
    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()

    vehicle_window.mainloop()


# Driver window
def driver():
    def delete_driver():
        # to be continue
        pass

    def load_data():
        sheet = workbook['Driver']
        list_values = list(sheet.values)
        print(list_values)
        for col_name in list_values[0]:
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            treeview.insert('', tk.END, values=value_tuple)

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
        if not Validation.is_valid_vehicle_id(vehicle_id) or vehicle_id == "#S###":
            # need to check whether the vehicle actually exist or available for assignment also bug
            tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle ID")
        if exist_vehicle_id(vehicle_id) == 1:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle already assigned")
        if exist_vehicle_id(vehicle_id) == 0:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle doesn't exist")
        if not Validation.is_valid_gender(gender):
            tkinter.messagebox.showwarning(title="Error", message="Invalid Gender")
        else:
            path = "Test-Taxi-information.xlsx"
            workbook = openpyxl.load_workbook(path, data_only=True)

            # The driver id need to be created by the system to make sure it's unique
            driver_sheet = workbook['Driver']
            driver_id = f"D{random.randint(0, 999)}"
            driver_list = dr.take_driver_info()
            driver_id_list = []
            for driver in driver_list:
                driver_id_list.append(driver.get_id())
            while driver_id in driver_id_list:
                driver_id = f"D{random.randint(0, 999)}"
            # appending the value into
            row_values = [driver_id, name, phone_num, vehicle_id, salary, gender, age]
            driver_sheet.append(row_values)
            workbook.save(path)

            treeview.insert('', tk.END, values=row_values)
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            vehicle_id_entry.delete(0, "end")
            salary_entry.delete(0, "end")
            gender_combobox.set(gender_combo_list[0])
            age_spinbox.delete(0, "end")



    # main frame for Driver Admin
    driver_window = tk.Tk()
    driver_window.title("Driver Admin")
    driver_frame = ttk.Frame(driver_window)
    driver_frame.pack()

    driver_info_frame = tk.LabelFrame(driver_frame, text="Driver info")
    driver_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # name
    name_label = tk.Label(driver_info_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(driver_info_frame)
    name_entry.insert(0, "Enter name")
    name_entry.configure(state='disabled')
    name_entry.grid(row=1, column=0)
    # phone number
    phone_num_label = tk.Label(driver_info_frame, text="Phone Number")
    phone_num_label.grid(row=0, column=1)
    phone_num_entry = tk.Entry(driver_info_frame)
    phone_num_entry.insert(0, "0### ### ###")
    phone_num_entry.configure(state='disabled')
    phone_num_entry.grid(row=1, column=1)
    # vehicle_id
    vehicle_id_label = tk.Label(driver_info_frame, text="Vehicle ID")
    vehicle_id_label.grid(row=0, column=2)
    vehicle_id_entry = tk.Entry(driver_info_frame)
    vehicle_id_entry.insert(0, "#S###")
    vehicle_id_entry.configure(state='disabled')
    vehicle_id_entry.grid(row=1, column=2)
    # salary
    salary_label = tk.Label(driver_info_frame, text="Salary")
    salary_label.grid(row=2, column=0)
    salary_entry = tk.Entry(driver_info_frame)
    salary_entry.grid(row=3, column=0)
    # gender
    gender_combo_list = ["Male", "Female", "Other"]
    gender_label = tk.Label(driver_info_frame, text="Gender")
    gender_label.grid(row=2, column=1)
    gender_combobox = ttk.Combobox(driver_info_frame, values=gender_combo_list)
    gender_combobox.grid(row=3, column=1)
    # age
    age_label = tk.Label(driver_info_frame, text="Age")
    age_label.grid(row=2, column=2)
    age_spinbox = tk.Spinbox(driver_info_frame, from_=0, to=200)
    age_spinbox.grid(row=3, column=2)
    # Confirm button
    button = tk.Button(driver_info_frame, text="Enter data", command=enter_driver_data)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    # Disable placeholder
    name_entry.bind('<Button-1>', lambda x: on_focus_in(name_entry))
    name_entry.bind('<FocusOut>', lambda x: on_focus_out(name_entry, 'Enter name'))

    phone_num_entry.bind('<Button-1>', lambda x: on_focus_in(phone_num_entry))
    phone_num_entry.bind('<FocusOut>', lambda x: on_focus_out(phone_num_entry, '0### ### ###'))

    vehicle_id_entry.bind('<Button-1>', lambda x: on_focus_in(vehicle_id_entry))
    vehicle_id_entry.bind('<FocusOut>', lambda x: on_focus_out(vehicle_id_entry, '#S###'))

    treeFrame = ttk.Frame(driver_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")
    cols = ("id", "name", "phone_num", "vehicle_id", "salary", "gender", "age")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("name", width=100)
    treeview.column("phone_num", width=100)
    treeview.column("vehicle_id", width=100)
    treeview.column("salary", width=100)
    treeview.column("gender", width=50)
    treeview.column("age", width=50)
    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()
    driver_window.mainloop()


"""The main window"""
window = tk.Tk()
window.title("Administration")
window.geometry("400x400")

frame = tk.Frame(window)
frame.pack()

# Driver
driver_button = tk.Button(frame, text="Driver Administration", command=driver)
driver_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

# Vehicle
vehicle_button = tk.Button(frame, text="Vehicle Administration", command=vehicle)
vehicle_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Invoice
invoice_button = tk.Button(frame, text="Invoice Administration", command=invoice)
invoice_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# Customer
customer_button = tk.Button(frame, text="Customer Administration", command=customer)
customer_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
window.mainloop()
