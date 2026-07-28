# ----------------------------------------------------
# ! ------------ regular expressions -----------------
# ----------------------------------------------------
# ? [1] sequence of characters that define a search pattern
# ? [2] regular expression is not in python its general concept
# ? [3] used in [credit card validatoin, IP address validation, email validaton]
# ? [4] test regEx "https://pythex.org/"
# ? [5] characters sheet "https://www.debuggex.com/cheatsheet/regex/python"
# ? [6] https://regex101.com/

# ----------------------------------------------------
# ! ----------------- quantifiers --------------------
# ----------------------------------------------------
# ?| "*"   --> 0 or more
# ?| "+"   --> 1 or more
# ?| "?"   --> 0 or 1
# ?| {x}   --> exactly x
# ?| {x,y} --> between x , y
# ?| {x,}  --> x or more
# ?| {,y}  --> up to y

# ----------------------------------------------------
# ! ----------------- characters ---------------------
# ----------------------------------------------------
# ?| [0-9]
# ?| [^0-9]
# ?| [A-Z]
# ?| [^A-Z]
# ?| [a-z]
# ?| [^a-z]

# ----------------------------------------------------
# ! ----------------- assertions ---------------------
# ----------------------------------------------------
# ?| "^" --> start of string
# ?| "$" --> end of string
# todo# match email
# todo# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# todo# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|etc)+$

# ----------------------------------------------------
# ! ------------------- logical ----------------------
# ----------------------------------------------------
# ? "|"  --> or
# ? "\"  --> escape special characters
# ? "()" --> separate groups
# todo# (\d-|\d\)|\d>) (\w+)
# todo# match web
# todo# ^(https?://)(www\.)?(\w+)\.(net|com|info)$

# ----------------------------------------------------
# ! ------------------ re module ---------------------
# ----------------------------------------------------
# ? search()  --> search a string for a match and return a first match only
# ? findAll() --> returns a list of all matches and empty list if no match
# ----------------------------------------------------


import re

capital = re.search(r"[A-Z]", "AdhamYasserBlabel")
print(capital)
print(capital.span())  # postion
print(capital.string)  # text
print(capital.group())  # match

print("----" * 15)

checkEmail = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.com|net|etc+$", "adhamblabel31@gmail.com")

print(checkEmail.span())  # postion
print(checkEmail.string)  # text
print(checkEmail.group())  # match

if checkEmail:
    print("Valid")
else:
    print("InValid")

print("----" * 15)
print("----" * 15)

inEmail = input("enter your email : ")
checkEmail = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.com|net|etc+$", inEmail)

emList = []
if checkEmail != []:
    emList.append(checkEmail)
    print("email added")
else:
    print("invalid email")

for email in emList:
    print(email)

# ----------------------------------------------------
# ! ---------------- split and sub -------------------
# ----------------------------------------------------
# ? split(pattern, string, maxSplit)            --> return a list or elements splitted on each match
# ? sub(pattern, replace, string, replaceCount) --> replace matches with what you want
# ----------------------------------------------------

import re

name = "Adham Yasser Abo Blabel"

rename = re.split(r"\s", name, 2)
print(rename)

print("----" * 15)

name = "Adham-Yasser_Abo Blabel"
rename = re.split(r"-|_", name)
print(rename)

print("----" * 15)

for n in enumerate(rename, 1):
    print(n)

print("----" * 15)

print(re.sub(r"-|_", " ", name))

print("****" * 15)
# ----------------------------------------------------

web = "https://www.adham.me:9999/name.php?name=hello"
reweb = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?(.+)", web)
#? re.M --> multiline   --> take all line ----------------------------^
#? re.I --> ignore case --> don't care if high or low case
#? re.D --> DoTall      --> match every thing


print(reweb.group)
print(reweb.groups)

for group in reweb.groups():
    print(group)
