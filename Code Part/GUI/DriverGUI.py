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


# Driver window
def driver(window, system):
    def load_data():
        head_driver = ("id", "name", "phone_num", "vehicle_id", "salary", "gender", "age")
        for heading_name in head_driver:
            treeview.heading(heading_name, text=heading_name)
        for driver in system.get_list("driver"):
            treeview.insert('', tk.END, values=(
                driver.get_id(), driver.get_name(), driver.get_phone_num(), driver.get_vehicle_id(),
                driver.get_salary(),
                driver.get_gender(), driver.get_age()))

        head_vehicle = "unassign_vehicle_id"
        treeview_vehicle.heading(head_vehicle, text=head_vehicle)
        for vehicle in dc.create_unassign_vehicle_list(system):
            treeview_vehicle.insert('', tk.END, values=vehicle)

    def delete_driver_data():
        id = id_entry.get()
        if id not in get_.driver_id_list(system):
            tkinter.messagebox.showerror("Error", "Driver ID not found", parent=window)
            id_entry.delete(0, tk.END)
            return
        driver_name, driver_phone_num, driver_vehicle_id, driver_salary, driver_gender, driver_age = get_.driver_data(
            system, id)
        system.delete_object("driver", id)
        get_.vehicle_assignment(system, driver_vehicle_id, "unassign")
        for row in treeview.get_children():
            if treeview.item(row) == {'text': '', 'image': '',
                                    'values': [id, driver_name, driver_phone_num, str(driver_vehicle_id), driver_salary,
                                                driver_gender, driver_age], 'open': 0, 'tags': ''}:
                treeview.delete(row)
                if str(driver_vehicle_id) == 'None':
                    id_entry.delete(0, tk.END)
                    return
                else:
                    treeview_vehicle.insert('', tk.END, values=driver_vehicle_id)

    def enter_driver_data():
        name = name_entry.get()
        phone_num = phone_num_entry.get()
        vehicle_id = vehicle_id_entry.get()
        salary = salary_entry.get()
        gender = gender_combobox.get()
        age = age_spinbox.get()
        if not validation.is_valid_name(name) or name == "Enter name":
            tkinter.messagebox.showwarning(title="Error", message="Invalid name", parent=window)
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number", parent=window)
        elif not validation.is_valid_vehicle_id(vehicle_id) or vehicle_id == "#S###":
            # need to check whether the vehicle actually exist or available for assignment also bug
            tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle ID", parent=window)
        elif validation.exist_vehicle_id(system, vehicle_id) == 1:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle already assigned", parent=window)
        elif validation.exist_vehicle_id(system, vehicle_id) == 0:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle doesn't exist", parent=window)
        elif not validation.is_valid_gender(gender):
            tkinter.messagebox.showwarning(title="Error", message="Invalid Gender", parent=window)
        else:
            # The id need to be created by the system to make sure it's unique
            driver_id = dc.create_driver_id(system)
            # appending the value into
            get_.vehicle_assignment(system, vehicle_id, "assign")
            row_values = [driver_id, name, phone_num, vehicle_id, salary, gender, age]
            system.set_new_driver(row_values)
            
            treeview.insert('', tk.END, values=row_values)

            for row in treeview_vehicle.get_children():
                if treeview_vehicle.item(row) == {'text': '', 'image': '', 'values': [vehicle_id], 'open': 0,
                                                  'tags': ''}:
                    treeview_vehicle.delete(row)

            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            vehicle_id_entry.delete(0, "end")
            salary_entry.delete(0, "end")
            gender_combobox.delete(0, "end")
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
            tkinter.messagebox.showwarning(title="Error", message="Invalid name", parent=window)
        elif not validation.is_valid_phone_number(phone_num) or phone_num == "0### ### ###":
            tkinter.messagebox.showwarning(title="Error", message="Invalid Phone Number", parent=window)
        elif not validation.is_valid_vehicle_id(vehicle_id) or vehicle_id == "#S###":
            # need to check whether the vehicle actually exist or available for assignment also bug
            tkinter.messagebox.showwarning(title="Error", message="Invalid Vehicle ID", parent=window)
        elif validation.exist_vehicle_id(system, vehicle_id) == 2:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle already assigned", parent=window)
        elif validation.exist_vehicle_id(system, vehicle_id) == 0:
            tkinter.messagebox.showwarning(title="Error", message="Vehicle doesn't exist", parent=window)
        elif not validation.is_valid_gender(gender):
            tkinter.messagebox.showwarning(title="Error", message="Invalid Gender", parent=window)
        else:
            # To get the values[0] == id, not other values
            selected = treeview.focus()
            values = treeview.item(selected, 'values')
            if vehicle_id != values[3]:
                get_.vehicle_assignment(system, values[3], "unassign")
                get_.vehicle_assignment(system, vehicle_id, "assign")
            
            updated_data = [values[0], name, phone_num, vehicle_id, salary, gender, age]
            system.update_driver(updated_data)
            
            treeview.item(selected, text="", values=(values[0], name, phone_num, vehicle_id, salary, gender, age))

            for row in treeview_vehicle.get_children():
                if treeview_vehicle.item(row) == {'text': '', 'image': '', 'values': [vehicle_id], 'open': 0,
                                                  'tags': ''}:
                    treeview_vehicle.delete(row)
                    if values[3] == "None":
                        name_entry.delete(0, "end")
                        phone_num_entry.delete(0, "end")
                        vehicle_id_entry.delete(0, "end")
                        salary_entry.delete(0, "end")
                        gender_combobox.delete(0, "end")
                        age_spinbox.delete(0, "end")
                        return
                    else:
                        treeview_vehicle.insert('', tk.END, values=[values[3]])
                    
            name_entry.delete(0, "end")
            phone_num_entry.delete(0, "end")
            vehicle_id_entry.delete(0, "end")
            salary_entry.delete(0, "end")
            gender_combobox.delete(0, "end")
            age_spinbox.delete(0, "end")

    def clear_driver_data():
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
        
    def search_driver_data():
        items_on_treeview = treeview.get_children()
        search_phone_num = search_ent_phone_num.get()
        for item in items_on_treeview:
            if search_phone_num in str("0" + str(treeview.item(item)['values'][2])):
                # Put the search result on the top of the treeview and highight it
                    treeview.move(item, '', 0)
                    treeview.selection_set(item)

    def search_unassign_vehicle_data():
        items_on_treeview = treeview_vehicle.get_children()
        search_vehicle_id = search_ent_unassign_vehicle_id.get()
        for item in items_on_treeview:
            if search_vehicle_id in str(treeview_vehicle.item(item)['values'][0]):
                # Put the search result on the top of the treeview and highight it
                    treeview_vehicle.move(item, '', 0)
                    treeview_vehicle.selection_set(item)

    # ============== Main window and Frames  ============== #
    # check if a frame already exists in the window grid in position 0,1 (row 0, column 1) and destroy it
    if len(window.grid_slaves(row=0, column=1)) > 0:
        window.grid_slaves(row=0, column=1)[0].destroy()
        
    # Main frame
    driver_frame = ttk.Frame(window)
    driver_frame.grid(row=0, column=1, padx=20, pady=10)

    # Frame for adding and modifying information
    driver_info_frame = tk.LabelFrame(driver_frame, text="Driver info")
    driver_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Frame for deleting the data
    delete_driver_info_frame = tk.LabelFrame(driver_frame, text="Delete Driver")
    delete_driver_info_frame.grid(row=1, column=0, pady=10)

    # Frame for searching the driver phone number 
    search_driver_info_frame = tk.LabelFrame(driver_frame, text="Search Customer by Phone Number")
    search_driver_info_frame.grid(row=1, column=1, pady=10)
    
    # Frame for searching unassign vehicle
    search_unassign_vehicle_frame = tk.LabelFrame(driver_frame, text="Search Unassign Vehicle")
    search_unassign_vehicle_frame.grid(row=1, column=2, pady=10)

    # ============== Basic information ============== #
    # name
    name_label = tk.Label(driver_info_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(driver_info_frame)
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
    
    # Search phone number
    search_phone_num_label = tk.Label(search_driver_info_frame, text="Search")
    search_phone_num_label.grid(row=0, column=0)
    search_ent_phone_num = tk.Variable()
    search_phone_num_entry = tk.Entry(search_driver_info_frame, textvariable=search_ent_phone_num)
    search_phone_num_entry.grid(row=1, column=0)
    search_ent_phone_num.trace("w", lambda name, index, mode, sv=search_ent_phone_num: search_driver_data())

    # Search unassigned vehicles
    search_unassign_vehicle_id_label = tk.Label(search_unassign_vehicle_frame, text="Search")
    search_unassign_vehicle_id_label.grid(row=0, column=0)
    search_ent_unassign_vehicle_id = tk.Variable()
    search_unassign_vehicle_id_entry = tk.Entry(search_unassign_vehicle_frame, textvariable=search_ent_unassign_vehicle_id)
    search_unassign_vehicle_id_entry.grid(row=1, column=0)
    search_ent_unassign_vehicle_id.trace("w", lambda name, index, mode, sv=search_ent_unassign_vehicle_id: search_unassign_vehicle_data())

    # ============== Modification Buttons ============== #
    # Add button
    add_button = ttk.Button(driver_info_frame, text="Enter data", command=enter_driver_data, style="Accent.TButton")
    add_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    # Select button
    select_button = ttk.Button(driver_info_frame, text="Select data", command=select_driver_data, style="Accent.TButton")
    select_button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

    # Update button
    update_button = ttk.Button(driver_info_frame, text="Update data", command=update_driver_data, style="Accent.TButton")
    update_button.grid(row=5, column=1, sticky="news", padx=20, pady=10)

    # Clear button
    clear_button = ttk.Button(driver_info_frame, text="Clear data", command=clear_driver_data, style="Accent.TButton")
    clear_button.grid(row=5, column=2, sticky="news", padx=20, pady=10)

    # Delete button
    delete_button = ttk.Button(delete_driver_info_frame, text="Delete data", command=delete_driver_data, style="Accent.TButton")
    delete_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)

    # Regridding widgets
    for widget in driver_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    
    for widget in search_unassign_vehicle_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        
    for widget in search_driver_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    
    
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
    treeview.column("id", width=70)
    treeview.column("name", width=100)
    treeview.column("phone_num", width=130)
    treeview.column("vehicle_id", width=100)
    treeview.column("salary", width=110)
    treeview.column("gender", width=70)
    treeview.column("age", width=50)
    treeview.pack()
    treeScroll.config(command=treeview.yview())

    # ============== Treeview to show available vehicle ============== #
    treeFrame_vehicle = ttk.Frame(driver_frame)
    treeFrame_vehicle.grid(row=0, column=2, pady=10)
    treeScroll_vehicle = ttk.Scrollbar(treeFrame_vehicle)
    treeScroll_vehicle.pack(side="right", fill="y")
    cols_vehicle = "unassign_vehicle_id"
    treeview_vehicle = ttk.Treeview(treeFrame_vehicle, show="headings", yscrollcommand=treeScroll_vehicle.set,
                                    columns=cols_vehicle, height=13)
    treeview_vehicle.column("unassign_vehicle_id", width=155)
    treeview_vehicle.pack()
    treeScroll_vehicle.config(command=treeview_vehicle.yview())

    load_data()

