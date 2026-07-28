# ----------------------------------------------------
# ! --------- instance attributes and methods --------
# ----------------------------------------------------
# ? self                : point to instance created from class
# ? instance attributes : instance attributes defined inside the constructor
# ----------------------------------------------------
# ? instance methods: take self parameter which point to instance created from class
# ? instance methods can have more than one parameter like any function
# ? instance methods can freely access attributes and methods on the same object
# ? instance methods can access the class itself
# ----------------------------------------------------
# ? class attributes : attributes defined outside the constructor

# ----------------------------------------------------
# ! --------- class methods & static methods ---------
# ----------------------------------------------------
# todo# class methods:
# ? [1] marked with "@classmethod" decorator to flag it as class method
# ? [2] it take "cls" parmeter not self to point to the clss not the instance
# ? [3] it doesn't require creation of a class instance
# ? [4] used when you want to do something with the class itself
# todo# static methods:
# ? [1] marked with "@staticmethod" decorator to flag it as class method
# ? [2] it takes no parameter
# ? [3] its bound to the class not instance
# ? [4] used when doing something doesn't have access to object or class but related to class
# ----------------------------------------------------


import Adham

print(Adham.deco("Adham"))


class Adham:
    allowedName = ["Adham", "adham", "ADHAM"]
    users = 0

    # constructor
    def __init__(self, fName, mName, lName):
        self.fname = fName
        self.mname = mName
        self.lname = lName
        Adham.users += 1

    @classmethod
    def userCount(cls):
        print(f"there is {cls.users} users in the program")

    @staticmethod
    def hello():
        print(f"static method")

    def fullName(self):
        if self.fname not in Adham.allowedName:
            raise ValueError("name is not allowed , baaaaka")
        else:
            return f"{self.fname} {self.mname} {self.lname}"

    def welcome(self):
        if self.fname.startswith("a"):
            return f"hello eng {self.fname}"
        elif self.fname.startswith("Ad"):
            return f"Hello Eng {self.fname}"
        else:
            return f"HELLO ENG {self.fname}"

    def deco(self):
        print("-" * 50)
        print(self.fname.center(50, "-"))
        print("-" * 50)

    def deleteUsers(self):
        Adham.users -= 1
        return f"user {self.fname} is deleted"


print(Adham.users)

ob1 = Adham("adham", "yasser", "abo blabel")
ob2 = Adham("Adham", "Yasser", "Abo Blabel")
ob3 = Adham("ADHAM", "YASSER", "ABO BLABEL")

ob4 = Adham("Ahmed", "Yasser", "Abo Blabel")

print(Adham.users)
# print(dir(ob1.name))
print(ob4.deleteUsers())
print(Adham.users)

print(ob1.fname, ob1.mname, ob1.lname)
print(ob2.fname, ob2.mname, ob2.lname)
print(ob3.fname, ob3.mname, ob3.lname)

print(ob2.fullName())

print(ob1.welcome())
print(ob2.welcome())
print(ob3.welcome())

print(ob2.deco())

# print(ob4.fullName())

Adham.userCount()

# print(ob1.fullName()) = print(Adham.fullName(ob1))

Adham.hello()
