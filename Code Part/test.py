import openpyxl
from Model import Customer, Vehicle, Driver, Feedback, Invoice

data = openpyxl.load_workbook("Taxi-information.xlsx", read_only=True, data_only=True)

# sheet = data['Customer']
# customer_list = []
# for row in sheet:
#     new_customer = Customer.Customer()
#     new_customer.set_customer(row[0].value, row[1].value, row[2].value)
#     customer_list.append(new_customer)
# for element in customer_list:
#     print("{:8} {:<15} {:<15}".format(element.get_id(), element.get_name(), element.get_phone_num()))

# sheet = data['Vehicle']
# vehicle_list = []
# for row in sheet:
#     new_vehicle = Vehicle.Vehicle()
#     new_vehicle.set_vehicle(row[0].value, row[1].value, row[2].value, row[3].value)
#     vehicle_list.append(new_vehicle)
# for element in vehicle_list:
#     print("{:8} {:5} {:15} {}".format(element.get_id(), element.get_type(), element.get_regis(), element.get_price()))
#
# sheet = data['Driver']
# print(sheet.max_column)
# driver_list = []
# for row in sheet:
#     new_driver = Driver.Driver()
#     new_driver.set_driver(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value)
#     driver_list.append(new_driver)
# for element in driver_list:
#     print("{:3} {:7} {:12} {:8} {:10} {:7} {:3}".format(element.get_id(), element.get_name(), element.get_phone(), element.get_vehicle_id(), element.get_salary(), element.get_gender(), element.get_age()))

# invoice GUI
    # def enter_invoice_data():
    #     id = id_entry.get()
    #     customer_id = customer_id_entry.get()
    #     driver_id = driver_id_entry.get()
    #     date = date_entry.get()
    #     payment = payment_combobox.get()
    #     distance = distance_entry.get()
    #     price = price_combobox.get()
    #     if not validation.is_valid_invoice_id(id) or id == "Enter ID":
    #         tkinter.messagebox.showwarning(title="Error", message="Invalid ID")
    #     elif not validation.is_valid_customer_id(customer_id) or customer_id == "Enter customer ID":
    #         tkinter.messagebox.showwarning(title="Error", message="Invalid customer ID")
    #     elif not validation.is_valid_driver_id(driver_id) or driver_id == "Enter driver ID":
    #         tkinter.messagebox.showwarning(title="Error", message="Invalid driver ID")
    #     elif not validation.is_valid_date(date) or date == "Enter date":
    #         tkinter.messagebox.showwarning(title="Error", message="Invalid date")
    #     elif not validation.is_valid_distance(distance) or distance == "Enter distance":
    #         tkinter.messagebox.showwarning(title="Error", message="Invalid distance")
    #     # time to add new invoice to the database

    # invoice_info_frame = tk.LabelFrame(invoice_frame, text="Invoice info")
    # invoice_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # # id
    # id_label = tk.Label(invoice_info_frame, text="ID")
    # id_label.grid(row=0, column=0)
    # id_entry = tk.Entry(invoice_info_frame)
    # id_entry.insert(0, "Enter ID")
    # id_entry.configure(state='disabled')
    # id_entry.grid(row=1, column=0)

    # # customer_id
    # customer_id_label = tk.Label(invoice_info_frame, text="Customer ID")
    # customer_id_label.grid(row=0, column=1)
    # customer_id_entry = tk.Entry(invoice_info_frame)
    # customer_id_entry.insert(0, "Enter Customer ID")
    # customer_id_entry.configure(state='disabled')
    # customer_id_entry.grid(row=1, column=1)

    # # driver_id
    # driver_id_label = tk.Label(invoice_info_frame, text="Driver ID")
    # driver_id_label.grid(row=0, column=2)
    # driver_id_entry = tk.Entry(invoice_info_frame)
    # driver_id_entry.insert(0, "Enter Driver ID")
    # driver_id_entry.configure(state='disabled')
    # driver_id_entry.grid(row=1, column=2)

    # # date
    # date_label = tk.Label(invoice_info_frame, text="Date")
    # date_label.grid(row=2, column=0)
    # date_entry = tk.Entry(invoice_info_frame)
    # date_entry.insert(0, "Enter Date")
    # date_entry.configure(state='disabled')
    # date_entry.grid(row=3, column=0)

    # # Way to payment
    # payment_label = tk.Label(invoice_info_frame, text="Payment")
    # payment_label.grid(row=2, column=1)
    # payment_combobox = ttk.Combobox(invoice_info_frame, values=["Cash", "Banking"])
    # payment_combobox.grid(row=3, column=1)

    # # Distance
    # distance_label = tk.Label(invoice_info_frame, text="Distance")
    # distance_label.grid(row=4, column=0)
    # distance_entry = tk.Entry(invoice_info_frame)
    # distance_entry.insert(0, "Enter distance")
    # distance_entry.configure(state='disabled')
    # distance_entry.grid(row=5, column=0)

    # # Price per km
    # price_label = tk.Label(invoice_info_frame, text="Price")
    # price_label.grid(row=4, column=1)
    # price_combobox = ttk.Combobox(invoice_info_frame, values=["10.000", "13.000", "15.000"])
    # price_combobox.grid(row=5, column=1)

    # # Confirm button
    # button = tk.Button(invoice_info_frame, text="Enter data", command=enter_invoice_data)
    # button.grid(row=6, column=0, sticky="news", padx=20, pady=10)

    # # Disable placeholder
    # id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
    # id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, 'Enter ID'))

    # customer_id_entry.bind('<Button-1>', lambda x: on_focus_in(customer_id_entry))
    # customer_id_entry.bind('<FocusOut>', lambda x: on_focus_out(customer_id_entry, 'Enter Customer ID'))

    # driver_id_entry.bind('<Button-1>', lambda x: on_focus_in(driver_id_entry))
    # driver_id_entry.bind('<FocusOut>', lambda x: on_focus_out(driver_id_entry, 'Enter Driver ID'))

    # date_entry.bind('<Button-1>', lambda x: on_focus_in(date_entry))
    # date_entry.bind('<FocusOut>', lambda x: on_focus_out(date_entry, 'Enter Date'))

    # distance_entry.bind('<Button-1>', lambda x: on_focus_in(distance_entry))
    # distance_entry.bind('<FocusOut>', lambda x: on_focus_out(distance_entry, 'Enter Distance'))

    # for widget in invoice_info_frame.winfo_children():
    #     widget.grid_configure(padx=10, pady=5)
