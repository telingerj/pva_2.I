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


    def pridejVybeh(self, vybeh):
        self.vybehy.append(vybeh)
        vybeh.pridejZoo(self)


class Vybeh:
    def __init__(self, nazev, rozloha):
        self.nazev = nazev
        self.rozloha = rozloha
        self.zoo = None


    def pridejZoo(self, zoo):
        self.zoo = zoo

z = Zoo("Zoo Praha", "Troja", 200, 1931, 545)
z2 = Zoo("Zoo Plzeň", "Plzeň", 150, 1954, 320)
z3 = Zoo("Zoo pohádkový les", "Pohádkový les", 100, 2010, 121)

v = Vybeh("sloni", 51)
v2 = Vybeh("žirafy", 32)
v3 = Vybeh("ptáci", 2)

z.pridejVybeh(v)
z.pridejVybeh(v2)
print(v.zoo.rokZalozeni)
