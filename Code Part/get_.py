"""Get the class object data given it unique id"""


def customer_data(system, id):
    customer_name = None
    customer_phone_num = None
    customer_chosen_vehicle = None
    for customer in system.get_list("customer"):
        if customer.get_id() == id:
            customer_name = customer.get_name()
            customer_phone_num = customer.get_phone_num()
            customer_chosen_vehicle = customer.get_chosen_vehicle()
    if customer_phone_num is not None:
        customer_phone_num_without0 = int(customer_phone_num[1:])
    else:
        customer_phone_num_without0 = None
    return customer_name, customer_phone_num_without0, customer_chosen_vehicle


def vehicle_data(system, id):
    type = None
    regis_num = None
    price = None
    for vehicle in system.get_list("vehicle"):
        if vehicle.get_id() == id:
            type = vehicle.get_type()
            regis_num = vehicle.get_regis_num()
            price = vehicle.get_price()
    if price is not None:
        price_int = int(price)
    else:
        price_int = None
    return type, regis_num, price_int


def driver_data(system, id):
    driver_name = None
    driver_phone_num = None
    driver_vehicle_id = None
    driver_salary = None
    driver_gender = None
    driver_age = None
    for driver in system.get_list("driver"):
        if driver.get_id() == id:
            driver_name = driver.get_name()
            driver_phone_num = driver.get_phone_num()
            driver_vehicle_id = driver.get_vehicle_id()
            driver_salary = driver.get_salary()
            driver_gender = driver.get_gender()
            driver_age = driver.get_age()
    if driver_phone_num is not None:
        driver_phone_num_without0 = int(driver_phone_num[1:])
    else:
        driver_phone_num_without0 = None
    return driver_name, driver_phone_num_without0, driver_vehicle_id, driver_salary, driver_gender, driver_age
