# ----------------------------------------------------
#!---------------- concatination ---------------------
# ----------------------------------------------------
# ?connect between two or more stirng --> (+)
# ex:
a = "adham "
b = " yasser"
c = a + " " + b
print(a + " " + b)
print(c)

x = "1 \
2 \
3"

y = "a \
b \
c"
print(x + "\n" + y)
#!you cannot concatinate string and integer together
# todo-- print("hello" + 1)  # error

# ----------------------------------------------------

z = """
'a'
"d"
"h"
'a'
'm'\
"""
print(z)

z = """
'a'\\\
"d"\\\
"h"\\\
'a'\\\
"m"
"""
print(z)

print("'adham'")
print('"adahm"')

# ----------------------------------------------------
#!----------- strings indexing & slicing -------------
# ----------------------------------------------------
# ?[1] all data in python is object
# ?[2] object contain elements
# ?[3] every eliment has its own index (index start from zero)
# ?[4] python uses zero based indexing
# ?[5] use spuare brackets to access element []
# ?[6] enable accessing parts of strings , tuples or lists

# todo# indexing ( access single item )
# todo# print(variable[index])
ex = "Adham Yasser Abo Blabel"
# 0123456789.......... -1
print(ex[0])   # --> A  --> positive index start from left to right
print(ex[-1])  # --> l  --> negative index start from right to left
print(ex[-2])  # --> e
print(ex[6])   # --> Y

# todo# slicing ( access multiple sequence items )
# todo# print(variable [start:end])

print(ex[0:5])  # --> Adham --> end not included index
print(ex[:5])   # --> Adham --> if start not here it will start from 0
print(ex[17:])  # --> Blabel--> if end not here it will print to end
print(ex[:])    # --> full

print(ex[0::1])  # --> full
print(ex[::])    # --> full
print(ex[::1])   # --> full
print(ex[0::])   # --> full

print(ex[0::2])  # --> #! AhmYse b lbl --> print char and skip char
print(ex[0::3])  # --> #! AaYs ole --> print char and two skip char
print(ex[1::2])  # --> #! start from index [1] & print char and two skip char

# ----------------------------------------------------
#! -------------- Strings Methods --------------------
# ----------------------------------------------------
# ? len()                                        --> calc numbers of char of string
# ? strip()                                      --> remove spaces from right and lift
# ? rstrip()                                     --> remove spaces from right
# ? lstrip()                                     --> remove spaces from lift
# ? title()                                      --> make first char of each words Capital and after numbers
# ? capitalize()                                 --> make first char Capital only
# ? zfill(length of the biggest numbers)         --> put zeros Ex:1 ,12 ,154 --> 001 ,012 154
# ? upper()                                      --> make all letters Capital
# ? split(string split where,int max split)      --> Splits from left the string at the specified separator, and returns a list
# ? rsplit(string split where,int max split)     --> Splits from right the string at the specified separator, and returns a list
# ? center(int  , string "x")                    --> put "x" before and after string
# ? count(string "x" ,start , end )              --> count how many "x" in string
# ? swapcase()                                   --> make lower case --> upper case and oppisite
# ? startswith(string , start , end)             --> Returns true if the string starts with the specified value
# ? endswith(string , start , end)               --> Returns true if the string ends with the specified value
# ? replace(old value , new value , count)       --> replace value with value
# ? jion(string between words,list)              --> join list with string between words
# ? index(string "x" , range)                    --> show what is the index of  "x"  yes->true , no->error
# ? find(string "x" , range)                     --> show what is the index of  "x" yes->true , no->false
# ? rjust(width,fill char)                       --> fill right with char
# ? ljust(width,fill char)                       --> fill left with char
# ? splitline()                                  --> split lines and return them in list
# ? expandtabs(x)                                --> expand tabs number of x
# ? isalnum()                                    --> Returns True if all characters in the string are alphanumeric
# ? isalpha()                                    --> Returns True if all characters in the string are in the alphabet#? isalnum() Returns True if all characters in the string are alphanumeric
# ? islower()                                    --> Returns True if all characters in the string are lower case
# ? isspace()                                    --> Returns True if all characters in the string are whitespaces
# ? istitle()                                    --> Returns True if the string follows the rules of a title
# ? isidentifier()                               --> Returns True if the string is an identifier (rule of naming variable)
# ? lower()                                      --> make all letters Small
#! more detail in pages 128-->131 in IS book

x = "Adham"
y = "   Adham   "
z = "###Adham###"
print(len(x))
print(len(y))

print(y.strip())
print(y.rstrip())
print(y.lstrip(), "\n")

print(z.strip("#"))
print(z.rstrip("#"))
print(z.lstrip("#"))

h = "adham yasser abo blabel is 1n"
print(h.title())
print(h.capitalize())

a, b, c = "9", "99", "999"
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

q = "adham"
print(q.upper())

u = "adham yasser abo blabel"
print(u.split())

