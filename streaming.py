class streaming:

    def __init__(self, streamYT, remix, streamDePaga):
        self.streamYT = streamYT
        self.remix = remix
        self.streamDePaga = streamDePaga

    @property
    def streamYT(self):
        return self.__streamYT

    @streamYT.setter
    def streamYT(self, valor):
        self.__streamYT = valor 

    @property
    def remix(self):
        return self.__remix

    @remix.setter
    def remix(self, valor):
        self.__remix = valor

    @property
    def streamDePaga(self):
        return self.__streamDePaga
    
    @streamDePaga.setter
    def streamDePaga(self, valor):
        self.__streamDePaga = valor

    def agregar(self):
        archivo=open("streaming.txt", "w")
        archivo.write(f" {self.streamYT} " + "\n")
        archivo.write(f" {self.remix} " + "\n")
        archivo.write(f" {self.streamDePaga} " + "\n")
        archivo.close()

    def leerNumerosStreaming(self):
        archivo=open("streaming.txt", "r")
        sumaStream = 0
        puntosStream = 0
        lineaStream = archivo.readline()
        while (lineaStream):
            sumaStream = sumaStream + int(lineaStream)
            lineaStream = archivo.readline()
        puntosStream = (sumaStream/200)
        print(puntosStream)      
        archivo.close()