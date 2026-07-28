# ----------------------------------------------------
#!----------------- function recursion ---------------
# ----------------------------------------------------
Name = "AAAAAAAddddddhhhhhhaaaaaaaaaammmmmmmmm"


def clean(name):
    if len(name) == 1:
        return name
    if name[0] == name[1]:
        return clean(name[1:])
    return name[0] + clean(name[1:])


print(clean(Name))
