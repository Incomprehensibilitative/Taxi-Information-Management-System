import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import Validation
import openpyxl


""" Common functions """
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
# Invoice window
def invoice():
    def new_invoice():
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

        new_invoice_window = tk.Tk()
        new_invoice_window.title("New invoice")
        new_invoice_frame = tk.Frame(new_invoice_window)
        new_invoice_frame.grid(row=0, column=0, padx=20, pady=10)

        # id
        id_label = tk.Label(new_invoice_frame, text="ID")
        id_label.grid(row=0, column=0)
        id_entry = tk.Entry(new_invoice_frame)
        id_entry.insert(0, "Enter ID")
        id_entry.configure(state='disabled')
        id_entry.grid(row=1, column=0)

        # customer_id
        customer_id_label = tk.Label(new_invoice_frame, text="Customer ID")
        customer_id_label.grid(row=0, column=1)
        customer_id_entry = tk.Entry(new_invoice_frame)
        customer_id_entry.insert(0, "Enter Customer ID")
        customer_id_entry.configure(state='disabled')
        customer_id_entry.grid(row=1, column=1)

        # driver_id
        driver_id_label = tk.Label(new_invoice_frame, text="Driver ID")
        driver_id_label.grid(row=0, column=2)
        driver_id_entry = tk.Entry(new_invoice_frame)
        driver_id_entry.insert(0, "Enter Driver ID")
        driver_id_entry.configure(state='disabled')
        driver_id_entry.grid(row=1, column=2)

        # date
        date_label = tk.Label(new_invoice_frame, text="Date")
        date_label.grid(row=2, column=0)
        date_entry = tk.Entry(new_invoice_frame)
        date_entry.insert(0, "Enter Date")
        date_entry.configure(state='disabled')
        date_entry.grid(row=3, column=0)

        # Way to payment
        payment_label = tk.Label(new_invoice_frame, text="Payment")
        payment_label.grid(row=2, column=1)
        payment_combobox = ttk.Combobox(new_invoice_frame, values=["Cash", "Banking"])
        payment_combobox.grid(row=3, column=1)

        # Distance
        distance_label = tk.Label(new_invoice_frame, text="Distance")
        distance_label.grid(row=4, column=0)
        distance_entry = tk.Entry(new_invoice_frame)
        distance_entry.insert(0, "Enter distance")
        distance_entry.configure(state='disabled')
        distance_entry.grid(row=5, column=0)

        # Price per km
        price_label = tk.Label(new_invoice_frame, text="Price")
        price_label.grid(row=4, column=1)
        price_combobox = ttk.Combobox(new_invoice_frame, values=["10.000", "13.000", "15.000"])
        price_combobox.grid(row=5, column=1)

        # Total price
        # def multi():
        #    m = distance_entry + price_entry
        #    print(m)
        total_label = tk.Label(new_invoice_frame, text="Total")
        total_label.grid(row=4, column=2)
        total_value = price_combobox * distance_entry
        total_value.grid(row=5, column=2)

        # Confirm button
        button = tk.Button(new_invoice_frame, text="Enter data", command=enter_invoice_data)
        button.grid(row=6, column=2, sticky="news", padx=20, pady=10)

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

        for widget in new_invoice_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    invoice_window = tk.Tk()
    invoice_window.title("Invoice Admin")
    invoice_frame = tk.Frame(invoice_window)
    invoice_frame.grid(row=0, column=0, padx=20, pady=10)
    new_invoice_button = tk.Button(invoice_frame, text="New Invoice", command=new_invoice)
    new_invoice_button.grid(row=0, column=0, padx=20, pady=10)

    invoice_window.mainloop()


# Vehicle window
def vehicle():
    def new_vehicle():
        def enter_vehicle_data():
            id = id_entry.get()
            type = type_combobox.get()
            regis_num = regis_num_entry.get()
            price = price_combobox.get()
            if not Validation.is_valid_vehicle_id(id) or id == "Enter id":
                tkinter.messagebox.showwarning(title="Error", message="Invalid id")
            if not Validation.is_valid_regis_num(regis_num) or regis_num == "Enter regis number":
                tkinter.messagebox.showwarning(title="Error", message="Invalid regis number")
            # Add new vehicle to database

        new_vehicle_window = tk.Tk()
        new_vehicle_window.title("New vehicle")
        new_vehicle_frame = tk.Frame(new_vehicle_window)
        new_vehicle_frame.grid(row=0, column=0, padx=20, pady=10)

        # id
        id_label = tk.Label(new_vehicle_frame, text="ID")
        id_label.grid(row=0, column=0)
        id_entry = tk.Entry(new_vehicle_frame)
        id_entry.insert(0, "Enter ID")
        id_entry.configure(state='disabled')
        id_entry.grid(row=1, column=0)

        # type
        type_label = tk.Label(new_vehicle_frame, text="Type")
        type_label.grid(row=0, column=1)
        type_combobox = ttk.Combobox(new_vehicle_frame, values=["5S", "7S", "9S"])
        type_combobox.grid(row=1, column=1)

        # regis number
        regis_num_label = tk.Label(new_vehicle_frame, text="Regis number")
        regis_num_label.grid(row=2, column=0)
        regis_num_entry = tk.Entry(new_vehicle_frame)
        regis_num_entry.insert(0, "Enter Regis Num")
        regis_num_entry.configure(state='disabled')
        regis_num_entry.grid(row=3, column=0)

        # price
        price_label = tk.Label(new_vehicle_frame, text="Price")
        price_label.grid(row=2, column=1)
        price_combobox = ttk.Combobox(new_vehicle_frame, values=["10.000", "13.000", "15.000"])
        price_combobox.grid(row=3, column=1)

        # Confirm button
        button = tk.Button(new_vehicle_frame, text="Enter data", command=enter_vehicle_data)
        button.grid(row=3, column=2)

        # Disable placeholder
        id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
        id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, 'Enter name'))

        regis_num_entry.bind('<Button-1>', lambda x: on_focus_in(regis_num_entry))
        regis_num_entry.bind('<FocusOut>', lambda x: on_focus_out(regis_num_entry, 'Enter regis number'))

        for widget in new_vehicle_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    vehicle_window = tk.Tk()
    vehicle_window.title("Vehicle Admin")
    vehicle_frame = tk.Frame(vehicle_window)
    vehicle_frame.grid(row=0, column=0, padx=20, pady=10)
    new_vehicle_button = tk.Button(vehicle_frame, text="New Vehicle", command=new_vehicle)
    new_vehicle_button.grid(row=0, column=0, padx=20, pady=10)

    vehicle_window.mainloop()


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


window.mainloop()
