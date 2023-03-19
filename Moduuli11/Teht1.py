class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu on nimeltään {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjailija on {self.kirjoittaja} ja kirjassa on {self.sivumäärä} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja on {self.päätoimittaja}")


julkaisu1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
julkaisu2 = Lehti("Aku Ankka", "Aki Hyyppä")

julkaisu1.tulosta_tiedot()
julkaisu2.tulosta_tiedot()
