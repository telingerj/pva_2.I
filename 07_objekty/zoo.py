class Zoo:
    def __init__(self, nazev, lokace, vstupne, rokZalozeni, rozloha):  # konstruktor
        self.nazev = nazev
        self.lokace = lokace
        self.vstupne = vstupne
        self.rokZalozeni = rokZalozeni
        self.rozloha = rozloha
        self.vybehy = []


    def vypis(self):
        print("zoologická zahrada", self.nazev, "v místě", self.lokace)


    def bylaZalozenaVTomtoStoleti(self):
        if self.rokZalozeni >= 2000:
            return True
        return False


    def jeStarsiNez(self, zoo2):
        if zoo2.rokZalozeni > self.rokZalozeni:
            return True
        return False


    def rozlohaVsechVybehu(self):
        s = 0
        for vybeh in self.vybehy:
            s += vybeh.rozloha
        return s


    def pridejVybeh(self, vybeh):
        if self.rozlohaVsechVybehu() + vybeh.rozloha > self.rozloha:
            return False
        self.vybehy.append(vybeh)
        vybeh.pridejZoo(self)
        return True


    def vratJmenaVsechZvirat(self):
        vsechnaZvirata = []
        for vybeh in self.vybehy:
            for zvire in vybeh.zvirata:
                vsechnaZvirata.append(zvire.jmeno)
        return vsechnaZvirata


class Vybeh:
    def __init__(self, nazev, rozloha):
        self.nazev = nazev
        self.rozloha = rozloha
        self.zoo = None
        self.zvirata = []


    def pridejZoo(self, zoo):
        self.zoo = zoo


    def pridejZvire(self, zvire):
        if len(self.zvirata) == 0:  # výběh je prázdný - přidání se vždy povede
            self.zvirata.append(zvire)
            zvire.pridejVybeh(self)
            return True
        if zvire.typ != self.zvirata[0].typ:
            return False
        self.zvirata.append(zvire)
        zvire.pridejVybeh(self)
        return True


class Zvire:
    def __init__(self, jmeno, hmotnost, typ, vyska):
        self.jmeno = jmeno
        self.hmotnost = hmotnost
        self.typ = typ
        self.vyska = vyska
        self.vybeh = None


    def pridejVybeh(self, vybeh):
        self.vybeh = vybeh



z = Zoo("Zoo Praha", "Troja", 200, 1931, 545)
z2 = Zoo("Zoo Plzeň", "Plzeň", 150, 1954, 70)
z3 = Zoo("Zoo pohádkový les", "Pohádkový les", 100, 2010, 121)

v = Vybeh("sloni", 51)
v2 = Vybeh("žirafy", 32)
v3 = Vybeh("ptáci", 2)
zv1 = Zvire("Pepa", 3654, "slon", 3)
zv2 = Zvire("Franta", 3788, "slon", 3.1)
zv3 = Zvire("Emílie", 2874, "žirafa", 8)

z.pridejVybeh(v)
z.pridejVybeh(v2)
z.pridejVybeh(v3)

v.pridejZvire(zv1)
v.pridejZvire(zv2)
v2.pridejZvire(zv3)

print(z.vratJmenaVsechZvirat())
