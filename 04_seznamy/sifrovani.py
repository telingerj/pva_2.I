zprava = "zprava"
zasifrovanaZprava = ""

for znak in zprava:
    kod = ord(znak)
    kod += 3
    if kod > ord("z"):
        kod -= 26
    zasifrovanaZprava += chr(kod)

print(zasifrovanaZprava)
