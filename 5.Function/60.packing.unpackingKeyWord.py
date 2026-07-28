# ----------------------------------------------------
#!------ packing , unpacking key word argument -------
# ----------------------------------------------------
# ? unpacking
def wel2(**name):  # argument become a dictionary
    print(type(name))  # dictionary
    for n, m in name.items():
        print(f"{n} --> {m}")


dictName = {
    "name": "adham",
    "name2": "Adham",
    "name3": "ADHAM"
    }

wel2(**dictName)  # pritn elements of dictionary
wel2(name="adham", name2="Adham", name3="ADHAM")

print(dictName)  # print key only
print(*dictName)  # print key and value as a bulk
