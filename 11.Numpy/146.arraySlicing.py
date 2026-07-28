# ------------------------------------------------
#! ---------------- array slicing ----------------
# ------------------------------------------------
# ? slicing => [start:end:steps] not including end
# ------------------------------------------------

import numpy as np

a1 = np.array(["A", "D", "H", "A", "M"])
print(a1.ndim)
print(a1[0])
print(a1[0:3])
print(a1[1:4])

print("-" * 50)

a2 = np.array(
    [
        ["A", "D", "H", "A", "M"],
        ["Y", "A", "S", "E", "R"],
        ["A", "H", "M", "E", "D"],
        ["M", "O", "U", "S", "A"],
    ]
)
print(a2.ndim)
print(a2[0])
print("-" * 50)
print(a2[:2])
print("-" * 50)
print(a2[::,:1])
print("-" * 50)
print(a2[0:2,0:3:2 ])
