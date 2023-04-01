import database_reader as dr

"""Get the class object data given it unique id"""

def customer_data(id):
    customer_list = dr.take_customer_info()
    for customer in customer_list:
            if customer.get_id() == id:
                customer_name = customer.get_name()
                customer_phone_num = customer.get_phone_num()
    customer_phone_num_without0 = int(customer_phone_num[1:])

    return customer_name, customer_phone_num_without0 

def vehicle_data(id):
    vehicle_list = dr.take_vehicle_info()
    for vehicle in vehicle_list:
        if vehicle.get_id() == id:
            type = vehicle.get_type()
            regis_num = vehicle.get_regis_num()
            price = vehicle.get_price()
    price_int = int(price)
    return type, regis_num, price_int

def driver_data(id):
    driver_list = dr.take_driver_info()
    for driver in driver_list:
            if driver.get_id() == id:
                driver_name = driver.get_name()
                driver_phone_num = driver.get_phone_num()
                driver_vehicle_id = driver.get_vehicle_id()
                driver_salary = driver.get_salary()
                driver_gender = driver.get_gender()
                driver_age = driver.get_age()
    driver_phone_num_without0 = int(driver_phone_num[1:])
    return driver_name, driver_phone_num_without0, driver_vehicle_id, driver_salary, driver_gender, driver_age