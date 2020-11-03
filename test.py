import numpy as np

x = np.array([[1, 2],
              [3, 4]])

min_ind = np.argmin(x[:, 1])
element = x[min_ind]
print(min_ind)
print(element)
