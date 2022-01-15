class Dietetyk:
    def __init__(self, imie, nazwisko, placowka, staz):
        self.imie = imie
        self.nazwisko = nazwisko
        self.placowka = placowka
        self.staz = staz

    def __str__(self):
        return (f'Dietetyk {self.imie} {self.nazwisko},'
                f'Placowka {self.placowka}, Staz {self.staz}')

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
    def placowka(self):
        return self.__placowka

    @placowka.setter
    def placowka(self, value):
        self.__placowka = value

    @property
    def staz(self):
        return self.__staz

    @staz.setter
    def staz(self, value):
        self.__staz = value
