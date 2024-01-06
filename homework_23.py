import numpy as np
arr = np.random.randint(1, 10, size=100000)
rar = np.arange(0, 100)
arr = np.resize(arr, (1000, 100))
f = 0
for i in range(1000):
    if arr[i][arr[i] > 7].size/arr[i].size*100 == 20:
        f += 1
print(f/1000)

