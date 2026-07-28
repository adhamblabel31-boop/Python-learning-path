# -------------------------------------------------
#! ------ compare performance and memory use ------
# -------------------------------------------------
# ? performance
# ? memory use
# -------------------------------------------------

import numpy as np
import time
import sys

elements = 200000

l1 = range(elements)
l2 = range(elements)

a1 = np.arange(elements)
a2 = np.arange(elements)

list_time = time.time()
list_combination = [n1 + n2 for n1, n2 in zip(l1, l2)]
# print(list_combination)

print(f"list time: {time.time()-list_time } seconds")
# for n1, n2 in zip(l1, l2):
#     print(n1 + n2)

array_time = time.time()
array_combination = a1 + a2
# print(array_combination)

print(f"array time: { time.time()-array_time } seconds")

a = np.array(range(100))
print(a)
print(a.itemsize)
print(a.size)
print(f"memory use: {a.size * a.itemsize} bytes")

print("-" * 50)

l = list(range(100))
print(l)
print(sys.getsizeof(1))
print(len(l))
print(f"memory use: {sys.getsizeof(1) * len(l)} bytes")
