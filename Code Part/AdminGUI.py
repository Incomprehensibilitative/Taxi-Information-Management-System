"""Gui Using tkinter
> Common: Almost all of the windows have these same functions
    - load_data(): using the database_reader and create a treeview of all the data inside the GUI
    - delete_data():
        + Get the id of the data you want to delete
        + Using database_destroyer to delete the data from database
        + Get all the data that you want to delete by function get_ to update treeview
    - enter_data():
        + Validate user input from the GUI
        + Add data to database
        + Update the treeview in GUI 
> Special: Only resolve_invoice(), this update invoice table with the newest customer use of taxi client
> More detail on how the code run, read comment in Customer function, the rest will be the same
"""
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import openpyxl
import random

import database_creator as dc
import database_writer as dw
import validation
import get_


# Placeholder Function: Allow sample input to be shown
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


# load data from database to print onto GUI
path = "Taxi-information.xlsx"
workbook = openpyxl.load_workbook(path, data_only=True)


""" New administration windows """
# Customer window
def customer(window, system):
    def load_data():
        # define heading for the treeview
        head = ("id", "name", "phone_num", "chosen_vehicle")
        for heading_name in head:
            treeview.heading(heading_name, text=heading_name)
        # append customer data from customer list into treeview
        for customer in system.get_list("customer"):
            treeview.insert('', tk.END, values=(customer.get_id(), customer.get_name(), customer.get_phone_num(), customer.get_chosen_vehicle()))


    def delete_customer_data():
        id = id_entry.get()
        customer_name, customer_phone_num, customer_chosen_vehicle = get_.customer_data(system, id)
        system.delete_object("customer", id)
        for row in treeview.get_children():
            if treeview.item(row) == {'text': '', 'image': '', 'values': [id, customer_name, customer_phone_num, customer_chosen_vehicle], 'open': 0, 'tags': ''}:
                treeview.delete(row)
        id_entry.delete(0, "end")


    def enter_customer_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        chosen_vehicle = chosen_vehicle_combobox.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name")
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
        elif not validation.is_valid_vehicle_type(chosen_vehicle):
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type")
        else:

            customer_id = dc.create_customer_id(system)
            row_values = [customer_id, name, phone_num, chosen_vehicle]
            system.set_new_customer(row_values)

            treeview.insert('', tk.END, value=row_values)
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")

    def select_customer_data():
        # Disable placeholder
        name_entry.configure(state='normal')
        phone_num_entry.configure(state='normal')


        # Clear entry boxes
        name_entry.delete(0, "end")
        phone_num_entry.delete(0, "end")

        # Grab row to update
        selected = treeview.focus()

        # Grab data
        values = treeview.item(selected, 'values')

        # Output to boxes
        name_entry.insert(0, values[1])
        phone_num_entry.insert(0, values[2])
        chosen_vehicle_combobox.insert(0, values[3])
        chosen_vehicle_combobox.configure(state='disabled')

    def update_customer_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name")
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
        else:
            # To get the id, not other values
            selected = treeview.focus()
            values = treeview.item(selected, 'values')
            print(values)
            # Since the values[0] == id, so we want to keep it, and change other data
            updated_data = [values[0], name, phone_num, values[3]]
            system.update_customer(updated_data)
            treeview.item(selected, text="", values=(values[0], name, phone_num, values[3]))
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")

    # ============== Main window and Frames  ============== #
    # Main window 
    customer_window = tk.Toplevel(window)
    customer_window.title("Customer Admin")

    # Main frame
    customer_frame = ttk.Frame(customer_window)
    customer_frame.pack()

    # Frame for adding and modifying informations
    user_info_frame = tk.LabelFrame(customer_frame, text="Customer Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Frame for deleting the data
    delete_user_info_frame = tk.LabelFrame(customer_frame, text="Delete Customer")
    delete_user_info_frame.grid(row=1, column=0, pady=10)

    # ============== Basic information ============== #
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

    #Chosen vehicle
    type_list = ["5S", "7S", "9S"]
    chosen_vehicle_label = tk.Label(user_info_frame, text="Type")
    chosen_vehicle_label.grid(row=0, column=2)
    chosen_vehicle_combobox = ttk.Combobox(user_info_frame, values=type_list)
    chosen_vehicle_combobox.grid(row=1, column=2)

    # Id
    id_label = tk.Label(delete_user_info_frame, text="Customer ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_user_info_frame)
    id_entry.insert(0, "C#")
    id_entry.configure(state='disabled')
    id_entry.grid(row=1, column=0)


    # ============== Modification Buttons ============== #
    # Add Button
    add_button = tk.Button(user_info_frame, text="Enter data", command=enter_customer_data)
    add_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Select button
    select_button = tk.Button(user_info_frame, text="Select data", command=select_customer_data)
    select_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    # Update button 
    update_button = tk.Button(user_info_frame, text="Update data", command=update_customer_data)
    update_button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

    # Delete button
    delete_button = tk.Button(delete_user_info_frame, text = "Delete data", command=delete_customer_data)
    delete_button.grid(row=1, column=1,sticky="news", padx=20, pady=10)


    # Regriding widgets
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)


    # disable placeholder
    name_entry.bind('<Button-1>', lambda x: on_focus_in(name_entry))
    name_entry.bind('<FocusOut>', lambda x: on_focus_out(name_entry, 'Enter name'))

    phone_num_entry.bind('<Button-1>', lambda x: on_focus_in(phone_num_entry))
    phone_num_entry.bind('<FocusOut>', lambda x: on_focus_out(phone_num_entry, '0### ### ###'))

    id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
    id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, 'C#'))


    # ============== Treeview ============== #
    treeFrame = ttk.Frame(customer_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="both")
    cols = ("id", "name", "phone_num", "chosen_vehicle")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("name", width=100)
    treeview.column("phone_num", width=100)
    treeview.column("chosen_vehicle", width=150)
    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()


    customer_window.mainloop()

