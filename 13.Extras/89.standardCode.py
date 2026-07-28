# ----------------------------------------------------
# ! ------------ pylint for standard code ------------
# ----------------------------------------------------
# ? [1] in the end should be new line
# ? [2] file name should be in snake case
# ? [3] function name should be in snake case
# ? [4] function should contain documentation
# ? [5] file should contain documentation
# ----------------------------------------------------
# todo# in command line --> pylint.exe "file address"

"""installing pylint"""


def say_welcome(name):
    """greating me"""
    msg = "is the best"
    print(f"{name} {msg}")


say_welcome("Adham")
