# ----------------------------------------------------
# ! ----------- Abstract Base Class => ABCs ----------
# ----------------------------------------------------
# ? [1] class called abstract class if it has one or more abstract methods
# ? [2] abc module in python provides infrastructure for defining custom abstract base classes
# ? [3] by adding @absttractmethod decorator on the methods
# ? [4] ABCMeta class is a metaclass used for defining abstrct base class
# ----------------------------------------------------
from abc import ABCMeta, abstractmethod


class programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

    @abstractmethod
    def has_name(self):
        pass

class python(programming):
    def has_oop(self):
        return "yes"

    def has_name(self):
        return "python"

class c(programming):
    def has_oop(self):
        return "no"

    def has_name(self):
        return "c"

# ob1 = programming()
# print(ob1.has_oop()) # error

ob2 = python()
print(ob2.has_oop())
print(ob2.has_name())

ob3 = c()
print(ob3.has_oop())
print(ob3.has_name())

