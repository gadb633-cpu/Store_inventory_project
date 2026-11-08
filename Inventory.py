class Inventory:
    def __init__(self):
        self.__products =[]
    def add(self,product):
        if self.find(product) ==None:
            self.__products.append(product)
        else:
            raise ValueError(f"{product}already exists")  
    def find(self,name):
        for product in self.__products:
            if product.name == name:
                return product
        return None
    def by_value(self):
        return list(sorted(self.__products,key=lambda p: p.total_value,reverse=True))
    @property
    def total_value(self):
        return sum(product.total_value for product in self.__products)