file = open("text_files/soubor1.txt", "r", encoding="utf-8")
text = file.read()
file.close()
seznam = text.split("\n")
soucet = 0
for i in seznam:
    soucet += int(i)

file = open("text_files/soubor2.txt", "w", encoding="utf-8")
file.write(str(soucet / len(seznam)))
file.close()

file = open("text_files/soubor3.txt", "r", encoding="utf-8")
text = file.read()
file.close()
osoby = text.split("\n")
nejstarsi_vek = 0
nejstarsi_jmeno = ""
for o in osoby:
    hodnoty = o.split(",")
    if int(hodnoty[2]) > nejstarsi_vek and hodnoty[1] == "muž":
        nejstarsi_jmeno = hodnoty[0]
        nejstarsi_vek = int(hodnoty[2])

print(nejstarsi_jmeno)

#TODO: uložte aritmetický průměr z první části do souboru soubor2.txt
#TODO: vypsat jméno nejstaršího muže
