class User:

    def __init__(self, username, contact):
        self.__name = username
        self.__contact = contact
        self.__address = None
        self.__email = None
        self.__shippingAddress = self.__address
        self.__isPremimum = False
        self.__isAdmin = False

    @property
    def name(self):
        return self.__name

    @property
    def contact(self):
        return self.__contact

    @property
    def address(self):
        return self.__address

    @property
    def email(self):
        return self.__email

    @property
    def shippingAddress(self):
        return self.__shippingAddress

    @property
    def isPremimum(self):
        return self.__isPremimum

    @property
    def isAdmin(self):
        return self.__isAdmin

    @name.setter
    def name(self, name):
        self.__name = name

    @contact.setter
    def contact(self, contact):
        self.__contact = contact

    @address.setter
    def address(self, address):
        self.__address = address

    @email.setter
    def email(self, email):
        self.__email = email

    @shippingAddress.setter
    def shippingAddress(self, shippingAddress):
        self.__shippingAddress = shippingAddress

    @isPremimum.setter
    def isPremium(self, isPremimum):
        self.__isPremimum = isPremimum

    @isAdmin.setter
    def isAdmin(self, isAdmin):
        self.__isAdmin = isAdmin

    def makePremium(self, user):
        if self.__isAdmin:
            user.isPremium = True
