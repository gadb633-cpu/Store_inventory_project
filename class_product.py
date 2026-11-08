class Product:
    def __init__(self,name,price,quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__total_value =0

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <=0:
            raise ValueError("price must be positive")
        else:
            self.__price = value

    @property
    def quantity(self):
        return self.__quantity
    
    def add_stock(self,amount):
        self.__quantity += amount

    def sell(self,amount):
        if amount > self.__quantity:
            raise ValueError(f"not enough {self.__name}")
        else:
            self.__quantity -= amount
    @property
    def total_value(self):
        self.__total_value = self.price*self.quantity
        return self.__total_value
    def __str__(self):
        return f"{self.__name}: {self.__price} x {self.__quantity}"