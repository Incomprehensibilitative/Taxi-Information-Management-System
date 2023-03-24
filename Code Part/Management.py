from Model import *
import input

class Management:
    def __init__(self):
        # To keep track of the number of object
        self.__number_of_drivers = 0
        self.__number_of_vehicles = 0
        self.__number_of_invoices = 0
        # To store all object that will be manage
        self.__customer_list = []
        self.__driver_list = []
        self.__feedback_list = []
        self.__invoice_list = []
        self.__vehicle_list = []

    """ Access database"""

    """ Adding new object function """
    def new_driver(self):
        # take in
        pass

    def new_vehicle(self):
        pass

    def new_customer(self):
        pass

    def new_feedback(self):
        pass

    def new_invoice(self):
        # During the creation of new_invoice it also call new_customer and new_driver, and optional new_feedback
        pass

