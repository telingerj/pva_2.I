import matplotlib.pyplot as plt
import math

x = []
y = []

for i in range(-50, 0):
    if i == 0:
        continue
    num = i / 10
    x.append(num)
    y.append(1 / num)

plt.plot(x, y, color="blue")

x = []
y = []

for i in range(0, 50):
    if i == 0:
        continue
    num = i / 10
    x.append(num)
    y.append(1 / num)

plt.plot(x, y, color="blue")
plt.show()
