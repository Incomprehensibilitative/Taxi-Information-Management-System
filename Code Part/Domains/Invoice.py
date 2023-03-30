""" Invoice is the record for all the charges after using the taxi service
- Invoice is created alongside with Driver and Customer since it hold the transaction between the two
- id: unique id
- payment_mode: cash, banking
- distance: total distance traveled
- total: the total price
"""


class Invoice:
    def __init__(self):
        self.__id = None
        self.__customer_id = None
        self.__driver_id = None
        self.__date = None
        self.__payment_mode = None
        self.__price_per_km = None
        self.__distance = None
        self.__total_fee = None

    def set_invoice(self, id, customer_id, driver_id, date, payment_mode, distance, price_per_km, total_fee):
        self.__id = id
        self.__customer_id = customer_id
        self.__driver_id = driver_id
        self.__date = date
        self.__payment_mode = payment_mode
        self.__price_per_km = price_per_km
        self.__distance = distance
        self.__total_fee = total_fee

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_payment_mode(self):
        return self.__payment_mode

    def get_distance(self):
        return self.__distance

    def get_price_per_kn(self):
        return self.__price_per_km

    def get_total(self):
        return self.__total_fee
