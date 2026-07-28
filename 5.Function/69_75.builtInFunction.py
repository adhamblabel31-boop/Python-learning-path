# ----------------------------------------------------
#! ------------- built-in functions ------------------
# ----------------------------------------------------
# ? [1]  all(iterable)                               --> Returns True if all elements of the iterable are true (or if the iterable is empty).
# ? [2]  any(iterable)                               --> Returns True if any element of the iterable is true. If the iterable is empty, returns False.
# ? [3]  bin(x)                                      --> Converts an integer number to a binary string prefixed with "0b".
# ? [4]  id(object)                                  --> Returns the identity of an object. This is an integer which is unique and constant for this object during its lifetime.
# ? [5]  sum(iterable, /, start=0)                   --> Sums start and the items of an iterable from left to right and returns the total.
# ? [6]  round(number , num of digits)               --> Rounds a floating point number to a specified number of digits.
# ? [7]  range(start, stop, step)                    --> Generates a sequence of numbers from start to stop (exclusive) by step.
# ? [8]  print(....)                                 --> Prints the given object to the standard output device  separated by space --> "sep" and followed by a newline --> "end".
# ? [9]  abs(x)                                      --> Returns the absolute value of a number.
# ? [10] pow(x, y[, z])                              --> Returns x to the power y; if z is present, returns x to the power y, modulo z.
# ? [11] min(iterable, *[, default=obj, key=func])   --> Returns the smallest item in an iterable or the smallest of two or more arguments.
# ? [12] max(iterable, *[, default=obj, key=func])   --> Returns the largest item in an iterable or the largest of two or more arguments.
# ? [12] slice(start, stop, step)                    --> Returns a slice object representing the set of indices specified by range(start, stop, step).
# ? [13] enumerate(iterable, start=0)                --> Returns an enumerate object. It contains the index and value of all items in the iterable as pairs.
# ? [14] help(object)                                --> Invokes the built-in help system.
# ? [15] reverse(iterable)                           --> Returns a reverse iterator.
# ? more...                                          --> https://docs.python.org/3/library/functions.html
# ----------------------------------------------------
# todo# iterable --> list, tuple, set, dict, string
# ----------------------------------------------------
# ? All

myList = [0, 1, 2, 3, 4, 5]
if all(myList):
    print("All elements are true")
else:
    print("at least one element is false")

print("----" * 15)
# ------------------------------------------------------
# ?Any

if any(myList):
    print("at least one element is true")
else:
    print("All elements are false")

print("----" * 15)
# ------------------------------------------------------
# ? Bin

num = 10
print(f"The binary representation of {num} is {bin(num)}")

print("----" * 15)
# ------------------------------------------------------
# ? Id

a = "Adham"
b = "ADHAM"
print(f"The id of a is {id(a)}")
print(f"The id of b is {id(b)}")

print("----" * 15)
# ----------------------------------------------------
# ? Sum

numbers = [1, 2, 3, 4, 5]
print(f"The sum of numbers is {sum(numbers)}")

print("----" * 15)
# ----------------------------------------------------
# ? Round

num = 5.6789
print(f"The rounded value of {num} is {round(num, 2)}")

print("----" * 15)
# ----------------------------------------------------
# ? Range
print(list(range(10)))  # 0 to 9

print(list(range(1, 11, 2)))  # odd
print(list(range(0, 11, 2)))  # even
# range(start --> "0" , stop --> "required" , step --> "1")

print("----" * 15)
# ----------------------------------------------------
# ? Print

print("Adham is the best")
print("Adham", "is", "the", "best", sep=" | ")

print("Adham", end=" *** ")
print("is the best")

print("----" * 15)
# ----------------------------------------------------
# ? Abs

num = -10
print(f"The absolute value of {num} is {abs(num)}")

print("----" * 15)
# ----------------------------------------------------
# ? Pow

