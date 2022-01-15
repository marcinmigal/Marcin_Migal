from classes.Dieta import Dieta
from classes.Pacjent import Pacjent
from classes.Dietetyk import Dietetyk
from classes.Zamowienie import Zamowienie

dieta_1 = Dieta(1, 'Niskokaloryczna', 46.789, 1500)
dieta_2 = Dieta(3, 'Wysokokaloryczna', 62.321, 3000)
pacjent_1 = Pacjent('Jan', 'Kowalski', 'Prosta 23, Katowice', 43)
dietetyk_1 = Dietetyk('Adam', 'Nowak', 'Rozdzienskiego 1, Katowice', 12)

zam_1 = Zamowienie()
zam_1.id_zamowienia = 3421
zam_1.data_zamowienia = '2020-01-12'
zam_1.pacjent = pacjent_1
zam_1.diety = [dieta_1, dieta_2]


print(zam_1)

# print(zam_1.oblicz_wartosc_zamowienia())

# print(zam_1.oblicz_sume_kalorii())
