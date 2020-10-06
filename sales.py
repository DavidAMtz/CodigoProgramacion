class sales:

    def __init__(self, digitalSales, fisicalSales):
        self.digitalSales = digitalSales
        self.fisicalSales = fisicalSales

    @property
    def digitalSales(self):
        return self.__digitalSales

    digitalSales.setter
    def digitalSales(self, valor):
        self.__digitalSales = valor

    @property
    def fisicalSales(self):
        return self.__fisicalSales

    fisicalSales.setter
    def fisicalSales(self, valor):
        self.__fisicalSales =  valor
