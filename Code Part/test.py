import openpyxl
import datetime
import random

from Domains import Customer, Vehicle, Driver, Invoice
import database_reader as dr
import database_destroyer as dd



# sheet = data['Customer']
# customer_list = []
# for row in sheet.iter_rows(min_row = 2):
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

# for i in range(10):
#     print(dr.take_customer_info()[i].get_id())

start_date = datetime.date(2022, 1, 1)
end_date = datetime.datetime.now().date()

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)

print(random_date)