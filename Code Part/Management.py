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
        new_customer.set_customer(values[0], values[1], values[2])
        self.__customer_list.append(new_customer)
        print("It fuckfing works")

    def set_new_driver(self, values):
        new_driver = Driver.Driver()    
        new_driver.set_driver(values[0],values[1],values[2],values[3],values[4],values[5], values[6])
        self.__driver_list.append(new_driver)
        print("It fuckfing works")

    def set_new_vehicle(self, values):
        new_vehicle = Vehicle.Vehicle()
        new_vehicle.set_vehicle(values[0],values[1],values[2],values[3])
        self.__vehicle_list.append(new_vehicle)
        print("It fuckfing works")

    def delete_object(self, list_name, obj_id):
        obj_list = self.get_list(list_name)
        for obj in obj_list:
            if obj.get_id() == obj_id:
                obj_list.remove(obj)
                print("It fuckfing works")
                break

    def update_customer(self, values):
        for i, id in enumerate(self.get_list("customer").get_id(),0):
            if values[0] == id:
                self.delete_object("customer", values[0])
                self.get_list("customer").insert(Customer.Customer().set_customer(values[0], values[1], values[2]),i)
                break

    def update_driver(self, values):
        for i, id in enumerate(self.get_list("driver").get_id(),0):
            if values[0] == id:
                self.delete_object("driver", values[0])
                self.get_list("driver").insert(Driver.Driver().set_driver(values[0],values[1],values[2],values[3],values[4],values[5], values[6]), i)
                break

    def update_vehicle(self, values):
        for i, id in enumerate(self.get_list("vehicle").get_id(), 0):
            if values[0] == id:
                self.delete_object("vehicle", values[0])
                self.get_list("driver").insert(Vehicle.Vehicle().set_vehicle(values[0],values[1],values[2],values[3]), i)
                break

