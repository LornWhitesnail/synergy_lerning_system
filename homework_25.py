import numpy as np
arr = np.arange(1, 11)
arr = np.resize(arr, (10, 10))
print(arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9])