from Model import Customer

import openpyxl

""" Access database """
"""" Take user input """
 # user input
"""1. tkinter take user input
    2. regular expression check input
    3. write to database excel"""
# database input
data = openpyxl.load_workbook("Taxi-information.xlsx", read_only=True)

def take_customer_info():
    sheet1 = data['Customer']
    customer_list = []
    for row in sheet1:
        new_customer = Customer.Customer()
        new_customer.set_customer(row[1], row[2], row[3])
        customer_list.append(new_customer)


def take_vehicle_info():


def take_driver_info():

def take_invoice_info():

def take_feedback_info():