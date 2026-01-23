seznam = [5, 2, 1, 4, 7, 8]

# vypsat všechna sudá čísla ze seznamu
# vypsat všechna lichá čísla ze seznamu
# vypsat všechna prvočísla ze seznamu

print("sudá čísla:", end="")
for i in range(len(seznam)):
    if seznam[i] % 2 == 0:
        print(seznam[i], end=" ")

print()
print("lichá čísla:", end="")
for i in range(len(seznam)):
    if seznam[i] % 2 == 1:
        print(seznam[i], end=" ")