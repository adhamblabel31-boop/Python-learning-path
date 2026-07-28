# ----------------------------------------------------
#!--------------------- range ------------------------
# ----------------------------------------------------
rang = range(1, 11)
for i in rang:
    print(i)
# ----------------------------------------------------
#! ---------------- print dict loop ------------------
# ----------------------------------------------------
info = {
    "name": "adham",
    "age": 18,
    "faculty": "computer and information"
    }

for inf in info:
    print(inf)  # print key only

for inf in info:
    print(info[inf])  # print value only

for inf in info:
    print(f"{inf} : {info[inf]}")  # print value and key