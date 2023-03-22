class Feedback:
    def __init__(self):
        self.__id = None
        self.__rate = None
        self.__date = None
        self.__message = None

    def set_feedback(self, id, rate, date, message):
        self.__id = id
        self.__rate = rate
        self.__date = date
        self.__message = message

    def get_id(self):
        return self.__id

    def get_rate(self):
        return self.__rate

    def get_data(self):
        return self.__date

    def get_message(self):
        return self.__message
