# after 95
# you can use it in decoration

look = True
cont = ""
while look:

    # codo block

    cont = input("plz press y to continue or press n to exit : ")
    if cont == "y":
        look = True

    elif cont == "n":
        look = False

    else:
        print("invalid input, exiting the program\n")
        look = False
