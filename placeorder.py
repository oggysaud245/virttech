from products import Products


class PlaceOrder(Products):

    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity
        self.__totalPrice = self.__product.price * self.__quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def name(self):
        return self.__product.name

    @property
    def price(self):
        return self.__product.price

    @property
    def description(self):
        return self.__product.description

    @property
    def totalPrice(self):
        return self.__totalPrice
