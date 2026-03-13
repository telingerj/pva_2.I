#  hra, ve které proti sobě bojují dvě armády
import random


class Armada:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.postavy = []


    def pridej_postavu(self, postava):
        self.postavy.append(postava)
        postava.pridej_armadu(self)


class Postava:
    def __init__(self, jmeno, zdravi, rychlost):
        self.jmeno = jmeno
        self.zdravi = zdravi
        self.rychlost = rychlost
        self.armada = None


    def pridej_armadu(self, armada):
        self.armada = armada


    def uber_zdravi(self, zdravi):
        self.zdravi -= zdravi


class Bojovnik(Postava):
    def __init__(self, jmeno, zdravi, rychlost, poskozeni):
        super().__init__(jmeno, zdravi, rychlost)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass


class Lukostrelec(Bojovnik):
    def __init__(self, jmeno, zdravi, rychlost, poskozeni, pocet_sipu, presnost):
        super().__init__(jmeno, zdravi, rychlost, poskozeni)
        self.pocet_sipu = pocet_sipu
        self.presnost = presnost


    def utok(self, postava):
        if self.pocet_sipu <= 0:
            return
        self.pocet_sipu -= 1
        if random.randint(1, 100) <= self.presnost:
            postava.uber_zdravi(self.poskozeni)


class Sermir(Bojovnik):
    def __init__(self, jmeno, zdravi, rychlost, poskozeni, ucinnost_stitu):
        super().__init__(jmeno, zdravi, rychlost, poskozeni)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        postava.uber_zdravi(self.poskozeni)


    def uber_zdravi(self, zdravi):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            return
        self.zdravi -= zdravi


class Kouzelnik(Postava):
    def __init__(self, jmeno, zdravi, rychlost, sila_magie, ucinnost_lecby):
        super().__init__(jmeno, zdravi, rychlost)
        self.sila_magie = sila_magie
        self.ucinnost_lecby = ucinnost_lecby


    def lecba(self, postava):
        if random.randint(1, 100) > self.ucinnost_lecby:
            return
        postava.zdravi += self.sila_magie



armada1 = Armada("hodni", "modra")
armada2 = Armada("zli", "cervena")

l1 = Lukostrelec("Pepa", 100, 200, 10, 10, 100)
l2 = Lukostrelec("Franta", 80, 250, 15, 10, 100)
k1 = Kouzelnik("Gandalf", 70, 150, 10, 90)

s1 = Sermir("Milan", 100, 200, 10, 50)

armada1.pridej_postavu(l1)
armada2.pridej_postavu(l2)
armada1.pridej_postavu(s1)
armada2.pridej_postavu(k1)

print(l2.zdravi)
l1.utok(l2)
print(l2.zdravi)
k1.lecba(l2)
print(l2.zdravi)
