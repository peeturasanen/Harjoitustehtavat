import random
from prettytable import PrettyTable

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, muutos):
        self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + muutos
        if self.tämänhetkinen_nopeus <= 0:
            self.tämänhetkinen_nopeus = 0
        if self.tämänhetkinen_nopeus >= self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        return

    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + (self.tämänhetkinen_nopeus * aika)
        return

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_kilometreinä, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_kilometreinä = pituus_kilometreinä
        self.osallistuvat_autot = osallistuvat_autot
        self.Lista_autoista = []
        luku = 1
        for n in range(osallistuvat_autot):
            self.Lista_autoista.append(Auto("abc-" + str(luku), random.randint(100, 200), 0, 0))
            luku = luku + 1

    def tuntikuluu(self):
        for Auto in self.Lista_autoista:
            Auto.kiihdytä(random.randint(-10, 15))
            Auto.kulje(1)

    def Tulosta_tilanne(self):
        taulu = PrettyTable()
        taulu.field_names = ["rekisteritunnus", "kuljettu matka", "huippunopeus"]
        for Auto in self.Lista_autoista:
            taulu.add_row([Auto.rekisteritunnus, Auto.kuljettu_matka, Auto.huippunopeus])
        taulu.sortby = "kuljettu matka"
        taulu.reversesort = True
        print(taulu)

    def Kilpailu_ohi(self):
        maksimipituus = 0
        for Auto in self.Lista_autoista:
            if Auto.kuljettu_matka >= maksimipituus:
                maksimipituus = Auto.kuljettu_matka
        return maksimipituus > self.pituus_kilometreinä

kilpailu = Kilpailu("Suuri romuralli", 8000, 10)
tunnit = 10
while kilpailu.Kilpailu_ohi() is False:
    for i in range(10):
        if kilpailu.Kilpailu_ohi():
            break
        kilpailu.tuntikuluu()
    print(f"Tilanne {tunnit} tunnin jälkeen: ")
    tunnit = tunnit + 10
    kilpailu.Tulosta_tilanne()
print("Suuri romuralli on päättynyt ja tulokset ovat selvillä: ")
kilpailu.Tulosta_tilanne()