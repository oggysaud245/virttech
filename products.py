class Products:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__description = None

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @name.setter
    def name(self, name):
        self.__name = name

    @price.setter
    def price(self, price):
        self.__price = price

    @description.setter
    def description(self, description):
        self.__description = description

