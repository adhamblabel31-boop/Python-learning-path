# ----------------------------------------------------
# ! ----------------- encapsulation ------------------
# ----------------------------------------------------
# ? encapsulation --> restrict access to the data stored in attributed and methods
# ? attributes = variable = properties
# todo # public
# ? [1] every attribute and method that we used so far is public
# ? [2] attributes and methods can be modified and run from everywhere
# ? [3] inside our outside the class
# todo # private
# ? [1] attributes and methods can be accessed from within the class or object only
# ? [2] attributes can't be modified from outside the class
# ? [3] attributes and methods prefixed with two underscores "__"
# todo # protected
# ? [1] attributes and methods can be accessed from within the class and sub classes
# ? [2] attributes and methods prefixed with one underscore "_"
# ----------------------------------------------------
print("public")

class member1:
    def __init__(self, name):
        self.name = name


ob1 = member1("Adham")
print(ob1.name)

ob1.name = "adham"
print(ob1.name)

print("----"*15)
# ----------------------------------------------------

print("private")

class member3:
    def __init__(self, name):
        self.__name = name

    def welcome(self):
        return f"Hello, {self.__name} "


ob3 = member3("Adham")
print(ob3.welcome())

# ob3.__name = "adham"
# print(ob3.__name) #error

print(ob3._member3__name)

print("----"*15)
# ----------------------------------------------------
print("protected")

class member2:
    def __init__(self, name):
        self._name = name


ob2 = member2("Adham")
print(ob2._name)

ob2._name = "adham"
print(ob2._name)

