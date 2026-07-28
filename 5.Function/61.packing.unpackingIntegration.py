# ----------------------------------------------------
#!--------- packing , unpacking integration ----------
# ----------------------------------------------------
def wel2(name, *name1, **name2):
    print(f"Hi , {name}")
    for o in name1:
        print(f"Hi , {o}")
    for n, m in name2.items():
        print(f"{n} --> Hi , {m}")


Name = "Adham"
tuppleName = ("adham", "Adham", "ADHAM")
dictName = {
    "way1": "adham",
    "way2": "Adham",
    "way3": "ADHAM"
    }

wel2(Name, *tuppleName, **dictName)
