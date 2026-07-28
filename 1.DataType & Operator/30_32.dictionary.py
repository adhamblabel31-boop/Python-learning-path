# ----------------------------------------------------
#! dictionary
# ----------------------------------------------------
# ? [1] assign in curly brackets --> {key:value}
# ? [2] dicy key has only immutable data type --> (numbers , strings , tuple) not list , dict
# ? [3] dict value can have any data types
# ? [4] dict key is unique --> can not repeat itemes --> take last value
# ? [5] not ordered access its element with key
# ----------------------------------------------------
theDict = {
        "name": "adham",
        "age": 18
}
print(theDict)
print(theDict["name"])
print(theDict.get("name"))

print(theDict.keys())
print(theDict.values())

#todo# two-dimensional dictionary

school1={
    1:{
        "name":"adham",
        "age":18,
        "lenght":175
    },
    2:{
        "name":"AYAB",
        "age":20,
        "lenght":160
    }
}
print(school1)
print(school1[1]["name"])
print(len(school1))
print(len(school1[1]))

one={
    "name":"adham",
    "age":18,
    "lenght":175
}
two={
    "name":"AYAB",
    "age":20,
    "lenght":160
}
school2={
    1:one,
    2:two
}
print(school2)
print(school2[1]["name"])

# ----------------------------------------------------
#! dictionary methods
# ----------------------------------------------------
# ? clear()      --> remove all element of the dict
# ? copy()       --> copy the dict
# ? update()     --> update or add new key:value to the dict
# ? setdefault() --> if key not exist add key:value else return value of the key
# ? popitem()    --> return last key:value and remove it from the dict
# ? items()      --> make tuples each of key:value and put all tuples in a list
# ? fromkeys()   --> create dict from list or tuple with same value for each key
# ----------------------------------------------------
myDict = {
    "name": "adham",
    "age": 18
}
myDict.clear()
print(myDict)

myDict = {
    "name": "adham",
    "age": 18
}
newDict = myDict.copy() 
print(newDict)

myDict = {
    "name": "adham",
    "age": 18
}
myDict.update({"age": 19, "lenght": 175})
print(myDict)

myDict = {
    "name": "adham",
    "age": 18
}
print(myDict.setdefault("name", "AYAB"))
print(myDict.setdefault("lenght", 175))
print(myDict)

myDict = {
    "name": "adham",
    "age": 18
}
print(myDict.popitem())
print(myDict)

myDict = {
    "name": "adham",
    "age": 18,
    "lenght": 175,
    "weight": 70
}
myDict["man"]= True
print(myDict.items())

k = ("name", "age", "lenght")
v = "unknown"
newDict = dict.fromkeys(k, v)
print(newDict)