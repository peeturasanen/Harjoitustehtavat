class Hissi:
    def __init__(self, ylinkerros, alinkerros, kerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.kerros = kerros

    def Siirry_kerrokseen(self, mene):
        while self.kerros != mene:
            if self.kerros < mene:
                self.Kerros_ylös()
            if self.kerros > mene:
                self.Kerros_alas()
        print(f"Saavut kerrokseen {self.kerros}.")

    def Kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(self.kerros)

    def Kerros_alas(self):
        self.kerros = self.kerros - 1
        print(self.kerros)

class Talo:
    def __init__(self, talon_ylinkerros, talon_alinkerros, määrä):
        self.talon_ylinkerros = talon_ylinkerros
        self.talon_alinkerros = talon_alinkerros
        self.määrä = määrä
        self.hissit = []
        self.hissin_kerros = talon_alinkerros
        for i in range(self.määrä):
            self.hissit.append(Hissi(self.talon_ylinkerros, self.talon_alinkerros, self.hissin_kerros))

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        print(f"hissi {hissin_numero}")
        self.hissit[hissin_numero - 1].Siirry_kerrokseen(kohde_kerros)

talo = Talo(30,0,3)

talo.aja_hissiä(1,22)
talo.aja_hissiä(2,10)
talo.aja_hissiä(1,0)
talo.aja_hissiä(2,9)