seznam = [7, 5, 8, 9, 3, 6, 10, 0]


for j in range(len(seznam) - 1):
    nejvetsiIndex = 0
    for i in range(len(seznam) - j):
        if seznam[i] > seznam[nejvetsiIndex]:
            nejvetsiIndex = i

    temp = seznam[nejvetsiIndex]
    seznam[nejvetsiIndex] = seznam[- 1 - j]
    seznam[- 1 - j] = temp

print(seznam)
