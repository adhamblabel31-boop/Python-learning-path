# ----------------------------------------------------
#!------------------ function scope ------------------
# ----------------------------------------------------
x = "Adham"  # global


def name1():
    global x
    x = "adham"
    print(x)


def name2():
    x = "ADHAM"  # local
    print(x)


name2()
name1()
name2()
