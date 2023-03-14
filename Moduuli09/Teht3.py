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
        print(f"Auton tämänhetkinen nopeus on {self.tämänhetkinen_nopeus}km/h.")
        return

    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + (self.tämänhetkinen_nopeus * aika)
        print(f"Auton kuljettu matka {self.kuljettu_matka}km")
        return

auto = Auto("ABC-123", 142, 0, 0)

auto.kiihdytä(50)
auto.kulje(2)
print(f"Auton Rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus}km/h, tämänhetkinen nopeus on {auto.tämänhetkinen_nopeus}km/h, ja kuljettu matka on {auto.kuljettu_matka}km.")