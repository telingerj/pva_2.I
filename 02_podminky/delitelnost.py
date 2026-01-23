# zjistit, jestli je cislo sudé, nebo liché

cislo = int(input())
if cislo == 0:
    print("číslo je 0")
elif cislo % 2 == 0:
    print("číslo je sudé")
else:
    print("číslo je liché")