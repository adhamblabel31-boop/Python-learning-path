# ----------------------------------------------------
#! set
# ----------------------------------------------------
# ? [1] assign in curly bracket --> {}
# ? [2] items not order & not indexed
# ? [3] can not be slicing
# ? [4] has only immutable data type --> (numbers , strings , tuple) not list , dict
# ? [5] set item is unique --> can not repeat itemes
# ----------------------------------------------------
theSet = {"adham", "dragon", 2, 5, 7, 8, 9, 1.5, True}
print(theSet)  # not ordered
# print(theSet[0]) error
# print(theSet[0:3]) error

theSet = {"adham", "dragon", 2, 5, 7, 8, 9, 1.5, True, (1, 5, 6, 8, 7, 4)}
# theSet = {"adham", "dragon",2,5,7,8,9,1.5,True,[1,5,6,8,7,4]} error

theSet = {"adham", 9, 6, 5, 4, 1, 2, 3, 6, 5, 47, "adham", 8, 7}
print(theSet)  # print adham only one

# ----------------------------------------------------
#! set methods
# ----------------------------------------------------
# ? clear()                 --> remove all element of the set
# ? add()                   --> add one element to the set
# ? copy()                  --> copy the set
# ? remove()                --> delete value from the set if value not exist --> error
# ? discard()               --> delete value from the set if value not exist nothing happen
# ? pop()                   --> remove all element and retern random value -->print(pop())
# ? pop()                   --> remove random element  -->pop()
# ? update()                --> mix two sets or set with tuple or list or more
# ? union()                 --> mix two sets or more                                     --> (|)
# ? difference()            --> show what exist in set1 and not exist in set2            --> (-)
# ? intersection()          --> show what set1 and set2 subscribe                        --> (&)
# ? symetric_intersection() --> show what set1 and set2 subscribe --> union-intersection --> (^)
# ? issuperset()            --> check if all elements of set2 are exist in set1
# ? issubset()              --> check if all elements of set1 are exist in set2
# ? isdisjoint()            --> check if no element of set1 are exist in set2 and oppisite
# ----------------------------------------------------
newSet = {"adham", 1, 2, 3, 4, 5, "AYAB"}
print(len(newSet))
newSet.clear()
print(newSet)

x = {1, 2, 3}
y = {"one", "two", "three"}
z = {"adham", "AYAB", 9}

print(x | y)
print(x | y | z)
print(x.union(y))
print(x.union(y, z))

v = {1, 2, 3}
v.add(4)
v.add(5)
print(v)

m = {1, 2, 3}
f = m.copy()
print(f)

m.remove(2)
print(m)
# m.remove(4) error

p = {5, 6, 7, 8, 9}
p.discard(7)
print(p)

p.discard(4)  # not error
print(p)

p.pop()
print(p)
print(p.pop())

x = {1, 2, 3}
y = {"one", "two", "three"}
z = ("adham", "AYAB", 9)
r = ["adham", "AYAB", 9]

x.update(y, z)
print(x)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2)
print(set2 - set1)
print(set1)
print(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.symmetric_difference_update(set2))
print(set1.symmetric_difference(set2))
print(set1)
print(set1 ^ set2)

set1.difference_update(set2)
print("1", set1)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))
print(set1 & set2)

set1.intersection_update(set2)
print("1", set1)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5}
print(set1.issuperset(set2))

set1 = {4, 5}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {9, 10, 11}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
