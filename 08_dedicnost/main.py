class Tvar2d:
    def __init__(self, jmeno):
        self.jmeno = jmeno


    def obvod(self):
        return 0


    def obsah(self):
        return 0


    def ma_vetsi_obsah(self, tvar2):
        return self.obsah() > tvar2.obsah()


    def je_podobny(self, tvar2):  # tvar2 musí být stejného typu
        return True


class Ctverec(Tvar2d):
    def __init__(self, jmeno, a):
        super().__init__(jmeno)
        self.a = a


    def obvod(self):
        return 4 * self.a


    def obsah(self):
        return self.a ** 2

    def je_podobny(self, tvar2):
        return True


class Obdelnik(Tvar2d):
    def __init__(self, jmeno, a, b):
        super().__init__(jmeno)
        self.a = a
        self.b = b


    def obvod(self):
        return self.a * 2 + self.b * 2


    def obsah(self):
        return self.a * self.b


    def je_podobny(self, tvar2):
        return self.a / self.b == tvar2.a / tvar2.b


class Kruh(Tvar2d):
    def __init__(self, jmeno, r):
        super().__init__(jmeno)
        self.r = r


    def obvod(self):
        return 2 * 3.14 * self.r


    def obsah(self):
        return 3.14 * (self.r ** 2)


    def je_podobny(self, tvar2):
        return True


class Trojuhelnik(Tvar2d):
    def __init__(self, jmeno, a, b, c):
        self.kontrola(a, b, c)
        super().__init__(jmeno)
        self.a = a
        self.b = b
        self.c = c

    def kontrola(self, a, b, c):
        strany = [a, b, c]
        strany.sort()
        if strany[0] + strany[1] <= strany[2]:
            raise ValueError("takový trojúhelník neexistuje")


    def obvod(self):
        return self.a + self.b + self.c


    def obsah(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


    def je_podobny(self, tvar2):
        return self.a / self.b == tvar2.a / tvar2.b and \
            self.a / self.c == tvar2.a / tvar2.c and \
            self.b / self.c == tvar2.b / tvar2.c


class RovnostrannyTrojuhelnik(Trojuhelnik):
    def __init__(self, jmeno, a):
        super().__init__(jmeno, a, a, a)


    def obvod(self):
        return self.a * 3


    def obsah(self):
        v = (self.a ** 2 - (self.a / 2) ** 2) ** 0.5
        return (self.a * v) / 2


    def je_podobny(self, tvar2):
        return True



c1 = Ctverec("čtvereček1", 5)
c2 = Ctverec("čtvereček2", 6)

o1 = Obdelnik("obdélníček1", 2, 3)
o2 = Obdelnik("obdélníček2", 4, 5)

k1 = Kruh("kolečko", 5)

t1 = Trojuhelnik("trolhůhelníček1", 2, 2, 3)
t2 = Trojuhelnik("trolhůhelníček1", 4, 4, 6)

print(t1.je_podobny(t2))
