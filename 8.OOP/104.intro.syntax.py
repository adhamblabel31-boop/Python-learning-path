# ----------------------------------------------------
# ! -------------------- OOP -------------------------
# ----------------------------------------------------
# ? [01] python support object oriented programming
# ? [02] OOP is a paradigm or coding style
# ? [03] paradigm   --> means structuring program so the methods[functions] and attributes[data] are bendled into object
# ? [04] methods    --> act as function that use the information of the object
# ? [06] procedural --> structure app like recipe , sets of steps to make the task
# ? [07] functional --> built on the concept of mathematical functoins
# ? [05] python is multi-paradigm programming languafe [procedural, OOP, functional]
# ? [08] OOP allows to organize the code and make it readable and reusable
# ? [09] everything in python is object
# ? [10] OOP --> attributes and methods

# ----------------------------------------------------
# ! ------------------- OOP syntax -------------------
# ----------------------------------------------------
# ? [01] class is the blueprint or constructor of the object
# ? [02] class instantiate means create instance of a class
# ? [03] instance --> object created from class and have their methods and attributes
# ? [04] class defined with keyword "class"
# ? [05] class name written with pascalcase style
# ? [06] class may contains methods and attributes
# ? [07] when creating object python look for the built in __init__ method
# ? [08] __init__ method called every time you create object from class
# ? [09] __init__ method is initialize the data for the object
# ? [10] any method with two underscore in the start and end called "dunder" or "magic mehtod"
# ? [11] self refer to the current instance created from the class and must be first param
# ? [12] self can be named anything
# ? [13] in python you don't need to call new() keyword to create object
# ----------------------------------------------------
# todo# class Name:
# todo#      constructor --> do instantiation [ create instance from a class ]
# todo#      each instance is separate object
# todo#      def __init__ (self , other data)
# todo#          body of function
# ----------------------------------------------------


class Adham:
    def __init__(self):
        print("Adham is the best")


Adham()
Adham()
Adham()

ob1 = Adham()
print(ob1.__class__)
