import random
"""
padlo = 0
pocet = 0
while padlo != 6:
    padlo = random.randint(1, 6)
    pocet += 1
print(pocet)
"""
"""
pocet = 0
cisla = []
for i in range(10):
    cislo = random.randint(1, 6)
    cisla.append(cislo)
    if cislo == 3:
        pocet += 1

print(pocet)
print(cisla)
"""
# házet tak dlouho, dokud nepadne 5x šestka za sebou
# kolik hodů jsem potřeboval?

pocetSestek = 0
pocetHodu = 0

while pocetSestek < 5:
    cislo = random.randint(1, 6)
    if cislo == 6:
        pocetSestek += 1
    else:
        pocetSestek = 0
    pocetHodu += 1

print(pocetHodu)