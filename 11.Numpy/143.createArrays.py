# -----------------------------------
# ! --------- create arrays ---------
# -----------------------------------

import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("-" * 50)

# type
print(type(my_list))
print(type(my_array))

print("-" * 50)

# accessing
print(my_list[0])
print(my_array[0])

print("-" * 50)


a = np.array(10)
b = np.array([10, 20])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(d[1, 1, 1]) # 8

print("-" * 50)

# number of dimensions
print(a.ndim) # 0
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3

print("-" * 50)

# custom dimensions
my_custom_array = np.array([1, 2, 3], ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim) # 3
print(my_custom_array[0,0,0]) # 1

print("-" * 50)





