# ----------------------------------------------------
# ! ----------------- decoration ---------------------
# ----------------------------------------------------
# ? [1] sometimes called meta progrmming
# ? [2] everything in python is object even functions
# ? [3] it takes a function and add some functionality and return it
# ? [4] it wrap other function and enhance their behaviour
# ? [5] it is higher order function (function accept function as parameter)
# ----------------------------------------------------
def myDecorator(func):
    def nestFunc():
        print("Adham")
        func()
        print("Adham")

    return nestFunc


@myDecorator
def welcome():
    print("Adham")


welcome()

# deco=myDecorator(welcome)

# deco()

print("*****" * 15)


# ----------------------------------------------------
def myDecorator1(func):
    def nestFunc(*nums):
        print("Adham")
        func(*nums)
        print("Adham")

    return nestFunc


def myDecorator2(func):
    def nestFunc(num1, num2):
        print("Adham")
        func(num1, num2)
        print("Adham")

    return nestFunc


@myDecorator1
# @myDecorator2
def add(n1, n2, n3):
    print(n1 + n2 + n3)


add(5, 2, 5)

print("*****" * 15)

# ----------------------------------------------------
from time import time


def speedFunc(func):
    def rang():
        start = time()
        func()
        end = time()
        print(f"func takes : {end-start}")

    return rang


@speedFunc
def name():
    print("Adahm")


name()


@speedFunc
def count():
    for n in range(1, 10):
        print(n)


count()
