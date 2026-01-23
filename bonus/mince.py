import matplotlib.pyplot as plt
import random

x = []
y = []
s = 0

for i in range(1000):
    x.append(i)
    if random.randint(0, 1) == 0:
        s += 1
    else:
        s -= 1
    y.append(s)

plt.plot(x, y)
plt.show()