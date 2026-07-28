# ------------------------------------------
# ! ---- compare data location and type ----
# ------------------------------------------

import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])

print("-" * 50)

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

print("-" * 50)

lsod = [20, 15,"A", True, 10.55, "Adham", "B"]
arod = np.array([20, 15,"A", True, 10.55, "Adham", "B"])

print(lsod)
print(arod)

print("-" * 50)

print(lsod[0])
print(arod[0])

print(type(lsod[0]))
print(type(arod[0]))

print("-" * 50)

lsod2 = [20, 15,"A", True, 10.55, "Adham", "B"]
arod2 = np.array([20, 15])

print(lsod)
print(arod)

print("-" * 50)

print(lsod2[0])
print(arod2[0])

print(type(lsod2[0]))
print(type(arod2[0]))
