#seznam = [9,8,7,6,5,4,3,2,1,0]
#seznam = [1,2,3,4,5]
#seznam = [5, 2, 3, 2, 3, 2, 5, 3, 2, 2]
seznam = ["petr", "jakub", "aleš", "roman"]
# [2, 3, 4, 5, 7, 8, 9]

for j in range(len(seznam)):
    for i in range(len(seznam) - 1 - j):
        if seznam[i] > seznam[i + 1]:
            temp = seznam[i]
            seznam[i] = seznam[i + 1]
            seznam[i + 1] = temp

print(seznam)
"""      
x = 1
y = 5
temp = x
x = y
y = temp
"""