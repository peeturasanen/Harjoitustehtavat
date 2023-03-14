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

auto = Auto("ABC-123", 142, 0, 0)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)

print(f"Auton Rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus}km/h, tämänhetkinen nopeus on {auto.tämänhetkinen_nopeus}km/h, ja kuljettu matka on {auto.kuljettu_matka}km.")