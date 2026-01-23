l = [
    [5, 2, 1],
    [8, 7, 0],
    [4, 6, 1]
]

# najít, jestli l obsahuje 6, na jaké pozici?
cislo = 6
nasel = False
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == cislo:
            print("číslo je na pozici", i, j)


# zjistit počet všech hodnot v seznamu

soucet = 0
for malySeznam in l:
    soucet += len(malySeznam)
print(soucet)
