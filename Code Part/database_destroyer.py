"""Delete function:
Search for ID in sheet and delete whole row"""

import openpyxl

import database_reader as dr

data = openpyxl.load_workbook("Taxi-information.xlsx", data_only=True)


def delete_customer(id):
    sheet = data['Customer']
    for i in range(0, len(dr.take_customer_info())):
        print(dr.take_customer_info()[i].get_id())
        if id == dr.take_customer_info()[i].get_id():
            sheet.delete_rows(i + 2)
            break
    data.save("Taxi-information.xlsx")


def delete_driver(id):
    sheet = data["Driver"]
    for i in range(len(dr.take_driver_info())):
        if id == dr.take_driver_info()[i].get_id():
            sheet.delete_rows(i + 2)
            break
    data.save("Taxi-information.xlsx")


def delete_vehicle(id):
    sheet = data["Vehicle"]
    for i in range(len(dr.take_vehicle_info())):
        if id == dr.take_vehicle_info()[i].get_id():
            sheet.delete_rows(i + 2)
            break
    data.save("Taxi-information.xlsx")
