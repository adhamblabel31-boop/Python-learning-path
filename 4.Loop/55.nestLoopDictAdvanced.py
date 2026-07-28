# ----------------------------------------------------
#!------------- nested loop advanced -----------------
# ----------------------------------------------------
persons={
    "adham":{
        "cs":"100%",
        "is":"100%",
        "dm":"100%"
    },
    "ahmed":{
        "cs":"50%",
        "is":"90%",
        "dm":"45%"
    },
    "ali":{
        "cs":"80%",
        "is":"93%",
        "dm":"57%"
    }
}
# print(persons.items())

for nameKey, blockValue in persons.items():
    print(f"name is : {nameKey}")
    for subKey,resultValue in blockValue.items():
        print(f"sub is : {subKey} --> {resultValue}")