seznam = [7, 5, 1, 0, 4, 3, 7, 7, 7]

seznam.pop() # odstraní poslední prvek
seznam.pop(1) # odstraní prvek na daném indexu
seznam.append(8) # přidá prvek na konec seznamu
seznam.insert(1, 2) # přidá prvek na daný index
print(seznam[1:4]) # podseznam
print(seznam[-3]) # záporné indexy odzadu seznamu
print(len(seznam)) # počet prvků v seznamu

# součet všech čísel v seznamu
"""
soucet = 0
for i in range(len(seznam)):
    soucet += seznam[i]
print(soucet)
"""

# největší a nejmenší číslo v seznamu
nejvetsi = seznam[0]
nejmensi = seznam[0]
nejvetsiPozice = 0
nejmensiPozice = 0
for i in range(len(seznam)):
    if seznam[i] > nejvetsi:
        nejvetsi = seznam[i]
        nejvetsiPozice = i
    if seznam[i] < nejmensi:
        nejmensi = seznam[i]
        nejmensiPozice = i
print("největší číslo je", nejvetsi,
      ", je na pozici", nejvetsiPozice)
print("nejmenší číslo je", nejmensi,
      ", je na pozici", nejmensiPozice)

