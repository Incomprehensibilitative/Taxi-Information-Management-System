import openpyxl
from Model import Customer, Vehicle, Driver, Feedback, Invoice

data = openpyxl.load_workbook("Taxi-information.xlsx", read_only=True, data_only=True)

# sheet = data['Customer']
# customer_list = []
# for row in sheet:
#     new_customer = Customer.Customer()
#     new_customer.set_customer(row[0].value, row[1].value, row[2].value)
#     customer_list.append(new_customer)
# for element in customer_list:
#     print("{:8} {:<15} {:<15}".format(element.get_id(), element.get_name(), element.get_phone_num()))

# sheet = data['Vehicle']
# vehicle_list = []
# for row in sheet:
#     new_vehicle = Vehicle.Vehicle()
#     new_vehicle.set_vehicle(row[0].value, row[1].value, row[2].value, row[3].value)
#     vehicle_list.append(new_vehicle)
# for element in vehicle_list:
#     print("{:8} {:5} {:15} {}".format(element.get_id(), element.get_type(), element.get_regis(), element.get_price()))
#
# sheet = data['Driver']
# print(sheet.max_column)
# driver_list = []
# for row in sheet:
#     new_driver = Driver.Driver()
#     new_driver.set_driver(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value, row[6].value)
#     driver_list.append(new_driver)
# for element in driver_list:
#     print("{:3} {:7} {:12} {:8} {:10} {:7} {:3}".format(element.get_id(), element.get_name(), element.get_phone(), element.get_vehicle_id(), element.get_salary(), element.get_gender(), element.get_age()))
