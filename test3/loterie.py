vyherni = [4, 18, 25, 29, 31, 98, 99]
vsazene = []

for i in range(7):
    vsazene.append(int(input()))

pocet = 0
for i in vsazene:
    for j in vyherni:
        if i == j:
            pocet += 1

if pocet == 7:
    print("vyhrál jsi jackpot")
elif pocet > 4:
    print("vyhrál jsi malou výhru")
else:
    print("nevyhrál jsi")