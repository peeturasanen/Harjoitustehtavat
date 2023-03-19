import random


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


class Sähköauto(Auto):
    def __init__(self, akkukapasiteetti, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, bensatankin_koko, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        super().__init__(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka)
        self.bensatankin_koko = bensatankin_koko


sähköauto = Sähköauto(52.5, "ABC-15", 180, 90, 0)
polttomoottoriauto = Polttomoottoriauto(32.3, "ACD-123", 165, 100, 0)

sähköauto.kiihdytä(random.randint(-10, 15))
polttomoottoriauto.kiihdytä(random.randint(-10, 15))
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)
print(f"sähköauton {sähköauto.rekisteritunnus} matkamittarilukema on {sähköauto.kuljettu_matka}km")
print(f"Polttomoottoriauton {polttomoottoriauto.rekisteritunnus} matkamittarilukema on {polttomoottoriauto.kuljettu_matka}km")
