# ----------------------------------------------------
#!----------------- Built in modules -----------------
# ----------------------------------------------------
# ? [1] it is a file that contains a set of functions to perform specific tasks.
# ? [2] you can import a module in your app to help you
# ? [3] you can import multiple modules in a single app.
# ? [4] you can create your own modules.
# ? [5] it saves your time and effort.
# ----------------------------------------------------

# import main module
import random

# print(random)
print(f"random float number between 0 and 1: {random.random()}")
#                                            module.function() --> when you import the main module

# show all functions and attributes inside module
print(dir(random))

print("-----" * 15)

# import specific function from module
from random import randint, random  # or * --> all functions

print(f"random integer number between 1 and 100: {randint(1, 100)}")
#                                                function() --> when you import specific function from module
print(f"random float number between 0 and 1: {random()}")

print("*****" * 15)

# ----------------------------------------------------
# ! -------------- create your module ----------------
# ----------------------------------------------------
# ? create new file to build your module

# import sys
# print(sys.path)  # to show the paths that python search for modules in it
# sys.path.append(r"C:\Users\Adham\GitHub\Python-learning-path\5.Function")  # to add new path to search for modules in it
# print(sys.path)

import Adham as A  # import your module

print(dir(A))  # show all functions and attributes inside your module

print(A.welcome("Adham"))
print(A.deco("Adham"))

from Adham import deco as d  # import specific function from your module

print(d("Adham"))

print("*****" * 15)

# ----------------------------------------------------
# ! ------------ install external packages -----------
# ----------------------------------------------------
# ? [1] module vs package --> package contains group of modules
# ? [2] External packages downloaded from internet to help you in your app.
# ? [3] you can install external packages using pip (package installer for python).
# ? [4] PIP install the package and its dependencies.
# ? [5] modules list "https://docs.python.org/3/py-modindex.html"
# ? [6] packages list "https://pypi.org/"
# ? [7] PIP manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ----------------------------------------------------
# pip install "module name"

import termcolor
import pyfiglet

print(pyfiglet.figlet_format("Adham"))
print(termcolor.colored("Adham", color="magenta", on_color="on_black"))
print(termcolor.colored(pyfiglet.figlet_format("Adham"), color="cyan", on_color="on_black"))