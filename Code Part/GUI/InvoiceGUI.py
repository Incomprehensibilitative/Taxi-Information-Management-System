import tkinter as tk
from tkinter import ttk
import random
from Control import get_
from Control import database_creator as dc


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
            customer_name, customer_phone_num, customer_chosen_vehicle, customer_pick_up_spot = get_.customer_data(
                system, customer_id)
            invoice_id = dc.create_invoice_id(system)

            for driver in system.get_list("driver"):
                if driver.get_vehicle_id() is None:
                    continue
                else:
                    driver_vehicle_id = driver.get_vehicle_id()
                    driver_vehicle_type = driver_vehicle_id[:2]
                    if driver_vehicle_type == customer_chosen_vehicle:
                        driver_id = driver.get_id()

            # need a date randomizer
            date = dc.create_date()
            payment = random.choice(payment_mode)
            distance = random.randint(0, 100)
            price_per_km = dc.create_price(customer_chosen_vehicle)
            total_fee = distance * int(price_per_km)

            row_values = [invoice_id, customer_id, driver_id, date, payment, distance, price_per_km, total_fee]
            system.set_new_invoice(row_values)

            treeview.insert('', tk.END, value=row_values)

    def load_data():
        head = ("id", "customer_id", "driver_id", "date", "payment_mode", "distance", "price_per_km", "total_fee")
        for head_name in head:
            treeview.heading(head_name, text=head_name)

        for invoice in system.get_list("invoice"):
            treeview.insert('', tk.END, values=(
                invoice.get_id(), invoice.get_customer_id(), invoice.get_driver_id(), invoice.get_date(),
                invoice.get_payment_mode(), invoice.get_distance(), invoice.get_price_per_km(), invoice.get_total()))

    # ============== Main window and Frames  ============== #
    # check if a frame already exists in the window grid in position 0,1 (row 0, column 1) and destroy it
    if len(window.grid_slaves(row=0, column=1)) > 0:
        window.grid_slaves(row=0, column=1)[0].destroy()

    invoice_frame = tk.Frame(window)
    invoice_frame.grid(row=0, column=1, padx=20, sticky="nsew")

    # ============== Treeview  ============== #
    treeFrame = ttk.Frame(invoice_frame)
    treeFrame.grid(row=0, column=1, pady=10, sticky="nsew")
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="both")
    cols = ("id", "customer_id", "driver_id", "date", "payment_mode", "distance", "price_per_km", "total_fee")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=65)
    treeview.column("customer_id", width=110)
    treeview.column("driver_id", width=100)
    treeview.column("date", width=125)
    treeview.column("payment_mode", width=140)
    treeview.column("distance", width=80)
    treeview.column("price_per_km", width=120)
    treeview.column("total_fee", width=120)
    treeview.pack()
    treeScroll.config(command=treeview.yview())

    # ============== Resolve all invoice before loading Treeview  ============== #
    load_data()
    resolve_invoice()

    invoice_frame.columnconfigure(0, weight=1)
    invoice_frame.columnconfigure(1, weight=1)
    invoice_frame.columnconfigure(2, weight=1)
