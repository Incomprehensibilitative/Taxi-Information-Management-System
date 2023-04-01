import re
import database_reader as dr

def is_valid_phone_number(phone_number):
    pattern = r"^\d{10,11}$"
    return bool(re.match(pattern, phone_number))


def is_valid_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    return bool(re.match(pattern, name))


def is_valid_date(date):
    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})$"
    return bool(re.match(pattern, date))


def is_valid_payment_mode(payment_mode):
    pattern = r"^(cash|banking)$"
    return bool(re.match(pattern, payment_mode))


def is_valid_regis_num(regis_num):
    pattern = r"^(29|30|31)-[A-Z]\d\s\d{3}(\.\d{2}|\d{1,2})$"
    return bool(re.match(pattern, regis_num))


def is_valid_salary(salary):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, salary))


def is_valid_age(age):
    pattern = r"^\d+$"
    return bool(re.match(pattern, age))


def is_valid_gender(gender):
    pattern = r"^(Male|Female|Other)$"
    return bool(re.match(pattern, gender))


def is_valid_customer_id(customer_id):
    pattern = r"^C\d+$"
    return bool(re.match(pattern, customer_id))


def is_valid_driver_id(driver_id):
    pattern = r"^D\d+$"
    return bool(re.match(pattern, driver_id))


def is_valid_vehicle_id(vehicle_id):
    pattern = r"[579]S\d{3}"
    return bool(re.match(pattern, vehicle_id))


def is_valid_invoice_id(invoice_id):
    pattern = r"^I\d+$"
    return bool(re.match(pattern, invoice_id))


def is_valid_vehicle_type(vehicle_type):
    pattern = r"^[579]S$"
    return bool(re.match(pattern, vehicle_type))

def exist_vehicle_id(id):
# check existence
    driver_list = dr.take_driver_info()
    vehicle_list = dr.take_vehicle_info()
    driver_vehicle_id_list = []
    vehicle_id_list = []
    # Check in driver whether the vehicle already belongs to other driver
    for driver in driver_list:
        driver_vehicle_id_list.append(driver.get_vehicle_id())
    for vehicle in vehicle_list:
        vehicle_id_list.append(vehicle.get_id())
    if id not in vehicle_id_list:
        return 0
    if id in driver_vehicle_id_list:
        return 1