class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto("ABC-123", 142, 0, 0)
print(f"Auton Rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus}km/h, tämänhetkinen nopeus on {auto.tämänhetkinen_nopeus}km/h, ja kuljettu matka on {auto.kuljettu_matka}km.")