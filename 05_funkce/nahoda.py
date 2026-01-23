import random

pocetHodu = 10000000
cisla = [0, 0, 0, 0, 0, 0]
for i in range(pocetHodu):
    hod = random.randint(1, 6)
    cisla[hod - 1] += 1


for i in range(len(cisla)):
    print(i + 1, ":", (cisla[i] / pocetHodu) * 100, "%")