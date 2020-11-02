from numpy import linalg as LA
import numpy as np

w, v = LA.eig(np.array([[1, -1],
                        [1, 1]]))
print("One")
print(w[0])
print(v[:, 0][0], " ", v[:, 0][1])
print("Two")
print(w[1])
print(v[:, 1][0], " ", v[:, 1][1])
