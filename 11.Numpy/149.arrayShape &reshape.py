# ------------------------------------
#! ------ array shape & reshape ------
# ------------------------------------
# ? shape returns a tuple contains the number of elements in each dimension
# ------------------------------------

import numpy as np

a1 = np.array([1, 2, 3, 4])
print(a1.ndim)
print(a1.shape)

print("-" * 50)

a2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(a2.ndim)
print(a2.shape)

print("-" * 50)

a3 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])
print(a3.ndim)
print(a3.shape)

print("-" * 50)

a4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(a4)
print(a4.ndim)
print(a4.shape)

print("*" * 50)

reshaped_a4 = a4.reshape(3, 4)
print(reshaped_a4)
print(reshaped_a4.ndim)
print(reshaped_a4.shape)

print("-" * 50)

a5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(a5.ndim)
print(a5.shape)

print("*" * 50)

reshaped_a5 = a5.reshape(-1)
print(reshaped_a5)
print(reshaped_a5.ndim)
print(reshaped_a5.shape)

print("*" * 50)

reshaped_a5 = a5.reshape(5, 4)
print(reshaped_a5)
print(reshaped_a5.ndim)
print(reshaped_a5.shape)

print("*" * 50)

reshaped_a5 = a5.reshape(2, 5, 2)
print(reshaped_a5)
print(reshaped_a5.ndim)
print(reshaped_a5.shape)


print("-" * 50)