# Invoice window
def invoice(window, system):
    def resolve_invoice():
        invoice_id_list = []
        customer_id_list = []
        invoice_customer_id_list = []
        driver_id_list = []
        customer_chosen_vehicle_list = []
        payment_mode = ["cash", "banking"]

        for invoice in system.get_list("invoice"):
            invoice_id_list.append(invoice.get_id())
            invoice_customer_id_list.append(invoice.get_customer_id())

        for driver in system.get_list("driver"):
            driver_id_list.append(driver.get_id())

        for customer in system.get_list("customer"):
            customer_id_list.append(customer.get_id())
            customer_chosen_vehicle_list.append(customer.get_chosen_vehicle)

        unassigned_customer = []
        for element in customer_id_list:
            if element not in invoice_customer_id_list:
                unassigned_customer.append(element)

        for customer_id in unassigned_customer:
            customer_name, customer_phone_num, customer_chosen_vehicle = get_.customer_data(system, customer_id)
            invoice_id = dc.create_invoice_id()

            for driver in system.get_list("driver"):
                driver_vehicle_id = driver.get_vehicle_id()
                driver_vehicle_type = driver_vehicle_id[:2]
                if driver_vehicle_type == customer_chosen_vehicle:
                    driver_id = driver.get_id()


            # need a date randomizer
            date = dc.create_date()
            payment = random.choice(payment_mode)
            distance = random.randint(0, 100)
            price_per_km = dc.create_price(customer_chosen_vehicle)
            total_fee = distance*int(price_per_km)

            row_values = [invoice_id, customer_id, driver_id, date, payment, distance, price_per_km, total_fee]
            system.set_new_invoice(row_values)

            treeview.insert('', tk.END, value=row_values)

    def load_data():
        head = ("id", "customer_id", "driver_id", "date", "payment_mode", "distance", "price_per_km", "total_fee")
        for head_name in head:
            treeview.heading(head_name, text=head_name)

        for invoice in system.get_list("invoice"):
            treeview.insert('', tk.END, values=(invoice.get_id(), invoice.get_customer_id(), invoice.get_driver_id(), invoice.get_date(),
                                                invoice.get_payment_mode(), invoice.get_distance(), invoice.get_price_per_km(), invoice.get_total()))

    invoice_window = tk.Toplevel(window)
    invoice_window.title("New invoice")
    invoice_frame = tk.Frame(invoice_window)
    invoice_frame.pack()

    # ============== Treeview  ============== #
    treeFrame = ttk.Frame(invoice_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="both")
    cols = ("id", "customer_id", "driver_id", "date", "payment_mode", "distance", "price_per_km", "total_fee")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=50)
    treeview.column("customer_id", width=100)
    treeview.column("driver_id", width=100)
    treeview.column("date", width=85)
    treeview.column("payment_mode", width=150)
    treeview.column("distance", width=80)
    treeview.column("price_per_km", width=150)
    treeview.column("total_fee", width=100)
    treeview.pack()
    treeScroll.config(command=treeview.yview())

    # ============== Resolve all invoice before loading Treeview  ============== #
    load_data()
    resolve_invoice()


    invoice_window.mainloop()


