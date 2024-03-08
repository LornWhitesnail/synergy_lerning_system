import matplotlib.pyplot as plt
from math import pi, sin, cos

x = [1, 2, 7]
y = [2, 6, 14]
lr = 0.01
w = [0]
b = [0]
for i in range(len(x)):
    dy = w[i] * x[i] + b[0]
    w.append(w[i] + 2 * lr * x[i] * (y[i] - dy))
    b.append(b[i] + 2 * lr * (y[i] - dy))
print(w, b)

x1 = []
lr= lr * 10
for a in range(100):
    x1.append(a*lr)
y1 = [[], [], [], []]
for i in range(4):
    for a in range(100):
        y1[i].append(x1[a] * w[i] + b[i])
plt.plot(x, y)
plt.plot(x1, y1[0])
plt.plot(x1, y1[1])
plt.plot(x1, y1[2])
plt.plot(x1, y1[3])
plt.show()