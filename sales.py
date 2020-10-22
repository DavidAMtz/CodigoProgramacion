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

    def agregar(self):
        archivo=open("sales.txt", "w")
        archivo.write(f" {self.digitalSales} " + "\n")
        archivo.write(f" {self.fisicalSales} " + "\n")
        archivo.close()

    def leerNumerosSales(self):
        archivo=open("sales.txt", "r")
        sumaSales = 0
        puntosSales = 0
        lineaSales = archivo.readline()
        while (lineaSales):
            sumaSales = sumaSales + int(lineaSales)
            lineaSales = archivo.readline()
        puntosSales = (sumaSales/100)
        print(puntosSales)
        archivo.close()