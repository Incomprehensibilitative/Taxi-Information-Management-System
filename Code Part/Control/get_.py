"""Get the class object data given it unique id"""

def customer_data(system, id):
    for customer in system.get_list("customer"):
        if customer.get_id() == id:
            customer_name = customer.get_name()
            customer_phone_num = customer.get_phone_num()
            customer_chosen_vehicle = customer.get_chosen_vehicle()
            customer_pick_up_spot = customer.get_pick_up_spot()
    customer_phone_num_without0 = int(customer_phone_num[1:])
    return customer_name, customer_phone_num_without0, customer_chosen_vehicle, customer_pick_up_spot

def vehicle_data(system, id):
    for vehicle in system.get_list("vehicle"):
        if vehicle.get_id() == id:
            type = vehicle.get_type()
            regis_num = vehicle.get_regis_num()
            price = vehicle.get_price()
            assign = vehicle.get_assigned()
    price_int = int(price)
    return type, regis_num, price_int, assign

def vehicle_assignment(system, id, task):
    for vehicle in system.get_list("vehicle"):
        if vehicle.get_id() == id:
            if task == "assign":
                vehicle.set_assigned("true")
            elif task == "unassign":
                vehicle.set_assigned("false")

def driver_data(system, id):
    driver_name = driver_phone_num = driver_vehicle_id = driver_gender = driver_age = ""
    driver_phone_num_withoutO = driver_salary = 0
    for driver in system.get_list("driver"):
        if driver.get_id() == id:
            driver_name = driver.get_name()
            driver_phone_num = driver.get_phone_num()
            driver_vehicle_id = driver.get_vehicle_id()
            driver_salary = int(driver.get_salary())
            driver_gender = driver.get_gender()
            driver_age = int(driver.get_age())
            driver_phone_num_withoutO = int(driver_phone_num[1:])
    return driver_name, driver_phone_num_withoutO, driver_vehicle_id, driver_salary, driver_gender, driver_age

def driver_id_list(system):
    id_list = []
    for driver in system.get_list("driver"):
        id_list.append(driver.get_id())
    return id_list