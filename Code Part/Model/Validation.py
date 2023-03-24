import re


class Validation:
    @staticmethod
    def is_valid_phone_number(phone_number):
        pattern = r"^\d{3}-\d{3}-\d{4}$"
        return bool(re.match(pattern, phone_number))

    @staticmethod
    def is_valid_name(name):
        pattern = r"^[a-zA-Z\s]+$"
        return bool(re.match(pattern, name))

    @staticmethod
    def is_valid_date(date):
        pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})$"
        return bool(re.match(pattern, date))

    @staticmethod
    def is_valid_rating(rate):
        pattern = r"^[1-5]%"
        return bool(re.match(pattern, rate))

    @staticmethod
    def is_valid_payment_mode(payment_mode):
        pattern = r"^(cash|banking)$"
        return bool(re.match(pattern, payment_mode))

    @staticmethod
    def is_valid_distance(distance):
        pattern = r"^\d+(\.\d+)?\s*km$"
        return bool(re.match(pattern, distance))

    @staticmethod
    def is_valid_total_fee(total_fee):
        pattern = r"^\d+(\.\d+)?\s*VND$"
        return bool(re.match(pattern, total_fee))

    @staticmethod
    def is_valid_regis_num(regis_num):
        pattern = r"^(29|30|31)[A-Z]\d\s\d{4,5}$"
        return bool(re.match(pattern, regis_num))

    @staticmethod
    def is_valid_price(price):
        pattern = r"^\d+(\.\d+)?\s*VND$"
        return bool(re.match(pattern, price))
        # this is price from Vehicle and price_per_km from Invoice

    @staticmethod
    def is_valid_salary(salary):
        pattern = r"^\d+(\.\d+)?\s*VND$"
        return bool(re.match(pattern, salary))

    @staticmethod
    def is_valid_age(age):
        pattern = r"^\d+$"
        return bool(re.match(pattern, age))

    @staticmethod
    def is_valid_gender(gender):
        pattern = r"^(Male|Female|Other)$"
        return bool(re.match(pattern, gender))

    # chưa làm id bởi vì đầu buồi :))
