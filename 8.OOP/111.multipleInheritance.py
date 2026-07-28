# ----------------------------------------------------
# ! ------------- multiple inheritance ---------------
# ----------------------------------------------------
class base1:
    def __init__(self):
        print("Adham in base one")

    def func1(self):
        print("Adham in function one")


class base2:
    def __init__(self):
        print("Adham in base two")

    def func2(self):
        print("Adham in function two")


class derived(base1, base2):
    pass


postion = derived()

# print(derived.mro())

print(postion.func1)
print(postion.func2)

postion.func1()
postion.func2()

# ----------------------------------------------------


class base:
    pass


class derived1(base):
    pass


class derived2(derived1):
    pass