print(pow(2, 5))  # 2*2*2*2*2 = 32
print(pow(2, 5, 3))  # (2*2*2*2*2) % 3 = 32 % 3 = 2

print("----" * 15)
# ----------------------------------------------------
# ? Min / Max

numbers = [1, 2, 3, 4, 5]
print(f"The minimum value is {min(numbers)}")
print(f"The maximum value is {max(numbers)}")

name = ["Adham", "f", "x", "yasser"]
print(f"The minimum character is {min(name)}")
print(f"The maximum character is {max(name)}")

print("----" * 15)
# ----------------------------------------------------
# ? Slice

numbers = [1, 2, 3, 4, 5]
print(numbers[slice(1, 4)])  # [2, 3, 4]
print(numbers[slice(0, 5, 2)])  # [1, 3 , 5]

print("----" * 15)
# ----------------------------------------------------
# ? enumerate

names = ["Adham", "Yasser", "Ahmed", "Mousa", "Abo Blabel"]
for index, name in enumerate(names):
    print(f"{index} => {name}")

print("----" * 15)
# ----------------------------------------------------
# ? help
# help(print)

print("----" * 15)
# ----------------------------------------------------
# ? reverse

names = "mahdA"
reversedNames = reversed(names)
for n in reversedNames:
    print(n)


print("****" * 15)


# ----------------------------------------------------
#! --------------------- map -------------------------
# ----------------------------------------------------
# ? [1] map take a function + iterator --> map(function, iterable, ...)
# ? [2] called with this bucause it map the function to all the items in the iterable
# ? [3] the function can be pre-defined or lambda function
# ----------------------------------------------------
def name(n):
    return f"- {n} -"


names = ["Adham", "Yasser", "Ahmed", "Mousa", "Abo Blabel"]

mappedNames = map(name, names)
# print(mappedNames) # --> <map object at "address">
for n in mappedNames:
    print(n)

print(list(mappedNames))


# ? using lambda function
mappedNames2 = map((lambda n: f"* {n} *"), names)
for n in mappedNames2:
    print(n)

print("****" * 15)


# ----------------------------------------------------
#! ------------------ filter -------------------------
# ----------------------------------------------------
# ? [1] filter take a function + iterator --> filter(function, iterable)
# ? [2] filter run a function on each item in the iterable and return only those items that the function return True for them
# ? [3] the function can be pre-defined or lambda function
# ? [4] filter out all items that the function return False for them
# ? [5] the function must return boolean value (True / False)
# ----------------------------------------------------
def filtNum(num):
    return num >= 9


numbers = [1, 3, 5, 7, 9, 11, 13, 15]
filteredNumbers = filter(filtNum, numbers)

for n in filteredNumbers:
    print(n)


def filtName(name):
    return name.startswith("A")


names = ["Adham", "Yasser", "Ahmed", "Mousa", "Abo Blabel"]
filteredNames = filter(filtName, names)
for n in filteredNames:
    print(n)


filteredNames2 = filter(lambda n: n.startswith("A"), names)
for n in filteredNames2:
    print(n)

print("****" * 15)
# ----------------------------------------------------
#! ------------------ reduce -------------------------
# ----------------------------------------------------
# ? [1] reduce take a function + iterator --> reduce(function, iterable)
# ? [2] reduce run a function on first two items in the iterable and return a single value
# ? [3] then it run the same function on the result and third item in the iterable
# ? [4] then it run the same function on the result and fourth and so on
# ? [5] till one element is left and this is the final result of reduce
# ? [6] the function can be pre-defined or lambda function
# ----------------------------------------------------
from functools import reduce


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]
reducedValue = reduce(add, numbers)
# ((1+2)+3)+4)+5 = 15
print(f"The reduced value is {reducedValue}")

reducedValue2 = reduce(lambda x, y: x + y, numbers)
print(f"The reduced value is {reducedValue2}")

print("****" * 15)
# ----------------------------------------------------
