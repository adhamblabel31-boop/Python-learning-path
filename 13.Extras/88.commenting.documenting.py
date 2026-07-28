# ----------------------------------------------------
# ! ----------- commenting vs documenting ------------
# ----------------------------------------------------
# ? [1] documentation string for class , module or function
# ? [2] can be accessed from the help and doc attributes
# ? [3] made for understanding the functionality of the complex code
# ? [4] there are one line and multiple line doc strings
# ? [5] document can be define by single or double quotation
# ----------------------------------------------------
def adham(name):
    """this function is to welcome me"""  # document single
    print(f"Hi , {name}")


def adham1(name):
    """
    this function is to welcome me
    take parameter name
    welcome user when send his name
    """  # document multiple
    print(f"Hi , {name}")


adham("Adham")
print(dir(adham))
print(adham.__doc__)  # print the document
help(adham)

print("-----" * 15)

adham1("Adham")
print(dir(adham1))
print(adham1.__doc__)  # print the document
help(adham1)
