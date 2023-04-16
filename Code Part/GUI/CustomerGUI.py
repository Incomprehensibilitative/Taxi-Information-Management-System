import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from Control import database_creator as dc
from Control import get_, validation


# Placeholder Function: Allow sample input to be shown
def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal')
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')

""" New administration windows """


# Customer window
def customer(window, system):
    def load_data():
        # define heading for the treeview
        head = ("id", "name", "phone_num", "chosen_vehicle", "pick_up_spot")
        for heading_name in head:
            treeview.heading(heading_name, text=heading_name)
        # append customer data from customer list into treeview
        for customer in system.get_list("customer"):
            treeview.insert('', tk.END, values=(
                customer.get_id(), customer.get_name(), customer.get_phone_num(), customer.get_chosen_vehicle(), customer.get_pick_up_spot()))

    def delete_customer_data():
        id = id_entry.get()
        customer_name, customer_phone_num, customer_chosen_vehicle, customer_pick_up_spot = get_.customer_data(system, id)
        system.delete_object("customer", id)
        for row in treeview.get_children():
            if treeview.item(row) == {'text': '', 'image': '',
                                      'values': [id, customer_name, customer_phone_num, customer_chosen_vehicle, customer_pick_up_spot],
                                      'open': 0, 'tags': ''}:
                treeview.delete(row)
        id_entry.delete(0, "end")

    def enter_customer_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        chosen_vehicle = chosen_vehicle_combobox.get()
        pick_up_spot = pick_up_spot_entry.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name", parent=window)
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number", parent=window)
        elif not validation.is_valid_vehicle_type(chosen_vehicle):
            tkinter.messagebox.showwarning(title="Error", message="Invalid vehicle type", parent=window)
        else:

            customer_id = dc.create_customer_id(system)
            row_values = [customer_id, name, phone_num, chosen_vehicle, pick_up_spot]
            system.set_new_customer(row_values)

            treeview.insert('', tk.END, value=row_values)
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            chosen_vehicle_combobox.delete(0, "end")
            pick_up_spot_entry.delete(0, "end")

    def select_customer_data():
        # Disable placeholder
        name_entry.configure(state='normal')
        phone_num_entry.configure(state='normal')
        chosen_vehicle_combobox.configure(state='normal')

        # Clear entry boxes
        name_entry.delete(0, "end")
        phone_num_entry.delete(0, "end")
        chosen_vehicle_combobox.delete(0, "end")
        pick_up_spot_entry.delete(0, "end")

        # Grab row to update
        selected = treeview.focus()

        # Grab data
        values = treeview.item(selected, 'values')

        # Output to boxes
        name_entry.insert(0, values[1])
        phone_num_entry.insert(0, values[2])
        chosen_vehicle_combobox.insert(0, values[3])
        pick_up_spot_entry.insert(0, values[4])
        # chosen_vehicle_combobox.configure(state='disabled')

    def update_customer_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        chosen_vehicle = chosen_vehicle_combobox.get()
        pick_up_spot = pick_up_spot_entry.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name", parent=window,
                                           icon="warning")
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number", parent=window)
        else:
            # To get the id, not other values
            selected = treeview.focus()
            values = treeview.item(selected, 'values')
            # Since the values[0] == id, so we want to keep it, and change other data
            updated_data = [values[0], name, phone_num, chosen_vehicle, pick_up_spot]
            system.update_customer(updated_data)
            treeview.item(selected, text="", values=(values[0], name, phone_num, chosen_vehicle, pick_up_spot))
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            chosen_vehicle_combobox.delete(0, "end")
            pick_up_spot_entry.delete(0, "end")

    def clear_customer_data():
        name_entry.delete(0, "end")
        phone_num_entry.delete(0, "end")
        chosen_vehicle_combobox.delete(0, "end")
        pick_up_spot_entry.delete(0, "end")
        
    def search_customer_data():
        search_by = search_by_combobox.get()
        if search_by == "":
            tkinter.messagebox.showwarning(title="Error", message="Please select a search option", parent=window)
            search_ent_var.set("")
        else:
            items_on_treeview = treeview.get_children()
            search_phone_num = search_ent_var.get()
            if search_by == "Phone Number":
                for item in items_on_treeview:
                    if search_phone_num in str("0" + str(treeview.item(item)['values'][2])):
                        # Put the search result on the top of the treeview and hightlight it
                            treeview.move(item, '', 0)
                            treeview.selection_set(item)
            if search_by == "Name":
                for item in items_on_treeview:
                    if search_phone_num in str(treeview.item(item)['values'][1]):
                        # Put the search result on the top of the treeview and hightlight it
                            treeview.move(item, '', 0)
                            treeview.selection_set(item)
                

    # ============== Main window and Frames  ============== #
    # Main frame
    # check if a frame already exists in the window grid in position 0,1 (row 0, column 1) and destroy it
    if len(window.grid_slaves(row=0, column=1)) > 0:
        window.grid_slaves(row=0, column=1)[0].destroy()

    # Main frame
    customer_frame = ttk.Frame(window)
    customer_frame.grid(row=0, column=1, padx=20, pady=10)

    # Frame for adding and modifying information
    user_info_frame = tk.LabelFrame(customer_frame, text="Customer Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Frame for deleting the data
    delete_user_info_frame = tk.LabelFrame(customer_frame, text="Delete Customer")
    delete_user_info_frame.grid(row=1, column=0, pady=10)
    
    # Frame for searching the data
    search_user_info_frame = tk.LabelFrame(customer_frame, text="Search Customer by Phone Number")
    search_user_info_frame.grid(row=1, column=1, pady=10)
    
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

    # Chosen vehicle
    type_list = ["5S", "7S", "9S"]
    chosen_vehicle_label = tk.Label(user_info_frame, text="Type")
    chosen_vehicle_label.grid(row=0, column=2)
    chosen_vehicle_combobox = ttk.Combobox(user_info_frame, values=type_list)
    chosen_vehicle_combobox.grid(row=1, column=2)

    # Pick_up_spot
    pick_up_spot_label = tk.Label(user_info_frame, text="Pick up spot")
    pick_up_spot_label.grid(row=0, column=3)
    pick_up_spot_entry = tk.Entry(user_info_frame)
    pick_up_spot_entry.grid(row=1, column=3)

    # Id
    id_label = tk.Label(delete_user_info_frame, text="Customer ID")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_user_info_frame)
    id_entry.insert(0, "C#")
    id_entry.configure(state='disabled')
    id_entry.grid(row=1, column=0)
    
    # Search by
    search_by_combo_list = ["Phone Number", "Name"]
    search_by_label = tk.Label(search_user_info_frame, text="Search by")
    search_by_label.grid(row=0, column=0)
    search_by_combobox = ttk.Combobox(search_user_info_frame, values=search_by_combo_list)
    search_by_combobox.grid(row=1, column=0)
    
    
    # Search phone number
    search_label = tk.Label(search_user_info_frame, text="Search")
    search_label.grid(row=0, column=1)
    search_ent_var = tk.Variable()
    search_entry = tk.Entry(search_user_info_frame, textvariable=search_ent_var)
    search_entry.grid(row=1, column=1)
    search_ent_var.trace("w", lambda name, index, mode, sv=search_ent_var: search_customer_data())
    

    # ============== Modification Buttons ============== #
    # Add Button
    add_button = ttk.Button(user_info_frame, text="Enter data", command=enter_customer_data, style="Accent.TButton")
    add_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    # Select button
    select_button = ttk.Button(user_info_frame, text="Select data", command=select_customer_data, style="Accent.TButton")
    select_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    # Update button
    update_button = ttk.Button(user_info_frame, text="Update data", command=update_customer_data, style="Accent.TButton")
    update_button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

    # Clear button
    clear_button = ttk.Button(user_info_frame, text="Clear data", command=clear_customer_data, style="Accent.TButton")
    clear_button.grid(row=3, column=2, sticky="news", padx=20, pady=10)

    # Delete button
    delete_button = ttk.Button(delete_user_info_frame, text="Delete data", command=delete_customer_data, style="Accent.TButton")
    delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)

    # Regridding widgets
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    for widget in search_user_info_frame.winfo_children():
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
    cols = ("id", "name", "phone_num", "chosen_vehicle", "pick_up_spot")
    treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=13)
    treeview.column("id", width=70)
    treeview.column("name", width=150)
    treeview.column("phone_num", width=150)
    treeview.column("chosen_vehicle", width=150)
    treeview.column("pick_up_spot", width=250)
    treeview.pack()
    treeScroll.config(command=treeview.yview())
    load_data()

