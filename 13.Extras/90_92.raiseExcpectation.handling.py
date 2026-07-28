# ----------------------------------------------------
# ! --------- errors and exceptions raising ----------
# ----------------------------------------------------
# ? [1] exceptions is a runtime error reporting mechanism
# ? [2] exception gives you the message to understand the problem
# ? [3] traceback gives you the line to look for the code in this line
# ? [4] exceptions have types (syntaxError , indexError , keyError , etc...)
# ? [5] exceptions list https://docs.python.org/3/library/exceptions/html
# ? [6] raise keyword used to raise your own exceptions
# ----------------------------------------------------
x = 9

if x < 0:
    raise Exception("pls enter number greater than zero")
# todo# any thing after the exception won't be printed

else:
    print(f"{x} is good and conitnue")

# todo# we need to stop the program in the condtion if it is false so we raise an excepton to stop it

name = "Adham"

if name != "Adham":
    raise Exception("enter the right name , dog")
else:
    print("here you go , Eng :)")

print("-----" * 15)
# ----------------------------------------------------
# ! -------------- exceptions handling ---------------
# ----------------------------------------------------
# ? [1] try     --> test the code for errors
# ? [2] except  --> handle the errors
# ----------------------------------------------------
# ? [3] else    --> if no errors
# ? [4] finally --> run the code
# ----------------------------------------------------

try:  # try the program --> print if true
    age = int(input("enter your age : "))
    print("try is good")

except:  # handle the errors if its found --> print if false
    print("it is not int")

else:  # if theres no errors --> print if true
    print("good else")

finally:  # run anyway whether true or false
    print("finaly of the program")


print("-----" * 15)
# ----------------------------------------------------

try:
    print(10 / 0)
    # print(z)
    print(int("Adham"))

except ZeroDivisionError:
    print("can't divide")

except NameError:
    print("identifier not found")

except ValueError:
    print("can't convert")

except:
    print("error happen")

print("-----" * 15)
# ----------------------------------------------------
# ? example
# ? to run hash the previous

theFile = None
tries = 5

while tries > 0:
    # print(f"{tries} tries left")
    # tries-=1

    try:  # try to open the file
        print("enter the absolsute path of the file")
        print(f"{tries} tries left")
        print(r"example : c:\Users\Adham\GitHub\Python-learning-path\7.Extras\90.raiseExcpectation.py")
        # C:\Users\Adham\GitHub\Python-learning-path\6.File Handling\adham.txt
        filePath = input("file path --> :").strip()
        path = open(filePath, "r")
        print(path.read())
        break

    except FileNotFoundError:
        print("file is not found pls try again")
        tries -= 1

    except:
        print("error happen")

    finally:
        if theFile is not None:
            theFile.close()
            print("file closed")


else:
    print("tries end you are forbiden")
