from user import User


class Cart(User):

    def __init__(self, user):
        self.__orders = []
        self.__totalPrice = 0
        self.__totalDiscount = 0
        self.__user = user

    def calcTotalPrice(self):
        self.__totalPrice = sum(order.totalPrice for order in self.__orders)

    def addProduct(self, order):
        self.__orders.append(order)
        self.calcTotalPrice()

    def removeProduct(self, order):
        self.__orders.remove(order)
        self.calcTotalPrice()

    def calDiscount(self, discount=10):
        if self.user.isPremium:
            self.__totalDiscount = self.__totalPrice * discount / 100
            self.__totalPrice = self.__totalPrice - self.__totalDiscount

    @property
    def user(self):
        return self.__user

    @property
    def amount(self):
        return self.__totalPrice + self.__totalDiscount

    @property
    def discountAmount(self):
        return self.__totalDiscount

    @property
    def totalAmount(self):
        return self.__totalPrice - self.__totalDiscount

    @property
    def invoice(self):
        invoice = f"---------Inovice for {self.user.name}---------\n"
        invoice += f"Address: {self.__user.address}\t\tContact: {self.__user.contact}\n"
        invoice += f"-----------------------------------------\n"
        invoice += f"Products\tQuantity\t\tAmount\n"
        for order in self.__orders:
            pname = str(order.name)
            fun = lambda length: "\t\t\t" if length <4 else "\t\t"
            tab = fun(len(pname))
            invoice += f"{order.name}{tab}{order.quantity}\t\t\t\t{order.totalPrice}\n"

        invoice += f"-----------------------------------------\n"
        invoice += f"\t\t\tSub Total: \t\t{self.amount}\n"
        invoice += f"\t\t\tDicount:\t\t{self.discountAmount}\n"
        invoice += f"-----------------------------------------\n"
        invoice += f"\t\t\tTotal: \t\t\t{self.totalAmount}\n"
        return invoice
