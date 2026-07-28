# ----------------------------------------------------
#! boolean operators
# ----------------------------------------------------
# ? and  --> all condition must be true to print true
# ? or   --> one condition must be true to print true
# ? not  --> reverse the result
# ----------------------------------------------------

print(100 > 50 and 200 > 100)  # true and true --> true
print(100 > 50 and 200 < 100)  # true and false --> false

print(100 < 50 or 200 > 100)  # false or true --> true
print(100 < 50 or 200 < 100)  # false or false --> false

print(not (100 > 50))  # not true --> false
print(not (100 < 50))  # not false --> true
# ----------------------------------------------------
#! arethmatic operator
# ----------------------------------------------------
# ? [+] addition
# ? [-] subtractoin
# ? [*] multiplication
# ? [/] division
# ? [%] modulas
# ? [**] exponent
# ? [//] floor division (remove numbers after point)
# ----------------------------------------------------
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)
print(10 % 2)
print(10**2)
print(10 // 2)

# ----------------------------------------------------
#! assignment operators
# ----------------------------------------------------
# ? =   --> assign value to variable
# ? +=  --> add and assign value to variable
# ? -=  --> subtract and assign value to variable
# ? *=  --> multiply and assign value to variable
# ? /=  --> divide and assign value to variable
# ? %=  --> modulus and assign value to variable
# ? //= --> floor division and assign value to variable
# ? **= --> exponent and assign value to variable
# ----------------------------------------------------

# todo# var1 = var1 [opperator] var2

a = 10
print(a)

a = 10
a += 2  # a = a + 2
print(a)

a = 10
a -= 2  # a = a - 2
print(a)

a = 10
a *= 2  # a = a * 2
print(a)

a = 10
a /= 2  # a = a / 2
print(a)

a = 10
a %= 2  # a = a % 2
print(a)

a = 10
a //= 2  # a = a // 2
print(a)

a = 10
a **= 2  # a = a ** 2
print(a)

# ----------------------------------------------------
#! comparison operators
# ----------------------------------------------------
# ? ==  --> equal
# ? !=  --> not equal
# ? >   --> greater than
# ? <   --> less than
# ? >=  --> greater than or equal
# ? <=  --> less than or equal
# ----------------------------------------------------
print(100 == 200)  # false
print(100 != 200)  # true
print(100 > 200)  # false
print(100 < 200)  # true
print(100 >= 200)  # false
print(100 <= 200)  # true

print("-" * 50)

# ----------------------------------------------------
#! type conversion --> casting
# ----------------------------------------------------
# ? int()    --> convert to integer
# ? float()  --> convert to float
# ? str()    --> convert to string
# ? list()   --> convert to list
# ? tuple()  --> convert to tuple
# ? set()    --> convert to set
# ? dict()   --> convert to dictionary
# ? bool()   --> convert to boolean
# ----------------------------------------------------
print("-" * 50)
# todo# converting str , tuple, set, dict to list

l = "Adham"  # str
t = ("A", "d", "h", "a", "m")  # tuple
s = {"A", "d", "h", "a", "m"}  # set
d = {1: "A", 2: "d", 3: "h", 4: "a", 5: "m"}  # dict

print(list(l))
print(list(t))
print(list(s))
print(list(d))

print("-" * 50)

# todo# converting str , list, set, dict to tuple
st = "Adham"  # str
l = ["A", "d", "h", "a", "m"]  # list
s = {"A", "d", "h", "a", "m"}  # set
d = {1: "A", 2: "d", 3: "h", 4: "a", 5: "m"}  # dict

print(tuple(st))
print(tuple(l))
print(tuple(s))
print(tuple(d))

print("-" * 50)

# todo# converting str , list, tuple, dict to set
st = "Adham"  # str
l = ["A", "d", "h", "a", "m"]  # list
t = ("A", "d", "h", "a", "m")  # tuple
d = {1: "A", 2: "d", 3: "h", 4: "a", 5: "m"}  # dict

print(set(st))
print(set(l))
print(set(t))
print(set(d))

print("-" * 50)

# todo# converting str , list, tuple, set to dict
st = "Adham"  # str
l = ["A", "d", "h", "a", "m"]  # list
t = ("A", "d", "h", "a", "m")  # tuple
s = {"A", "d", "h", "a", "m"}  # set

# print(dict(st)) error
# print(dict(l)) error
# print(dict(t)) error
# print(dict(s)) error

# ? correct way to convert to dict
# todo# first way
# * nested iterable
# * each nested iterable must have exactly two items
# todo# second way
# * using fromkeys() method

l = [[1, "A"], [2, "d"], [3, "h"], [4, "a"], [5, "m"]]  # list
t = ((1, "A"), (2, "d"), (3, "h"), (4, "a"), (5, "m"))  # tuple
s = {(1, "A"), (2, "d"), (3, "h"), (4, "a"), (5, "m")}  # set existing of tuples


print(dict(l))
print(dict(t))
print(dict(s))

print("-" * 50)

st = "Adham"  # str
l = ["A", "d", "h", "a", "m"]  # list
t = ("A", "d", "h", "a", "m")  # tuple
s = {"A", "d", "h", "a", "m"}  # set

print(dict.fromkeys(st))
print(dict.fromkeys(l))
print(dict.fromkeys(t))
print(dict.fromkeys(s))
