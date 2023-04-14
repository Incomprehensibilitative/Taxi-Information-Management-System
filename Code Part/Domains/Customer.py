"""" A generic customer 
- id: unique id
- name: customer name
- phone_num: customer phone number
"""


class Customer:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__phone_num = None
        self.__chosen_vehicle = None
        self.__pick_up_spot = None

    def set_customer(self, id, name, phone_num, type, pick_up_spot):
        self.__id = id
        self.__name = name
        self.__phone_num = phone_num
        self.__chosen_vehicle = type
        self.__pick_up_spot = pick_up_spot

    def get_pick_up_spot(self):
        return self.__pick_up_spot

    def get_chosen_vehicle(self):
        return self.__chosen_vehicle

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone_num(self):
        return self.__phone_num
