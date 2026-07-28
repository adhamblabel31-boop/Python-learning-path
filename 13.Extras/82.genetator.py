# ----------------------------------------------------
# ! ------------------ generator ---------------------
# ----------------------------------------------------
# ? [1] generator is a function with "yield" keyWord instead of "return"
# ? [2] it support iteration and return generator iterator by calling "yield"
# ? [3] generator function can have one or more "yield"
# ? [4] by using next() it resume from where it called "yiled" not from begining
# ? [5] when call, its not start automatically , its only give you the control
# ----------------------------------------------------


def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


print(type(myGenerator()))

myGen = myGenerator()
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))

# for n in myGen:
#     print(n)
