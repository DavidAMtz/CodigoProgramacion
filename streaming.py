class streaming:

    def __init__(self, stream, remix, streamDePaga):
        self.stream = strem
        self.remix = remix
        self.streamDePaga = streamDePaga

    @property
    def stream(self):
        return self.__stream

    @stream.setter
    def stream(self, valor):
        self.__stream = valor 

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