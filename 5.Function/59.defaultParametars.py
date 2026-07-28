# ----------------------------------------------------
#!--------------- default parametars -----------------
# ----------------------------------------------------
# def wel(name="Adham", age, country): error --> default parametars must be the last parametar hasn't default parametars
def wel(name="Adham", age=18, country="Eygpt"):
    print(f"Hi, {name} | your age is : {age} | your country is : {country}")


wel("Adham", 18)
wel("adham", 45, "KSA")
wel()
wel("Ahmed", 21, "Algeria")
