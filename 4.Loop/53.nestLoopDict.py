# ----------------------------------------------------
#!------------------- nested loop --------------------
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

for name in persons:
    print(f"name is :{name}")
    for sub in persons[name] :
        print(f"sub is : {sub} --> {persons[name][sub]}")
