import re


def is_valid_phone_number(phone_number):
    pattern = r"^\d{10,11}$"
    return bool(re.match(pattern, phone_number))


def is_valid_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    return bool(re.match(pattern, name))


def is_valid_date(date):
    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})$"
    return bool(re.match(pattern, date))


def is_valid_rating(rate):
    pattern = r"^[1-5]%"
    return bool(re.match(pattern, rate))


def is_valid_payment_mode(payment_mode):
    pattern = r"^(cash|banking)$"
    return bool(re.match(pattern, payment_mode))


def is_valid_distance(distance):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, distance))


def is_valid_total_fee(total_fee):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, total_fee))


def is_valid_regis_num(regis_num):
    pattern = r"^(29|30|31)[A-Z]\d\s\d{4,5}$"
    return bool(re.match(pattern, regis_num))


def is_valid_price(price):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, price))
    # this is price from Vehicle and price_per_km from Invoice


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
    pattern = r"^V\d+$"
    return bool(re.match(pattern, vehicle_id))


def is_valid_feedback_id(feedback_id):
    pattern = r"^F\d+$"
    return bool(re.match(pattern, feedback_id))


def is_valid_invoice_id(invoice_id):
    pattern = r"^I\d+$"
    return bool(re.match(pattern, invoice_id))


def is_valid_vehicle_type(vehicle_type):
    pattern = r"^[579]S$"
    return bool(re.match(pattern, vehicle_type))
