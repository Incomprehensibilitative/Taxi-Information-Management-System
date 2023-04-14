"""Use to manage all the changes into a list of objects
After the software is terminated write all the changes to the database"""

import database_reader as dr
from Domains import Customer, Vehicle, Driver, Invoice


class Management:
    def __init__(self):
        self.__customer_list = dr.take_customer_info()
        self.__driver_list = dr.take_driver_info()
        self.__vehicle_list = dr.take_vehicle_info()
        self.__invoice_list = dr.take_invoice_info()

    # add new object/ data to the list of choice
    def get_list(self, list_name):
        if list_name == "customer":
            return self.__customer_list
        if list_name == "driver":
            return self.__driver_list
        if list_name == "vehicle":
            return self.__vehicle_list
        if list_name == "invoice":
            return self.__invoice_list
        else:
            print("Error")

    def set_new_customer(self, values):
        new_customer = Customer.Customer()
        new_customer.set_customer(values[0], values[1], values[2], values[3], values[4])
        self.__customer_list.append(new_customer)


    def set_new_driver(self, values):
        new_driver = Driver.Driver()
        new_driver.set_driver(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
        self.__driver_list.append(new_driver)


    def set_new_vehicle(self, values):
        new_vehicle = Vehicle.Vehicle()
        new_vehicle.set_vehicle(values[0],values[1],values[2],values[3], values[4])
        self.__vehicle_list.append(new_vehicle)


    def set_new_invoice(self, values):
        new_invoice = Invoice.Invoice()
        new_invoice.set_invoice(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])
        self.__invoice_list.append(new_invoice)


    def delete_object(self, list_name, obj_id):
        obj_list = self.get_list(list_name)
        for obj in obj_list:
            if obj.get_id() == obj_id:
                obj_list.remove(obj)
                break

    def update_customer(self, values):
        for i, customer in enumerate(self.get_list("customer"), 0):
            if customer.get_id() == values[0]:
                self.delete_object("customer", values[0])
                updated_customer = Customer.Customer()
                updated_customer.set_customer(values[0], values[1], values[2], values[3], values[4])
                self.get_list("customer").insert(i, updated_customer)
                break

    def update_driver(self, values):
        for i, driver in enumerate(self.get_list("driver"), 0):
            if driver.get_id() == values[0]:
                self.delete_object("driver", values[0])
                updated_driver = Driver.Driver()
                updated_driver.set_driver(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
                self.get_list("driver").insert(i, updated_driver)
                break

    def update_vehicle(self, values):
        for i, vehicle in enumerate(self.get_list("vehicle"), 0):
            if vehicle.get_id() == values[4]:
                self.delete_object("vehicle", values[4])
                updated_vehicle = Vehicle.Vehicle()
                updated_vehicle.set_vehicle(values[0], values[1], values[2], values[3])
                self.get_list("vehicle").insert(i, updated_vehicle)
                break
