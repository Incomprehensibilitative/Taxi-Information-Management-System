import re


def is_valid_phone_number(phone_number):
    pattern = r"^\d{10,11}$"
    return bool(re.match(pattern, phone_number))


def is_valid_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    return bool(re.match(pattern, name))


def is_valid_regis_num(regis_num):
    pattern = r"^(29|30|31)-[A-Z]\d\s\d{3}(\.\d{2}|\d{1,2})$"
    return bool(re.match(pattern, regis_num))


def is_valid_gender(gender):
    pattern = r"^(Male|Female|Other)$"
    return bool(re.match(pattern, gender))


def is_valid_vehicle_id(vehicle_id):
    if vehicle_id == "None":
        return True
    pattern = r"[579]S\d{3}"
    return bool(re.match(pattern, vehicle_id))


def is_valid_vehicle_type(vehicle_type):
    pattern = r"^[579]S$"
    return bool(re.match(pattern, vehicle_type))

def is_valid_age(age):
    # must be a number and greater than 18
    pattern = r"^([1-9]\d|[8-9]\d{2,})$"
    return bool(re.match(pattern, age))

def is_valid_age(age):
    # must be a number and greater than 18
    pattern = r"^([1-9]\d|[8-9]\d{2,})$"
    return bool(re.match(pattern, age))


def exist_vehicle_id(system, id):
    # check existence
    driver_vehicle_id_list = []
    vehicle_id_list = []
    # Check in driver whether the vehicle already belongs to other driver
    for driver in system.get_list("driver"):
        driver_vehicle_id_list.append(driver.get_vehicle_id())
    for vehicle in system.get_list("vehicle"):
        vehicle_id_list.append(vehicle.get_id())
    if id == "None":
        return 3
    if id not in vehicle_id_list:
        return 0
    if id in driver_vehicle_id_list:
        return 1
    for driver in system.get_list("driver"):
        if driver.get_vehicle_id() == id:
            return 2