# Vehicle window
def vehicle(window, system):
    # ============== Main functions ============== #
    def load_data():
        head = ("id", "type", "regis_num", "price")
        for heading_name in head:
            treeview.heading(heading_name, text=heading_name)

        for vehicle in system.get_list("vehicle"):
            treeview.insert('', tk.END, values=(vehicle.get_id(), vehicle.get_type(), vehicle.get_regis_num(), vehicle.get_price()))

    def delete_vehicle_data():
        id = id_entry.get()
        type, regis_num, price = get_.vehicle_data(system, id)
        system.delete_object("vehicle", id)
        for row in treeview.get_children():
            if treeview.item(row) == {'text': '', 'image': '', 'values': [id, type, regis_num, price], 'open': 0, 'tags': ''}:
                treeview.delete(row)

    def enter_vehicle_data():
        type = type_combobox.get()
        regis_num = regis_num_entry.get()
        if not validation.is_valid_vehicle_type(type):
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type")
        elif not validation.is_valid_regis_num(regis_num) or regis_num == "Enter regis number":
            tkinter.messagebox.showwarning(title="Error", message="Invalid regis number")
        else:

            vehicle_id = dc.create_vehicle_id(system, type)
            price = dc.create_price(type)
            assign = "false"
            row_values = [vehicle_id, type, regis_num, price, assign]
            system.set_new_vehicle(row_values)

            treeview.insert('', tk.END, values=row_values)
            type_combobox.delete(0, "end")
            regis_num_entry.delete(0, "end")

    def select_vehicle_data():
        # Disable placeholder
        type_combobox.configure(state='normal')
        regis_num_entry.configure(state='normal')

        # Clear entry boxes
        type_combobox.delete(0, "end")
        regis_num_entry.delete(0, "end")

        # Grab row to update
        selected = treeview.focus()

        # Grab data
        values = treeview.item(selected, 'values')

        # Output to boxes
        type_combobox.insert(0, values[1])
        regis_num_entry.insert(0, values[2])

    def update_vehicle_data():
        type = type_combobox.get()
        regis_num = regis_num_entry.get()
        if not validation.is_valid_vehicle_type(type):
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type")
        elif not validation.is_valid_regis_num(regis_num) or regis_num == "Enter regis number":
            tkinter.messagebox.showwarning(title="Error", message="Invalid regis number")
        else:
            selected = treeview.focus()
            values = treeview.item(selected, 'values')
            if type != values[1]:
                new_vehicle_id = dc.create_vehicle_id(system, type)
                new_price = dc.create_price(type)
                old_vehicle_id = values[0]
                updated_data1 = [new_vehicle_id, type, regis_num, new_price, old_vehicle_id]
                system.update_vehicle(updated_data1)
                treeview.item(selected, text="", values=(new_vehicle_id, type, regis_num, new_price))
            else:
                updated_data2 = [values[0], values[1], regis_num, values[3], values[0]]
                system.update_vehicle(updated_data2)
                treeview.item(selected, text="", values=(values[0], values[1], regis_num, values[3]))

    # ============== Main window and Frames  ============== #
    # Main window 
    vehicle_window = tk.Toplevel(window)
    vehicle_window.title("New vehicle")

    # Main frame 
    vehicle_frame = tk.Frame(vehicle_window)
    vehicle_frame.pack()

    # Frame for adding and modifying informations
    vehicle_info_frame = tk.LabelFrame(vehicle_frame, text="Vehicle info")
    vehicle_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Frame for deleting the data  
    delete_vehicle_info_frame = tk.LabelFrame(vehicle_frame, text="Delete Vehicle")
    delete_vehicle_info_frame.grid(row=1, column=0, pady=10)

    # ============== Basic information ============== #
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
    # the dash might create error
    regis_num_entry.insert(0, "29-C1 233.23")
    regis_num_entry.configure(state='disabled')
    regis_num_entry.grid(row=1, column=0)

    # price
    price_label = tk.Label(vehicle_info_frame, text="Price")
    price_label.grid(row=0, column=3)
    price_info_label = tk.Label(vehicle_info_frame, text="5S - 10,000\n7S - 13,000\n9S - 15,000")
    price_info_label.grid(row=1, column=3)

    # Id
    id_label = tk.Label(delete_vehicle_info_frame, text="Vehicle ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_vehicle_info_frame)
    id_entry.insert(0, "#S###")
    id_entry.configure(state='disabled')
    id_entry.grid(row=1, column=0)

    # ============== Modification Buttons ============== #
    # Add button
    button = tk.Button(vehicle_info_frame, text="Enter data", command=enter_vehicle_data)
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Select button
    select_button = tk.Button(vehicle_info_frame, text="Select data", command=select_vehicle_data)
    select_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    # Update button 
    update_button = tk.Button(vehicle_info_frame, text="Update data", command=update_vehicle_data)
    update_button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

    # Delete button
    delete_button = tk.Button(delete_vehicle_info_frame, text = "Delete data", command=delete_vehicle_data)
    delete_button.grid(row=1, column=1,sticky="news", padx=20, pady=10)

    # ============== Others ============== #
    # Regriding widgets
    for widget in vehicle_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Disable placeholder
    regis_num_entry.bind('<Button-1>', lambda x: on_focus_in(regis_num_entry))
    regis_num_entry.bind('<FocusOut>', lambda x: on_focus_out(regis_num_entry, 'Enter regis number'))

    id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
    id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, '#S###'))

     # ============== Treeview ============== #
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
def driver(window, system):
    def load_data():
        head_driver = ("id", "name", "phone_num", "vehicle_id", "salary", "gender", "age")
        for heading_name in head_driver:
            treeview.heading(heading_name, text=heading_name)
        for driver in system.get_list("driver"):
            treeview.insert('', tk.END, values=(driver.get_id(), driver.get_name(), driver.get_phone_num(), driver.get_vehicle_id(), driver.get_salary(), driver.get_gender(), driver.get_age()))

        head_vehicle = ("unassign_vehicle_id")
        treeview_vehicle.heading(head_vehicle, text=head_vehicle)
        for vehicle in dc.create_unassign_vehicle_list(system):
            treeview_vehicle.insert('', tk.END, values=(vehicle))

    def delete_driver_data():
        id = id_entry.get()
        driver_name, driver_phone_num, driver_vehicle_id, driver_salary, driver_gender, driver_age = get_.driver_data(system, id)
        system.delete_object("driver", id)
        for row in treeview.get_children():
            if treeview.item(row) == {'text': '', 'image': '', 'values': [id, driver_name, driver_phone_num, driver_vehicle_id, driver_salary, driver_gender, driver_age], 'open': 0, 'tags': ''}:
                treeview.delete(row)


    def enter_driver_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        vehicle_id = vehicle_id_entry.get()
        salary = salary_entry.get()
        gender = gender_combobox.get()
        age = age_spinbox.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name")
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
        elif not validation.is_valid_vehicle_id(vehicle_id) or vehicle_id == "#S###":
            # need to check whether the vehicle actually exist or available for assignment also bug
            tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle ID")
        elif validation.exist_vehicle_id(system, vehicle_id) == 1:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle already assigned")
        elif validation.exist_vehicle_id(system, vehicle_id) == 0:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle doesn't exist")
        elif not validation.is_valid_gender(gender):
            tkinter.messagebox.showwarning(title="Error", message="Invalid Gender")
        else:
            # The id need to be created by the system to make sure it's unique
            driver_id = dc.create_driver_id(system)
            # appending the value into
            get_.vehicle_assignment(system, vehicle_id)
            row_values = [driver_id, name, phone_num, vehicle_id, salary, gender, age]
            system.set_new_driver(row_values)

            treeview.insert('', tk.END, values=row_values)

            for row in treeview_vehicle.get_children():
                if treeview_vehicle.item(row) == {'text': '', 'image': '', 'values': [vehicle_id], 'open': 0, 'tags': ''}:
                    treeview_vehicle.delete(row)

            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            vehicle_id_entry.delete(0, "end")
            salary_entry.delete(0, "end")
            gender_combobox.set(gender_combo_list[0])
            age_spinbox.delete(0, "end")

    def select_driver_data():
        # Disable placeholder
        name_entry.configure(state='normal')
        phone_num_entry.configure(state='normal')
        vehicle_id_entry.configure(state='normal')
        salary_entry.configure(state='normal')
        gender_combobox.configure(state='normal')
        age_spinbox.configure(state='normal')

        # Clear boxes
        name_entry.delete(0, "end")
        phone_num_entry.delete(0, "end")
        vehicle_id_entry.delete(0, "end")
        salary_entry.delete(0, "end")
        gender_combobox.delete(0, "end")
        age_spinbox.delete(0, "end")

        # Grab row to update
        selected = treeview.focus()

        # Grab data
        values = treeview.item(selected, 'values')

        # Output data to boxes
        name_entry.insert(0, values[1])
        phone_num_entry.insert(0, values[2])
        vehicle_id_entry.insert(0, values[3])
        salary_entry.insert(0, values[4])
        gender_combobox.insert(0, values[5])
        age_spinbox.insert(0, values[6])


    def update_driver_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        vehicle_id = vehicle_id_entry.get()
        salary = salary_entry.get()
        gender = gender_combobox.get()
        age = age_spinbox.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name")
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number")
        elif not validation.is_valid_vehicle_id(vehicle_id) or vehicle_id == "#S###":
            # need to check whether the vehicle actually exist or available for assignment also bug
            tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle ID")
        # Need new validation
        elif validation.exist_vehicle_id(system, vehicle_id) == 2:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle already assigned")
        elif validation.exist_vehicle_id(system, vehicle_id) == 0:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle doesn't exist")
        elif not validation.is_valid_gender(gender):
            tkinter.messagebox.showwarning(title="Error", message="Invalid Gender")
        else:
            # To get the values[0] == id, not other values
            selected = treeview.focus()
            values = treeview.item(selected, 'values')

            updated_data = [values[0], name, phone_num, vehicle_id, salary, age, gender]
            system.update_driver(updated_data)
            
            treeview.item(selected, text="", values=(values[0], name, phone_num, vehicle_id, salary, gender, age))
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            vehicle_id_entry.delete(0, "end")
            salary_entry.delete(0, "end")
            gender_combobox.delete(0, "end")
            age_spinbox.delete(0, "end")

    # ============== Main window and Frames  ============== #
    # Main window

    driver_window = tk.Toplevel(window)
    driver_window.title("Driver Admin")

    # Main frame
    driver_frame = ttk.Frame(driver_window)
    driver_frame.pack()


    # Frame for adding and modifying informations
    driver_info_frame = tk.LabelFrame(driver_frame, text="Driver info")
    driver_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Frame for deleting the data
    delete_driver_info_frame = tk.LabelFrame(driver_frame, text="Delete Driver")
    delete_driver_info_frame.grid(row=1, column=0, pady=10)

    # ============== Basic information ============== #
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

    # Id
    id_label = tk.Label(delete_driver_info_frame, text="Driver ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_driver_info_frame)
    id_entry.insert(0, "D#")
    id_entry.configure(state='disabled')
    id_entry.grid(row=1, column=0)


    # ============== Modification Buttons ============== #
    # Add button
    add_button = tk.Button(driver_info_frame, text="Enter data", command=enter_driver_data)
    add_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    # Select button
    select_button = tk.Button(driver_info_frame, text="Select data", command=select_driver_data)
    select_button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

    # Update button 
    update_button = tk.Button(driver_info_frame, text="Update data", command=update_driver_data)
    update_button.grid(row=5, column=1, sticky="news", padx=20, pady=10)

    # Delete button
    delete_button = tk.Button(delete_driver_info_frame, text = "Delete data", command=delete_driver_data)
    delete_button.grid(row=3, column=1,sticky="news", padx=20, pady=10)


    # ============== Others ============== #
    # Disable placeholder
    name_entry.bind('<Button-1>', lambda x: on_focus_in(name_entry))
    name_entry.bind('<FocusOut>', lambda x: on_focus_out(name_entry, 'Enter name'))

    phone_num_entry.bind('<Button-1>', lambda x: on_focus_in(phone_num_entry))
    phone_num_entry.bind('<FocusOut>', lambda x: on_focus_out(phone_num_entry, '0### ### ###'))

    vehicle_id_entry.bind('<Button-1>', lambda x: on_focus_in(vehicle_id_entry))
    vehicle_id_entry.bind('<FocusOut>', lambda x: on_focus_out(vehicle_id_entry, '#S###'))

    id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
    id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, 'D#'))

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
    treeview.column("gender", width=70)
    treeview.column("age", width=50)
    treeview.pack()
    treeScroll.config(command=treeview.yview())

    # ============== Treeview to show avaiavle vehicle ============== #
    treeFrame_vehicle = ttk.Frame(driver_frame)
    treeFrame_vehicle.grid(row=0, column=2, pady=10)
    treeScroll_vehicle = ttk.Scrollbar(treeFrame_vehicle)
    treeScroll_vehicle.pack(side="right", fill="y")
    cols_vehicle = ("unassign_vehicle_id")
    treeview_vehicle = ttk.Treeview(treeFrame_vehicle, show="headings", yscrollcommand=treeScroll_vehicle.set, columns=cols_vehicle, height=13)
    treeview_vehicle.column("unassign_vehicle_id", width=150)
    treeview_vehicle.pack()
    treeScroll_vehicle.config(command=treeview_vehicle.yview())

    load_data()
    driver_window.mainloop()

# Saving the data to excel when closing the GUI
def on_closing(window, system):
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit, all changes will be save to database"):
        dw.write_data(system)
        window.destroy()


"""The main window"""
def main(system):
    # ============== Main window and Frames  ============== #
    window = tk.Tk()
    window.title("Administration")
    window.geometry("400x400")

    frame = tk.Frame(window)
    frame.pack()

    # ============== Open Different Administration Windows  ============== #
    # limit number of window opened

    # Driver
    driver_button = tk.Button(frame, text="Driver Administration", command=lambda: driver(window, system))
    driver_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    # Vehicle
    vehicle_button = tk.Button(frame, text="Vehicle Administration", command=lambda: vehicle(window, system))
    vehicle_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

    # Invoice
    invoice_button = tk.Button(frame, text="Print Invoice", command=lambda: invoice(window, system))
    invoice_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    # Customer
    customer_button = tk.Button(frame, text="Customer Administration", command=lambda: customer(window, system))
    customer_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Check if window is being close
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window, system))

    window.mainloop()