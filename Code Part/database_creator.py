"""This help create basic data that need to be assigned by the system
Included Random function"""
import random
import datetime


def create_date():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.datetime.now().date()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    date = str(random_date)
    return date

def create_unassign_vehicle_list(system):
    vehicle_id_list = []

    for vehicle in system.get_list("vehicle"):
        if vehicle.get_assigned() == "false":
            vehicle_id_list.append(vehicle.get_id())

    return vehicle_id_list


def create_price(vehicle_type):
    if vehicle_type == "5S":
        return "10000"
    elif vehicle_type == "7S":
        return "13000"
    elif vehicle_type == "9S":
        return "15000"


def create_customer_id(system):
    # Creat customer id
    sub_part = f"{random.randint(0, 999)}"
    if len(sub_part) == 1:
        sub_part = "00" + sub_part
    elif len(sub_part) == 2:
        sub_part = "0" + sub_part
    customer_id = "C" + sub_part

    # Check if the customer id is already existed
    customer_id_list = []
    for customer in system.get_list("customer"):
        customer_id_list.append(customer.get_id())
    while customer_id in customer_id_list:
        sub_part = f"{random.randint(0, 999)}"
        if len(sub_part) == 1:
            sub_part = "00" + sub_part
        elif len(sub_part) == 2:
            sub_part = "0" + sub_part
        customer_id = "C" + sub_part
    return customer_id


def create_vehicle_id(system, type):
    # Create vehicle id
    sub_part = f"{random.randint(0, 999)}"
    if len(sub_part) == 1:
        sub_part = "00" + sub_part
    elif len(sub_part) == 2:
        sub_part = "0" + sub_part
    vehicle_id = type + sub_part
    vehicle_id_list = []

    # Check if the vehicle id is already existed
    for vehicle in system.get_list("vehicle"):
        vehicle_id_list.append(vehicle.get_id())
    while vehicle_id in vehicle_id_list:
        sub_part = f"{random.randint(0, 999)}"
        if len(sub_part) == 1:
            sub_part = "00" + sub_part
        elif len(sub_part) == 2:
            sub_part = "0" + sub_part
        vehicle_id = type + sub_part
    return vehicle_id


def create_driver_id(system):
    # Create driver id
    sub_part = f"{random.randint(0, 999)}"
    if len(sub_part) == 1:
        sub_part = "00" + sub_part
    elif len(sub_part) == 2:
        sub_part = "0" + sub_part
    driver_id = "D" + sub_part

    # Check if the driver id is already existed
    while driver_id in system.get_list("driver"):
        sub_part = f"{random.randint(0, 999)}"
        if len(sub_part) == 1:
            sub_part = "00" + sub_part
        elif len(sub_part) == 2:
            sub_part = "0" + sub_part
        driver_id = "D" + sub_part
    return driver_id


def create_invoice_id(system):
    # Create invoice id
    sub_part = f"{random.randint(0, 999)}"
    if len(sub_part) == 1:
        sub_part = "00" + sub_part
    elif len(sub_part) == 2:
        sub_part = "0" + sub_part
    invoice_id = "I" + sub_part

    # Check if the invoice id is already existed
    while invoice_id in system.get_list("invoice"):
        sub_part = f"{random.randint(0, 999)}"
        if len(sub_part) == 1:
            sub_part = "00" + sub_part
        elif len(sub_part) == 2:
            sub_part = "0" + sub_part
        invoice_id = "I" + sub_part
    return invoice_id


def create_phone_num():
    sub_part = random.randint(10000000, 99999999)
    phone_num = "09" + str(sub_part)
    return phone_num
