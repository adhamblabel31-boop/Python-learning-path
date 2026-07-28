# ----------------------------------------------------
# ! ------------ iterator vs iterator ----------------
# ----------------------------------------------------
# todo# iterable
# ? [1] object contains data that can be iterated upon
# ? [2] such as (string , list , set , tuple , dictonary)
# ----------------------------------------------------
# todo# iterator
# ? [1] object used to iterate over iterable using next() method return 1 element at a time
# ? [2] you can generate iterator from iterable from iterable when using iter () method
# ? [3] for loop already calls iter() method on the iterable behind the scene
# ? [4] gives " StopIteration" if theres no next element
# ----------------------------------------------------
name = "Adham"
for let in name:
    print(let, end="")
print()


iterName = iter(name)
print(next(iterName), end="")
print(next(iterName), end="")
print(next(iterName), end="")
print(next(iterName), end="")
print(next(iterName))
