# ----------------------------------------------------
# ! ----------------- magic methods ------------------
# ----------------------------------------------------
# ? [1] every thing in python is an object
# ? [2] __init__       called automatically when instantiating class
# ? [3] self.__class__ the class to which a class instance belongs
# ? [4] __str__        gives a human-readable output of the object
# ? [5] __len__        returns the length of the container called when we use the built in len() function on the object
# ----------------------------------------------------
class skill:
    def __init__(self):
        self.skills = ["Adham", "adham", "ADHAM"]

    def __str__(self):
        return f"my name is {self.skills}"

    def __len__(self):
        return len(self.skills)


mySkills = skill()
print(mySkills)
print(mySkills.__class__)

name = "Adham"
print(type(name))
print(name.__class__)
# print(dir(str))
print(str.upper(name))

print(len(mySkills))

mySkills.skills.append("aDHAM")
mySkills.skills.append("adhaM")

print(len(mySkills))
