oletus_kapasiteetti = 5
oletus_lisays = 5


class IntJoukko:
    def __init__(self, kapasiteetti=oletus_kapasiteetti, kasvatuskoko=oletus_lisays):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")

        self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("kapasiteetti2") 

        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True

        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.lukujono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm % len(self.lukujono) == 0:
            taulukko_old = self.lukujono
            self.kopioi_taulukko(self.lukujono, taulukko_old)
            self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(taulukko_old, self.lukujono)

        return True

    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                for j in range(i, self.alkioiden_lkm - 1):
                    apu = self.lukujono[j]
                    self.lukujono[j] = self.lukujono[j + 1]
                    self.lukujono[j + 1] = apu

                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos