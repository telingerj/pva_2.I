import matplotlib.pyplot as plt

znamky = [1, 4, 1, 1, 2, 4, 5, 1, 2, 4, 1]

x = []
y = []
s = 0

for i in range(len(znamky)):
    x.append(i)
    s += znamky[i]
    y.append(s / (i + 1))

plt.plot(x, y)
plt.show()
