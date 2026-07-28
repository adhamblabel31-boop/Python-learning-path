# ----------------------------------------------------
# ! ------------- @property decorator ----------------
# ----------------------------------------------------


class member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        return f"Hello, {self.name}"

    @property
    def age_day(self):
        return f"{self.age * 365.25} days"


ob = member("Adham", 18)

print(ob.name)
print(ob.age)

print(ob.welcome())

print(ob.age_day)
# print(ob.age_day()) # error
