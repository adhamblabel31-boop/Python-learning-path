# ----------------------------------------------------
#! boolean
# ? use to check some thing
# ? true or false
# ----------------------------------------------------

print(100 > 200)
print(100 < 200)

# ----------------------------------------------------
#! true when :
# ----------------------------------------------------
# ? [1] string but not empty
# ? [2] numbers but not 0
# ? [3] list , tuple , dict , set but not empty
# ----------------------------------------------------

print(bool("adham"))
print(bool(100))
print(bool([1, 2, 3]))

# ----------------------------------------------------
#! false when :
# ----------------------------------------------------
# ? [1] empty string
# ? [2] number 0
# ? [3] empty list , tuple , dict , set
# ? [4] none
# ----------------------------------------------------

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))

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
