class Customer:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__phone_num = None

    def set_customer(self, id, name, phone_num):
        self.__id = id
        self.__name = name
        self.__phone_num = phone_num

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone_num(self):
        return self.__phone_num
