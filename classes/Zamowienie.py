class Zamowienie:

    def __str__(self):
        return (f'Zam {self.id_zamowienia}, dla pacjenta '
                f'{self.pacjent.imie} {self.pacjent.nazwisko}'
                f'data: {self.data_zamowienia}, '
                f'wybrane diety: {self.wybrane_diety} '
                f'wartosc zamowienia: {self.oblicz_wartosc_zamowienia()} '
                f'suma kalorii w zamowieniu: {self.oblicz_sume_kalorii()}')

    @property
    def id_zamowienia(self):
        return self.__id_zamowienia

    @id_zamowienia.setter
    def id_zamowienia(self, value):
        self.__id_zamowienia = value

    @property
    def pacjent(self):
        return self.__pacjent

    @pacjent.setter
    def pacjent(self, value):
        self.__pacjent = value

    @property
    def diety(self):
        return self.__diety

    @diety.setter
    def diety(self, value):
        self.__diety = value
        self.wybrane_diety = [item.id_diety for item in value]

    @property
    def data_zamowienia(self):
        return self.__data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, value):
        self.__data_zamowienia = value

    def oblicz_wartosc_zamowienia(self):
        wartosc = 0
        for i in self.diety:
            wartosc += i.cena
        return round(wartosc, 2)

    def oblicz_sume_kalorii(self):
        wartosc = 0
        for i in self.diety:
            wartosc += i.kalorie
        return round(wartosc, 2)

    def print_list(self):
        print(self.wybrane_diety)
