"""This help create basic data that need to be assigned by the system
Included Random function"""
import random
import datetime
import database_reader as dr


def create_date():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.datetime.now().date()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def create_price(vehicle_type):
    vehicle_type
    if vehicle_type == "5S":
        return "10000"
    elif vehicle_type == "7S":
        return "13000"
    elif vehicle_type == "9S":
        return "15000"

def create_customer_id():
    customer_id = f"C{random.randint(0, 999)}"
    customer_list = dr.take_customer_info()
    customer_id_list = []
    for customer in customer_list:
        customer_id_list.append(customer.get_id())
    while customer_id in customer_id_list:
        customer_id = f"C{random.randint(0, 999)}"
    return customer_id

def create_vehicle_id(type):
    vehicle_id = f"{type}{random.randint(0,999)}"
    vehicle_list = dr.take_vehicle_info()
    vehicle_id_list = []
    for vehicle in vehicle_list:
        vehicle_id_list.append(vehicle.get_id())
    while vehicle_id in vehicle_id_list:
        vehicle_id = f"{type}{random.randint(0, 999)}"
    return vehicle_id

def create_driver_id():
    driver_id = f"D{random.randint(0, 999)}"
    driver_list = dr.take_driver_info()
    driver_id_list = []
    for driver in driver_list:
        driver_id_list.append(driver.get_id())
    while driver_id in driver_id_list:
        driver_id = f"D{random.randint(0, 999)}"
    return driver_id

