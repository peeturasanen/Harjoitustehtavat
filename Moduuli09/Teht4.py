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

Autot = []
luku = 1

for n in range(10):
    Autot.append(Auto("abc-" + str(luku), random.randint(100, 200), 0, 0))
    luku = luku + 1

kisanpituus = 0
while kisanpituus <= 10000:
    for auto in Autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= kisanpituus:
            kisanpituus = auto.kuljettu_matka

taulu = PrettyTable()
taulu.field_names = ["rekisteritunnus", "kuljettu matka", "huippunopeus"]
for auto in Autot:
    taulu.add_row( [auto.rekisteritunnus, auto.kuljettu_matka, auto.huippunopeus])
taulu.sortby = "kuljettu matka"
taulu.reversesort = True
print(taulu)