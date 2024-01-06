import numpy as np
arr = np.random.randint(1, 10, size=100)
print(arr[arr>7].size/arr.size*100)