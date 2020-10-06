class radio:

    def __init__(self, radioPlays):
        self.radioPlays = radioPlays

    @property
    def radioPlays(self):
        return self.__radioPlays

    @radioPlays.setter
    def radioPlays(self, valor):
        self.__radioPlays = valor

    
        

