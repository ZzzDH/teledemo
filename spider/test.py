import numpy as np

arr = np.array([[1, 2, 100, 4, 5, 6],
                [ 1, 1, 100, 3, 5, 5],
                [2, 2, 4, 4, 6, 6]])
print(arr.shape)
print(arr.max(axis=0))