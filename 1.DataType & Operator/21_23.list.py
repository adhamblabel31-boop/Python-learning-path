# ----------------------------------------------------
#! list
# ----------------------------------------------------
# ? [1] assign in square brackets --> []
# ? [2] ordered                   --> zero indexing
# ? [3] mutable                   --> add , edit , delete
# ? [4] list item is not unique   --> can repeat itemes
# ? [5] can assign different data types
# ----------------------------------------------------
theList = ["adham", 9, "dragon", 99, True]

print(theList)
print(theList[0])
print(theList[-1])
print(theList[1:3])
print(theList[1::3])

theList[1] = 999
print(theList)

theList[1:3] = [999]
print(theList)

# ----------------------------------------------------
#! list methods
# ----------------------------------------------------
# ? append()  --> add value to the end of the list
# ? extend()  --> mix two list in one list
# ? remove()  --> delete the first value of the element from the list
# ? sort()    --> arrange intger only or string only element decending if reverse=false & acending if reverse=true --> list name.sort(reverse=true or false) by default false
# ? reverse() --> reverse element of list
# ? clear()   --> remove all element of list
# ? copy()    --> copy the list
# ? count()   --> count how many value of element appear
# ? index()   --> show in where index is the element exist
# ? insert()  --> add value before index                    --> list name.insert(index,value)
# ? pop()     --> remove all element and retern index value --> print(pop(index))
# ? pop()     --> remove element index value                --> pop(index)

newList = ["Adham", 9, "eng", True]
print(newList)

newList.append(False)
print(newList)

newList.append(theList)
print(newList)
print(newList[5])  # ? the list -->  because it add to the list as one element

# todo# you can reach to element in the append list by write index of the main list between index of the sub list
print(newList[5][0])

a = [1, 2, 3, 4, 5]
b = ["a", "a", "b", "c", "d", "e"]
a.extend(b)
print(a)

a.remove("a")
print(a)

c = [-1, 5, 1, 7, 99, 20, -8, 2, 5]
c.sort()
print(c)

d = ["z", "d", "e", "u", "o", "w"]

d.reverse()
print(d)

d.sort()
print(d)

x = [1, 5, 88, 4, 4, 6, 7, 4, 54, 1, 8, 7, 45, 9, 63, 21, 222, 4, 555, 9, 87, 5, 7]
x.clear()
print(x)

x = [1, 5, 88, 4, 4, 6, 7, 4, 54, 1, 8, 7, 45, 9, 63, 222, 4, 555, 9, 87, 5, 7]
y = x.copy()
print(y)

print(x.count(7))

print(x.index(88))

x.insert(-2, "adham")
print(x)

x.pop(-3)
print(x)
