cislo = int(input())

while cislo > 1:
    print(cislo, end=",")
    if cislo % 2 == 0:
        cislo = int(cislo / 2)
    else:
        cislo = cislo * 3 + 1

print(cislo)