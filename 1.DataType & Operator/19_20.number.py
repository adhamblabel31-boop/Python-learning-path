# ----------------------------------------------------
#! numbers
# ----------------------------------------------------
# ? [1] integer --> postive or minus  --> 10
# ? [2] float   -->  postive or minus --> 2.5
# ? [3] complex --> real+imaginary    --> 6+5j
# ----------------------------------------------------
# todo# [1] you can convert from int to float or complex
# todo# [2] you can convert from float to int or complex
# todo# [3] you can not convert complex to any type
# ----------------------------------------------------

print(type(5))
print(type(-5))

print(type(5.0))
print(type(-5.25))

print(type(5 + 45j))
print(type(-5 - 13j))

compl = 5 + 6j
print("real : {}".format(compl.real))
print("imaginary : {}".format(compl.imag))


print(100)
print(float(100))
print(complex(100))

print(100.99)
print(int(100.99))
print(complex(100.99))

print(100 + 2j)
# print(int(100+2j))   error
# print(float(100+2j)) error
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
