import re


def is_valid_phone_number(phone_number):
    pattern = r"^\d{10,11}$"
    return bool(re.match(pattern, phone_number))


def is_valid_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    return bool(re.match(pattern, name))


def is_valid_distance(distance):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, distance))


def is_valid_regis_num(regis_num):
    pattern = r"^(29|30|31)[A-Z]\d\s\d{4,5}$"
    return bool(re.match(pattern, regis_num))


def is_valid_salary(salary):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, salary))


def is_valid_age(age):
    pattern = r"^\d+$"
    return bool(re.match(pattern, age))

