# ----------------------------------------------------
#!----------------- lmbda function  ------------------
#!--------------- anonymous function -----------------
# ----------------------------------------------------
# ? [1] it has no name
# ? [2] can call it inline without defining it
# ? [3] can use it in return data fron another function
# ? [4] used for simple functions and def hamdle the large tasks
# ? [5] is one single expression not block of code
# ? [6] lambda type is function
# ----------------------------------------------------
# normal function
def Name(name,age) : return f"Hi , {name} | your age is : {age}"
print(Name("Adham",18))


# lambda function
lName = lambda name,age : f"Hi , {name} | your age is : {age}"
# name= lambda parametar task
print(lName("Adham",18))