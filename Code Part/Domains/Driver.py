""""A generic Driver
- id: unique id
- name, gender, age, phone, salary: belong to the driver
- vehicle_id: each driver is assigned with a specific vehicle
"""


class Driver:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__phone_num = None
        self.__vehicle_id = None
        self.__salary = None
        self.__gender = None
        self.__age = None

    def set_driver(self, id, name, phone, vehicle_id, salary, gender, age):
        self.__id = id
        self.__name = name
        self.__phone_num = phone
        self.__vehicle_id = vehicle_id
        self.__salary = salary
        self.__gender = gender
        self.__age = age

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone_num(self):
        return self.__phone_num

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_salary(self):
        return self.__salary

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age
