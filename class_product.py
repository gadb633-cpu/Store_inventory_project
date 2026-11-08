class Product:
    def __init__(self,name,price,quntity):
        self.__name = name
        self.__price = price
        self.__quntity = quntity

    @property
    def name(self):
        return self.__name

    @name.setter
    def _name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def _price(self, value):
        self.__price = value

    @property
    def quntity(self):
        return self.__quntity