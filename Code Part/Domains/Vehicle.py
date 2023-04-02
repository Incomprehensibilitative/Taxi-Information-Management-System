"""" A generic vehicle for transportation
- id: unique id
- type: 5S, 7S, 9S (the number of seats including the driver)
- regis_num : '(29)[A-Z] [0-999].[0-99]'
- price: how much a vehicle charge per km
"""


class Vehicle:
    def __init__(self):
        self.__id = None
        self.__type = None
        self.__regis_num = None
        self.__price = None

    def set_vehicle(self, id, type, regis_num, price):
        self.__id = id
        self.__type = type
        self.__regis_num = regis_num
        self.__price = price

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_regis_num(self):
        return self.__regis_num

    def get_price(self):
        return self.__price
