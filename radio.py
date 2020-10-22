class radio:

    def __init__(self, radioPop, radioAC):
        self.radioPop = radioPop
        self.radioAC = radioAC

    @property
    def radioPop(self):
        return self.__radioPop

    @radioPop.setter
    def radioPop(self, valor):
        self.__radioPop = valor

    @property
    def radioAC(self):
        return self.__radioAC

    @radioAC.setter
    def radioAC(self, valor):
        self.__radioAC = valor

    def agregar(self):
        archivo=open("radio.txt", "w")
        archivo.write(f" {self.radioPop} " + "\n")
        archivo.write(f" {self.radioAC} " + "\n")
        archivo.close()

    def leerNumerosRadio(self):
        archivo=open("radio.txt", "r")
        sumaRadio = 0
        puntosRadio = 0
        lineaRadio = archivo.readline()
        while (lineaRadio):
            sumaRadio = sumaRadio + int(lineaRadio)
            lineaRadio = archivo.readline()
        puntosRadio = (sumaRadio/700)
        print(puntosRadio)
        archivo.close()
     