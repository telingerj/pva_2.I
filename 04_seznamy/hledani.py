l = [8, 4, 7, 0, 2, 6, 4, 9]
# najde hledané číslo a řekne index

hledaneCislo = int(input())
nasel = False
for i in range(len(l)):
    if l[i] == hledaneCislo:
        print("hledane číslo je na pozici", i)
        nasel = True
        break

if not nasel:
    print("číslo tam není")
