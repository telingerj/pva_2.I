# všechna sudá čísla od 1 do 10
# všechna lichá čísla od 1 do 10

# všechna čísla od 1 do 100, která jsou
# dělitelná 2, ale ne 3

"""
a = 0
while a < 10:
    print(a)
    a += 1
"""
"""
a = 2
while a <= 10:
    print(a)
    a += 2
"""
"""
a = 1
while a <= 10:
    print(a)
    a += 2
"""
"""
a = 1
while a <= 100:
    if a % 2 == 0 and a % 3 != 0:
        print(a)
    a += 1
"""

# rozhodněte, jestli je číslo ze vstupu prvočíslo
# prvočísla od 2 do 100
"""
k = 2
while k < 100:
    i = 2
    jePrvocislo = True
    while i < k:
        if k % i == 0:
            jePrvocislo = False
            break
        i += 1

    if jePrvocislo:
        print(k, end=" ")
    k += 1
"""
# prvočíselný rozklad zadaného čísla
"""
cislo = int(input())
while cislo > 1:
    i = 2
    while cislo % i != 0:
        i += 1
    print(i, end=" ")
    cislo /= i

"""

for i in range(100, 0, -1):
    print(i)