class Invoice:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__date = None
        self.__payment_mode = None
        self.__distance = None

    def set_invoice(self, id, name, date, payment_mode, distance):
        self.__id = id
        self.__name = name
        self.__date = date
        self.__payment_mode = payment_mode
        self.__distance = distance

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_payment_mode(self):
        return self.__payment_mode

    def get_distance(self):
        return self.__distance
