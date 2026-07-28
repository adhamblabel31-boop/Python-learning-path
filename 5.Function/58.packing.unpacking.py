# ----------------------------------------------------
#!---------- packing , unpacking argument ------------
# ----------------------------------------------------
print(1, 2, 3, 4, 5)
num = [1, 2, 3, 4, 5]
print(num)  # print list as bulk
print(*num)  # print element of list


# ? packing --> when you know number of parameter
def wel1(name1, name2, name3):
    print(f"Hi, {name1}")
    print(f"Hi, {name2}")
    print(f"Hi, {name3}")


wel1("adham", "Adham", "ADHAM")
# wel("adham","Adham","ADHAM", "Ahmed") error --> only 3 parametar

print("-" * 30)


# ? unpacking --> when you don't know number of parameter
def wel2(*name):  # argument become a tupple
    print(type(name))  # tupple
    for n in name:
        print(f"Hi, {n}")


wel2("adham", "Adham", "ADHAM", "Ahmed")

tuppleName = ("adham", "Adham", "ADHAM")
wel2(tuppleName)  # will taking a tupple as one argument
wel2(*tuppleName)  # will taking tupple's element
