# ------------------------------------------------
# ! -------- data types and control array --------
# ------------------------------------------------
# * https://numpy.org/devdocs/user/basics.types.html
# * https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# ? '?' boolean
# ? 'b' (signed) byte
# ? 'B' unsigned byte
# ? 'i' (signed) integer
# ? 'u' unsigned integer
# ? 'f' floating-point
# ? 'c' complex-floating point
# ? 'm' timedelta
# ? 'M' datetime
# ? 'O' (Python) objects
# ? 'S', 'a' zero-terminated bytes (not recommended)
# ? 'U' Unicode string
# ? 'V' raw data (void)
# ------------------------------------------------

import numpy as np

# show array data type

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
a3 = np.array(["a", "b", "c", "d", "e"])
a4 = np.array(["Adham", "Yasser", "Ahmed"])

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
print(a4.dtype)

print("-" * 50)

# create array with specific data type

a5 = np.array([1, 2, 3, 4, 5], dtype=float)          # --> float , "float" , "f"
a6 = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=int)  # --> int   , "int"   , "i"
# a7 = np.array(["Osama_Elzero", "B", "Ahmed"], dtype=int) # Value Error

print(a5.dtype)
print(a6.dtype)
# print(a7.dtype)

print("-" * 50)

# change data type of existing array

a8 = np.array([0, 1, 2, 3, 0, 4])
print(a8.dtype)
print(a8)

print("-" * 50)

a8 = a8.astype("float")
print(a8.dtype)
print(a8)

print("-" * 50)

a8 = a8.astype("bool")
print(a8.dtype)
print(a8)

print("-" * 50)

# test capacity

a9 = np.array([100, 200, 300, 400], dtype="f")
print(a9.dtype)
print(a9[0].itemsize)  # 4 Bytes

a9 = a9.astype("float")  # change to Float64
print(a9.dtype)
print(a9[0].itemsize)  # 8 Bytes
