# ----------------------------------------------------
#! tuple
# ----------------------------------------------------
# ? [1] assign in parentheses    --> () or without it
# ? [2] ordered                  --> zero indexing
# ? [3] immutable                --> can not add , edit , delete
# ? [4] tuple item is not unique --> can repeat itemes
# ? [5] can assign different data types
# ? [6] operators used in strings and lists available in tuples
# ----------------------------------------------------
theTuple1 = ("adham", 1, 1.5, 99, -4, True, "dragon")
print(theTuple1)

theTuple2 = "adham", 1, 1, 1.5, 99, -4, True, "dragon"
print(theTuple2)
print(theTuple2[0])
print(theTuple2[0:3])

# theTuple1.append(5) #error

# todo# tuple with one element
a = (("adham"),)
b = ("Adham",)
print(a)
print(type(a))
print(type(b))

# todo# concatination
x = ("adham", "ayab", 1, 99, 9)
y = ("Adham", "AYAB", 5, 55, 9)
print(x + y)
print(x + ("ayamab", 5) + y)

# todo# repeat list, string , tuple
myTuple = (1, 2, 3, 4, 5)
myString = "adham "
myList = [5, 4, 3, 2, 1]
print(myTuple * 5)
print(myString * 5)
print(myList * 5)

# ----------------------------------------------------
#! tuple methods
# ----------------------------------------------------
# ? count()   --> count how many value of element appear   --> tuple name.count(value)
# ? index()   --> show in where index is the element exist --> tuple name.index(value)
# ----------------------------------------------------
g = ("adham", 5, 9, 8, 7, "adham")
print(g.count("adham"))
print(g.index(9))

# ----------------------------------------------------
#! tuple destruct
# ----------------------------------------------------
m = ("a", "b", "c")
x, y, z = m
print(x)
print(y)
print(z)

# ? put under score to skip value
m = (1, "a", 2, "b", 3, "c")
_, x, y, _, _, z = m
print(x)
print(y)
print(z)
