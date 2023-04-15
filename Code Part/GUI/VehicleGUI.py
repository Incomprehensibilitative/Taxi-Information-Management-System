import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from Control import validation, get_
from Control import database_creator as dc

# Placeholder Function: Allow sample input to be shown
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')


# Vehicle window
def vehicle(window, system):
    # ============== Main functions ============== #
    def load_data():
        head = ("id", "type", "regis_num", "price")
        for heading_name in head:
            treeview.heading(heading_name, text=heading_name)

        for vehicle in system.get_list("vehicle"):
            treeview.insert('', tk.END,
                            values=(vehicle.get_id(), vehicle.get_type(), vehicle.get_regis_num(), vehicle.get_price()))

    def delete_vehicle_data():
        id = id_entry.get()
        try: 
            type, regis_num, price = get_.vehicle_data(system, id)
        except UnboundLocalError:
            tkinter.messagebox.showwarning(title="Error", message="Doesn't exist", parent=vehicle_window)
        else:
        # delete from system
            system.delete_object("vehicle", id)
            # delete from driver_vehicle_id
            for driver in system.get_list("driver"):
                if driver.get_vehicle_id() == id:
                    driver.set_vehicle_id("None")
            
            # delete from treeview
            for row in treeview.get_children():
                if treeview.item(row) == {'text': '', 'image': '', 'values': [id, type, regis_num, price], 'open': 0,
                                        'tags': ''}:
                    treeview.delete(row)

    def enter_vehicle_data():
        type = type_combobox.get()
        regis_num = regis_num_entry.get()
        if not validation.is_valid_vehicle_type(type):
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type", parent=vehicle_window)
        elif not validation.is_valid_regis_num(regis_num) or regis_num == "Enter regis number":
            tkinter.messagebox.showwarning(title="Error", message="Invalid regis number", parent=vehicle_window)
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
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type", parent=vehicle_window)
        elif not validation.is_valid_regis_num(regis_num) or regis_num == "29-A# ###.##":
            tkinter.messagebox.showwarning(title="Error", message="Invalid regis number", parent=vehicle_window)
        else:
            selected = treeview.focus()
            values = treeview.item(selected, 'values')
            # doesn't allow user to change the vehicle type if the id is assigned to a driver
            for driver in system.get_list("driver"):
                if driver.get_vehicle_id() == values[0]:
                    tkinter.messagebox.showwarning(title="Error", message="Vehicle ID is assigned to a driver, can't change it type",
                                                   parent=vehicle_window)
                    type_combobox.delete(0, "end")
                    regis_num_entry.delete(0, "end")
                    return
            
            if type != values[1]:
                # create new vehicle id and it price
                new_vehicle_id = dc.create_vehicle_id(system, type)
                new_price = dc.create_price(type)
                old_vehicle_id = values[0]                
                # update vehicle id
                updated_data1 = [new_vehicle_id, type, regis_num, new_price, old_vehicle_id]
                system.update_vehicle(updated_data1)
                treeview.item(selected, text="", values=(new_vehicle_id, type, regis_num, new_price))
                
                # reset input boxes
                type_combobox.delete(0, "end")
                regis_num_entry.delete(0, "end")
            else:
                updated_data2 = [values[0], values[1], regis_num, values[3], values[0]]
                system.update_vehicle(updated_data2)
                treeview.item(selected, text="", values=(values[0], values[1], regis_num, values[3]))
                type_combobox.delete(0, "end")
                regis_num_entry.delete(0, "end")

    def clear_vehicle_data():
        type_combobox.configure(state='normal')
        regis_num_entry.configure(state='normal')

        type_combobox.delete(0, "end")
        regis_num_entry.delete(0, "end")
        
    def search_vehicle_data():
        items_on_treeview = treeview.get_children()
        search_regis_num = search_ent_var.get()
        for item in items_on_treeview:
            if search_regis_num in (treeview.item(item)['values'][2]):
                treeview.move(item, '', 0)
                treeview.selection_set(item)
                

    # ============== Main window and Frames  ============== #
    # Main window
    vehicle_window = tk.Toplevel(window)
    vehicle_window.title("Vehicle Admin")

    # Main frame
    vehicle_frame = tk.Frame(vehicle_window)
    vehicle_frame.pack()

    # Frame for adding and modifying information
    vehicle_info_frame = tk.LabelFrame(vehicle_frame, text="Vehicle info")
    vehicle_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Frame for deleting the data
    delete_vehicle_info_frame = tk.LabelFrame(vehicle_frame, text="Delete Vehicle")
    delete_vehicle_info_frame.grid(row=1, column=0, pady=10)
    
    # Frame for searching the data
    search_vehicle_info_frame = tk.LabelFrame(vehicle_frame, text="Search Vehicle by Regis Number")
    search_vehicle_info_frame.grid(row=1, column=1, pady=10)

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
    regis_num_entry.insert(0, "29-A# ###.##")
    regis_num_entry.configure(state='disabled')
    regis_num_entry.grid(row=1, column=0)

    # price
    price_label = tk.Label(vehicle_info_frame, text="Price")
    price_label.grid(row=0, column=2)
    price_info_label = tk.Label(vehicle_info_frame, text="5S - 10,000\n7S - 13,000\n9S - 15,000")
    price_info_label.grid(row=1, column=2)

    # Id
    id_label = tk.Label(delete_vehicle_info_frame, text="Vehicle ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_vehicle_info_frame)
    id_entry.insert(0, "#S###")
    id_entry.configure(state='disabled')
    id_entry.grid(row=1, column=0)
    
    # Search regis number
    search_label = tk.Label(search_vehicle_info_frame, text="Search")
    search_label.grid(row=0, column=0)
    search_ent_var = tk.Variable()
    search_entry = tk.Entry(search_vehicle_info_frame, textvariable=search_ent_var)
    search_entry.grid(row=1, column=0)
    search_ent_var.trace("w", lambda name, index, mode, sv=search_ent_var: search_vehicle_data())

    # ============== Modification Buttons ============== #
    # Add button
    button = ttk.Button(vehicle_info_frame, text="Enter data", command=enter_vehicle_data, style="Accent.TButton")
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Select button
    select_button = ttk.Button(vehicle_info_frame, text="Select data", command=select_vehicle_data, style="Accent.TButton")
    select_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    # Update button
    update_button = ttk.Button(vehicle_info_frame, text="Update data", command=update_vehicle_data, style="Accent.TButton")
    update_button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

    # Clear button
    clear_button = ttk.Button(vehicle_info_frame, text="Clear data", command=clear_vehicle_data, style="Accent.TButton")
    clear_button.grid(row=3, column=2, sticky="news", padx=20, pady=10)

    # Delete button
    delete_button = ttk.Button(delete_vehicle_info_frame, text="Delete data", command=delete_vehicle_data, style="Accent.TButton")
    delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)
    
    # ============== Others ============== #
    # Regridding widgets
    for widget in vehicle_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    for widget in search_vehicle_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Disable placeholder
    regis_num_entry.bind('<Button-1>', lambda x: on_focus_in(regis_num_entry))
    regis_num_entry.bind('<FocusOut>', lambda x: on_focus_out(regis_num_entry, '29-A# ###.##'))

    id_entry.bind('<Button-1>', lambda x: on_focus_in(id_entry))
    id_entry.bind('<FocusOut>', lambda x: on_focus_out(id_entry, '#S###'))

    # ============== Treeview ============== #
    treeFrame = ttk.Frame(vehicle_frame)
    treeFrame.grid(row=0, column=1, pady=10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")
    cols = ("id", "type", "regis_num", "price")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=70)
    treeview.column("type", width=50)
    treeview.column("regis_num", width=120)
    treeview.column("price", width=80)
    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()

    vehicle_window.mainloop()
