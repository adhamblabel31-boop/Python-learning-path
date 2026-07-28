# --------------------------------------------------
#!use hashtag(#) to write a comment
# --------------------------------------------------
#! ----------- characteristics of python -----------
# --------------------------------------------------
# ? [1] interpreted
# ? [2] interactive --> output appear in terminal
# ? [3] integrated  --> link with another language easily
# ? [4] indentation --> the first space before line
# ? [5] case senstive
# --------------------------------------------------

print("Adham")
#!you can put semicolon (;) between two sentence in the same line
print("hi")
print("man")
print("hi")
print("man")
# --------------------------------------------------
# todo# type() --> show type of variable --> print(type(variable))
#! all data in pyhton is object

# --------------------------------------------------
#!data type
# --------------------------------------------------
# ? int   --> integer            --> (10,-61)
# ? flaot --> float point number --> (-56.5,9.565)
# ? bool  --> boolean            --> (true,false)
# ? char  --> charactar          --> ('A,5')
# ? str   --> string             --> ("sdjff,sf448,951"),('')
# ? list  --> list               --> ([sd,54,s4,dsf,56.44,-65,sdf])
# ? tuple --> Tuple              --> ((sd,dss,56,564,dfds))
# ? dict  --> dictionary         --> ( { "x":1, "y":2, "z":3 } )
#!  more detail in page 110 in IS book
# --------------------------------------------------

#!how to assign value
# --------------------------------------------------
# ?[name of variable] [assignment operator(=+-*/)] [value]
# ex:
test = 5
print(test)
# --------------------------------------------------

#!rules of write name of variable
# --------------------------------------------------
# ? [1] can write A-->Z , 1-->9 , underscore (_) only anything else is error
# ? [2]cannot start with digit
# ? [3]case sensetive --> a!=A
# --------------------------------------------------

#! type of writing variable
# --------------------------------------------------
# ? camel  --> myName
# ? snake  --> my_name
# ? pascal --> MyName
# --------------------------------------------------

#!characteristics of python
# --------------------------------------------------
# ? source code --> original code you write it in computer
# ? translation --> converting source code into machine language
# ? compilation --> translate code before run time
# ? run time    --> period app take to executing commands
# ? interpreted --> code translated on the fly during exeution
# --------------------------------------------------

# * there are some of words reserve in language
# * you cannot use it
# * to know it --> help("keywords")
# --------------------------------------------------
#! to assign many value use comma (,)
# ex:
a, b, c = 1, 2, 3
print(a, b, c)
print(b)
print(c)

# --------------------------------------------------
#! escape sequences characters (\) back slash
# --------------------------------------------------
# ? [1] \b               --> back space
# ? [2] \+newline(entre) --> escape new line -->contain entre
# ? [3] \"               --> escape double quote
# ? [4] \'               --> escape single quote
# ? [5] \\               --> escape back slash
# ? [6] \n               --> line feed
# ? [7] \r               --> carrige return
# ? [8] \t               --> horizontal tab (3 spaces)
# ? [9] \xpp             --> character hex value
# --------------------------------------------------

# todo# back space
print("adham\byasser")  # will remove (m)

# todo# entre +\ --> escape back slash + back slash
print("adham \
yasser")

# todo# escape back slash
# todo# to print back slash put it twice
print("adham\\")

# todo# name escape double quote
print('"adham"yasser')

# todo# line feed
print("adham\nyasser")

# todo# carrige return
# todo# put 123 in the firist and remove abc
print("abcd\r123")
print("123456\rabcde")

# todo# horizontal tab
print("adham\tyasser")

# todo# carrige return
print("\x4f\x73")