u = "adham-yasser-abo blabel"
print(u.split("-"))

u = "adham+yasser+abo+blabel"
print(u.split("+", 2))

g = "Adham"
print(g.center(9, "-"))

n = "adham ali adham nour adham"
print(n.count("adham"))
print(n.count("adham", 0, 18))

m = "Adham"
print(m.swapcase())

m = "aDHAM"
print(m.swapcase())

b = "adham azham"
print(b.startswith("a"))

b = "adham azham"
print(b.startswith("z", 7, 12))

b = "adham azham"
print(b.endswith("m"))

b = "adham azham"
print(b.endswith("m", 0, 5))

b = "adham azham azham azham"
print(b.replace("azham", "adham"))

c = ["adham", "yasser"]
print("-".join(c))

o = "adham ban man sna said more jam nam"
print(o.index("j"))
# print(o.index("x")) error

o = "adham ban man sna said more jam nam"
print(o.find("j"))
print(o.find("x"))  # -1

w = "Adham"
print(w.rjust(7))
print(w.rjust(7, "-"))

w = "Adham"
print(w.ljust(7))
print(w.ljust(7, "-"))

s = """1
2
3
4
5
"""
print(s.splitlines())

m = "a\td\th\ta\tm"
print(m.expandtabs(20))

b = "asdf123"
m = "asdf"
l = "132"
print(b.isalnum())
print(b.isalpha())
print(b.isspace())
print(b.istitle())
print(b.isidentifier(), "\n")

print(m.isalnum())
print(m.isalpha())
print(m.isspace())
print(m.istitle())
print(m.isidentifier(), "\n")

print(l.isalnum())
print(l.isalpha())
print(l.isspace())
print(l.istitle())
print(l.isidentifier())

# --------------------------------------------------
#!------------- string formatting ------------------
# --------------------------------------------------
# todo #---------- Method One ----------------------
# --------------------------------------------------
# ? print("bla bla bla %s,d,f " % (variable) )

# ? %s   --> string
# ? %.xs --> string print the from first to  x index

# ? %d   --> intger
# ? %.xd --> intger print x numbers and fill zeros

# ? %f   --> flaot
# ? %.xf --> flaot print x numbers after point


name = "Adham"
age = 18
rank = 999

print("name is : " + name)
# print("name is : "+name ,"age is : "+age) error
# print("name is : "+name + "age is : "+age) error

print("name is : %s" % name)
print("name is : %s & age is : %.5d & rank is : %f" % (name, age, rank))

n = "Adham"
e = "Eng"
p = 99.99999999

print("name is : %s & is the best %.3s & i rate him %.8f " % (n, e, p))

# --------------------------------------------------
# todo #---------- Method Two ----------------------
# --------------------------------------------------
# ? print("bla bla bla {} bla bla bla {}".format(variable1 , variable2))

# ?{:s}    --> string
# ?{:.xs}  --> string print the from first to x index

# ?{:d}    --> intger
# ?{:.xd}  --> intger print x numbers and fill zeros

# ?{:f}    --> float
# ?{:.xf}  --> flaot print x numbers after point

# ?{:_d,f} --> intger or float put (_) between each three numbers
# ?{:,d,f} --> intger or float put (,) between each three numbers

name = "Adham"
age = 18
rank = 999

print("Name is : {}".format(name))
print("Name is : {} & Age is : {} & Rank is : {}".format(name, age, rank))
print("Name is : {:.5s} & Age is : {:5d} & Rank is : {:.1f}".format(name, age, rank))

money = 152485628498.123456
print("My money is : {:_f}".format(money))
print("My money is : {:,f}".format(money))
print("My money is : {:,f}".format(money))

# ? arrangment

x, y, z = "A", "D", "H"
#          0    1    2
print("Adham. {0:s} {1:s} {2:s}".format(x, y, z))
print("Adham. {0:s} {2:s} {1:s}".format(x, y, z))
print("Adham. {1:s} {0:s} {2:s}".format(x, y, z))
print("Adham. {1:s} {2:s} {0:s}".format(x, y, z))
print("Adham. {2:s} {0:s} {1:s}".format(x, y, z))
print("Adham. {2:s} {1:s} {0:s}".format(x, y, z))

# --------------------------------------------------
# todo #---------- Method Three --------------------
# --------------------------------------------------
# ? print(f"bla bla bla {variable}")

# ?{variables:s}    --> string
# ?{variables:xs}   --> string print the from first to x index

# ?{variables:d}    --> intger
# ?{variables:xyd}  --> intger print y numbers and fill x

# ?{variables:.f}    --> float
# ?{variables:.xyf}  --> float print y numbers after point and fill x

# ?{variables:_d,f} --> intger or float put (_) between each three numbers
# ?{variables:,d,f} --> intger or float put (,) between each three numbers

name = "Adham"
age = 18
rank = 999

print(f"Name is : {name} & Age : {age:03d} & Rank : {rank:.2f}")
