"""Use to manage all the changes into a list of objects
After the software is terminated write all the changes to the database"""

import database_reader as dr

class Management:
    def __init__(self):
        self.__customer_list = dr.take_customer_info()
        self.__driver_list = dr.take_driver_info()
        self.__vehicle_list = dr.take_vehicle_info()
        self.__invoice_list = dr.take_invoice_info()
    
    # add new object/ data to the list of choice
    def add_new(self, list, obj):
        if list == "customer":
            self.__customer_list.append(obj)
        if list == "driver":
            self.__driver_list.append(obj)
        if list == "vehicle":
            self.__vehicle_list.append(obj)
        if list == "invoice":
            self.__invoice_list.append(obj)
        else:
            print("Error")
