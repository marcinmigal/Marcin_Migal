class Dieta:
    def __init__(self, id_diety, nazwa, cena, kalorie):
        self.id_diety = id_diety
        self.nazwa = nazwa
        self.cena = cena
        self.kalorie = kalorie

    def __str__(self):
        return (f'Dieta nr {self.id_diety}, Nazwa {self.nazwa},'
                f'cena: {self.cena} , ilosc kalorii: {self.kalorie}')

    @property
    def id_diety(self):
        return self.__id_diety

    @id_diety.setter
    def id_diety(self, value):
        self.__id_diety = value

    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, value):
        self.__nazwa = value

    @property
    def cena(self):
        return self.__cena

    @cena.setter
    def cena(self, value):
        self.__cena = value

    @property
    def kalorie(self):
        return self.__kalorie

    @kalorie.setter
    def kalorie(self, value):
        self.__kalorie = value
