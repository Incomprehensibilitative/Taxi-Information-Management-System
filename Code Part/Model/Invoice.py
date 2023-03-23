""" Invoice is the record for all the charges after using the taxi service
- Invoice is created along side with Driver and Customer since it hold the transaction between the two
- id: unique id
- payment_mode: C, B (cash, banking)
- distance: total distance traveled
- total: the total price
"""


class Invoice:
    def __init__(self):
        self.__id = None
        self.__date = None
        self.__payment_mode = None
        self.__distance = None
        self.__total = None

    def set_invoice(self, id, name, date, payment_mode, distance):
        self.__id = id
        self.__name = name
        self.__date = date
        self.__payment_mode = payment_mode
        self.__distance = distance

    def set_total(self, total):
        self.__total = total

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
