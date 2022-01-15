class Pacjent:
    def __init__(self, imie, nazwisko, adres, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.wiek = wiek

    def __str__(self):
        return (f'Pacjent {self.imie} {self.nazwisko}, lat {self.wiek},'
                f'adres: {self.adres}')

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, value):
        self.__imie = value

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, value):
        self.__nazwisko = value

    @property
    def wiek(self):
        return self.__wiek

    @wiek.setter
    def wiek(self, value):
        self.__wiek = value

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        self.__adres = value
