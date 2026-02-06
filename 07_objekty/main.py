class Clovek:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.auta = []


    def pozdrav(self):
        print("Ahoj, já se jmenuju", self.jmeno, "a je mi", self.vek, "let")


    def starsi20Let(self):
        if self.vek > 20:
            return True
        return False


    def pridejAuto(self, auto):
        self.auta.append(auto)
        auto.pridejMajitele(self)


class Auto:
    def __init__(self, vykon, kapacita, cena, znacka):
        self.vykon = vykon
        self.kapacita = kapacita
        self.cena = cena
        self.znacka = znacka
        self.majitel = None


    def jeVykonnejsiNez(self, auto2):
        if self.vykon > auto2.vykon:
            return True
        return False


    def pridejMajitele(self, clovek):
        self.majitel = clovek


h = Clovek("Petr", 51)
h2 = Clovek("Jakub", 38)
h3 = Clovek("Anička", 9)

a1 = Auto(200, 4, 900000, "Audi")
a2 = Auto(80, 5, 100000, "Škoda")

a2.pridejMajitele(h)
print(a2.majitel.jmeno)