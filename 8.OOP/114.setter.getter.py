# ----------------------------------------------------
# ! --------------- getter & setter ------------------
# ----------------------------------------------------


class member:
    def __init__(self, name):
        self.__name = name

    def welcome(self):
        return f"Hello, {self.__name}"

    def setName(self, newName): # setter
        self.__name = newName

    def getName(self):  # getter
        return self.__name


ob1 = member("Adham")
print(ob1.getName())

ob1.setName("adham")
print(ob1.getName())
