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

hissi = Hissi(30, 0, 0)
hissi.Siirry_kerrokseen(22)
hissi.Siirry_kerrokseen(0)