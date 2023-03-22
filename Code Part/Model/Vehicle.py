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

    def get_regis(self):
        return self.__regis_num

    def get_price(self):
        return self.__price

