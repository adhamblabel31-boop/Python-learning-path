# ------------------------------------------------
# ! ------- arithmetic & useful operations -------
# ------------------------------------------------
# ? addition
# ? subtraction
# ? multiplication
# ? division
# ------------------------------------------------
# ? min
# ? max
# ? sum
# ? ravel => returns flattened array 1 dimension with same type
# ------------------------------------------------

import numpy as np

# Arithmetic Operations

a1 = np.array([10, 20, 30])
a2 = np.array([5, 2, 4])

print(a1 + a2)  # result [15, 22, 34]
print(a1 - a2)  # result [5, 18, 26]
print(a1 * a2)  # result [50, 40, 120]
print(a1 / a2)  # result [2, 10, 7.5]

print("-" * 50)

a3 = np.array([[1, 4], [5, 9]])
a4 = np.array([[2, 7], [10, 5]])

print(a3 + a4)  # result [ [3, 11], [15, 14] ]
print(a3 - a4)  # result [ [-1, -3], [-5, 4] ]
print(a3 * a4)  # result [ [2, 28], [50, 45] ]
print(a3 / a4)  # result [ [0.5, 0.57142857], [0.5, 1.8] ]

print("-" * 50)

# min, max, sum

a5 = np.array([10, 20, 30])
print(a5.min())
print(a5.max())
print(a5.sum())

print("-" * 50)

a6 = np.array([[6, 4], [3, 9]])
print(a6.min())
print(a6.max())
print(a6.sum())

print("-" * 50)

# ravel

a7 = np.array([[6, 4], [3, 9]])
print(a7.ravel())

a8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a8.ndim)
print(a8.ravel())
x = a8.ravel()
print(x.ndim)