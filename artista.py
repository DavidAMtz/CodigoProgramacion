class artista:

    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    def agregar(self):
        archivo=open("artista.txt", "w")
        archivo.write(f"{self.nombre} ")
        archivo.close()
    
    def nombreArtista(self):
        archivo=open("artista.txt", "r")
        lineaArtista = archivo.readline()
        archivo.close()
        print(lineaArtista)



    