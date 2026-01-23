slovo = input()
slovo2 = ""

for i in range(len(slovo) - 1, -1, -1):
    slovo2 += slovo[i]

if slovo == slovo2:
    print("ano")
else:
    print("ne")
