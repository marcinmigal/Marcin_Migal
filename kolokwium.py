class FirmaTransportowa:
    def __init__(self, nazwa_firmy: str, adres: str, rodzaj_dzialanosci: str, wlasciciel:str, nip:int):
        self.__nazwa_firmy = nazwa_firmy
        self.__adres = adres
        self.__rodzaj_dzialanosci = rodzaj_dzialanosci
        self.__wlasciciel = wlasciciel
        self.__nip = nip
    @property
    def get_nazwa_firmy(self):
        return self.nazwa_firmy
    @property
    def get_adres(self):
        return self.__adres
    @property
    def get_rodzaj_dzialanosci(self):
        return self.__rodzaj_dzialanosci
    @property
    def get_wlasciciel(self):
        return self.__wlasciciel
    @property
    def get_nip(self):
        return self.__nip

    def __str__(self) -> str:
        return f'Firma transportowa: {self.nazwa_firmy}, adres: {self.adres}, prowadzona przez: {self.wlasciciel} {self.nip}, rodzaj dzialanosci: {self.rodzaj_dzialanosci}'

class FirmaSpozywcza:
    def __init__(self, nazwa_firmy: str, ulica: str, nr_bundynku: str, ilosc_pracownikow:int, miasto:str):
        self.__nazwa_firmy = nazwa_firmy
        self.__ulica = ulica
        self.__nr_bundynku = nr_bundynku
        self.__ilosc_pracownikow = ilosc_pracownikow
        self.__miasto = miasto  

    @property
    def get_nazwa_firmy(self):
        return self.__nazwa_firmy
    @property
    def get_ulica(self):
        return self.__ulica
    @property
    def get_nr_budynku(self):
        return self.__nr_bundynku
    @property
    def get_ilosc_pracownikow(self):
        return self.__ilosc_pracownikow
    @property
    def get_miasto(self):
        return self.__miasto

    def __str__(self) -> str:
        return f'Firma spozywcza {self.nazwa_firmy}, Adres {self.miasto}, {self.ulica}, {self.nr_budynku}, Aktualnie zatrudnia: {self.ilosc_pracownikow} pracowników'

class Pojazd(FirmaTransportowa):
    def __init__(self, nr_rejestracji: str, marka: str, model: str, rocznik:int, przebieg:float, nazwa_firmy:str ):
        super().__init__(nazwa_firmy)
        self.nr_rejestracji = nr_rejestracji
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.przebieg = przebieg
    @property
    def get_nr_rejestracji(self):
        return self.__nr_rejestracji
    @property
    def get_marka(self):
        return self.__marka
    @property
    def get_model(self):
        return self.__model
    @property
    def get_rocznik(self):
        return self.__rocznik
    @property
    def get_przebieg(self):
        return self.__przebieg

    def __str__(self) -> str:
        return f'Pojazd {self.marka} {self.model} o rejestracji {self.nr_rejestracji}, rocznik {self.rocznik}, przebieg {self.przebieg}'

class Odcinek:
    def __init__(self, dystans:float, miejscowosc_startowa: str, miejscowosc_koncowa: str, czy_odc_platny: str, przejazd_zagraniczny:str):
        self.__dystans = dystans
        self.__miejscowosc_startowa = miejscowosc_startowa
        self.__miejscowosc_koncowa = miejscowosc_koncowa
        self.__czy_odc_platny = czy_odc_platny
        self.__przejazd_zagraniczny = przejazd_zagraniczny

    @property
    def get_dystans(self):
        return self.__dystans

    @property
    def get_miejscowosc_startowa(self):
        return self.__miejscowosc_startowa

    @property
    def get_miejscowosc_koncowa(self):
        return self.__miejscowosc_koncowa

    @property
    def get_czy_odc_platny(self):
        return self.__czy_odc_platny

    @property
    def get_przejazd_zaraniczny(self):
        return self.__przejazd_zagraniczny


    def __str__(self) -> str:
        return f'Odcinek o dystansie: {self.dystans}, rozpoczęty w: {self.miejscowosc_startowa}, zakończony w: {self.miejscowosc_koncowa}, przejazd zagraniczny: {self.przejazd_zagraniczny}, odcinek platny: {self.czy_odc_platny}' 

class Kurs():
    def __str__(self) -> str:
        return f'Kurs {self.kod_systemowy}, '
    @property
    def get_kod_systemowy(self):
        return self.__kod_systemowy

    @get_kod_systemowy.setter
    def set_kod_systemowy(self, value):
            self.__kod_systemowy = value

    @property
    def get_data_rozpoczecia(self):
        return self.__data_rozpoczecia

    @get_data_rozpoczecia.setter
    def set_data_rozpoczecia(self, value):
            self.__data_rozpoczecia = value


    @property
    def get_data_zakonczenia(self):
        return self.__data_zakonczenia

    @get_data_zakonczenia.setter
    def set_data_zakonczenia(self, value):
            self.__data_zakonczenia = value

    @property
    def get_koszty(self):
        return self.__koszty

    @get_koszty.setter
    def set_koszty(self, value):
            self.__koszty = value

    @property
    def get_zysk(self):
        return self.__zysk

    @get_zysk.setter
    def set_zysk(self, value):
            self.__zysk = value
            



odc_1 = Odcinek(256, 'Katowice', 'Wroclaw', 'Tak', 'Nie')
odc_2 = Odcinek(1400, 'Katowice', 'Wenecja', 'Tak', 'Tak')

kurs_1 = Kurs()
kurs_1.set_kod_systemowy = 'K255'
kurs_1.set_data_rozpoczecia = '12.10.2021'
kurs_1.set_data_zakonczenia = '12.10.2021'
kurs_1.set_koszty = 670
kurs_1.set_zysk = 4800