"""Gui Using tkinter
> Common: Almost all the windows have these same functions
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
from Control import database_writer as dw
from GUI import DriverGUI, VehicleGUI, InvoiceGUI, CustomerGUI

# Saving the data to excel when closing the GUI
def on_closing(window, system):
    msg_box = tkinter.messagebox.askokcancel("Save", "Do you want to quit, all changes will be save to database")
    if msg_box == True:
        print("Saving data to excel")
        dw.write_data(system)
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit"):
        window.destroy()


"""The main window"""


def main(system):
    # ============== Main window and Frames  ============== #
    window = tk.Tk()
    window.tk.call("source", "Azure-ttk-theme/azure.tcl")
    window.tk.call("set_theme", "dark")
    style = ttk.Style()
    style.configure("Treeview", rowheight=30)
    window.title("Administration")
    window.geometry("400x400")

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, sticky="nsew")

    # Add invisible row to the top
    frame.rowconfigure(0, weight=1)
    ttk.Label(frame).grid(row=0, column=0, columnspan=3)

    # Add an outline to the frame
    frame["borderwidth"] = 3
    frame["relief"] = "sunken"

    
    # Driver
    driver_button = ttk.Button(frame, text="Driver Administration", command=lambda: DriverGUI.driver(window, system))
    driver_button.grid(row=1, column=1, sticky="ew", padx=20, pady=10)
    
    # Vehicle
    vehicle_button = ttk.Button(frame, text="Vehicle Administration", command=lambda: VehicleGUI.vehicle(window, system))
    vehicle_button.grid(row=2, column=1, sticky="ew", padx=20, pady=10)

    # Customer
    customer_button = ttk.Button(frame, text="Customer Administration", command=lambda: CustomerGUI.customer(window, system))
    customer_button.grid(row=3, column=1, sticky="ew", padx=20, pady=10)

    # Invoice
    invoice_button = ttk.Button(frame, text="Show Invoices", command=lambda: InvoiceGUI.invoice(window, system))
    invoice_button.grid(row=4, column=1, sticky="ew", padx=20, pady=10)

    # Add invisible row to the bottom
    frame.rowconfigure(5, weight=2)
    ttk.Label(frame).grid(row=5, column=0, columnspan=3)

    # Add invisible column to the left
    frame.columnconfigure(0, weight=1)

    # Add invisible column to the right
    frame.columnconfigure(2, weight=1)

    # Check if window is being close
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window, system))

    window.mainloop()
