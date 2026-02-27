class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def chod(self):
        print("ťap ťap")


class Pes(Zvire):
    def __init__(self, jmeno):
        super().__init__(jmeno)

    def zastekej(self):
        print("haf")


class Kocka(Zvire):
    def __init__(self, jmeno):
        super().__init__(jmeno)

    def zamnoukej(self):
        print("mňau")


p = Pes("Azor")
p.zastekej()

k = Kocka("Micka")
k.zamnoukej()

p.chod()
k.chod()
