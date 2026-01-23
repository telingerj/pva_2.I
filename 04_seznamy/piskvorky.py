herniPole = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

hracNaTahu = "X"
vyhral = "."
while vyhral != "X" and vyhral != "O":
    # vykreslení herního pole
    for y in range(len(herniPole)):
        for x in range(len(herniPole[0])):
            print(herniPole[y][x], end=" ")
        print()

    # hráčův tah
    print("hraje hráč", hracNaTahu)
    while True:
        hracX = int(input("zadej pozici x: "))
        hracY = int(input("zadej pozici y: "))
        if (0 <= hracX <= len(herniPole) and
            0 <= hracY <= len(herniPole) and
                herniPole[hracY][hracX] == "."):
            break
        print("Tahle pozice není povolená")
    herniPole[hracY][hracX] = hracNaTahu

    # kontrola výhry
    for vyherniZnak in ["X", "O"]:
        # kontrol řádku
        for y in range(len(herniPole)):
            pocetZnaku = 0
            for x in range(len(herniPole[0])):
                if herniPole[y][x] == vyherniZnak:
                    pocetZnaku += 1
            if pocetZnaku == len(herniPole):
                vyhral = vyherniZnak
        # kontrola sloupce
        for x in range(len(herniPole[0])):
            pocetZnaku = 0
            for y in range(len(herniPole)):
                if herniPole[y][x] == vyherniZnak:
                    pocetZnaku += 1
            if pocetZnaku == len(herniPole):
                vyhral = vyherniZnak
        # kontrola diagonaly
        pocetZnaku = 0
        for i in range(len(herniPole)):
            if herniPole[i][i] == vyherniZnak:
                pocetZnaku += 1
        if pocetZnaku == len(herniPole):
            vyhral = vyherniZnak

        pocetZnaku = 0
        for i in range(len(herniPole)):
            if herniPole[i][2 - i] == vyherniZnak:
                pocetZnaku += 1
        if pocetZnaku == len(herniPole):
            vyhral = vyherniZnak



    # výměna hráče na tahu
    if hracNaTahu == "X":
        hracNaTahu = "O"
    elif hracNaTahu == "O":
        hracNaTahu = "X"

print("vyhrál hráč", vyhral)