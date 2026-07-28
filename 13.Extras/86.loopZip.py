# ----------------------------------------------------
# ! ---------------- loop with zip -------------------
# ----------------------------------------------------
# ? zip() return a zip object contains all objects
# ? zip length is the length of lowest object
# ----------------------------------------------------
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "D", "H", "A", "M"]
tupple1 = ("Adham", "ADHAM", "adham")
dict2 = {"name": "Adham", "Age": 18, "countyr": "Egypt"}

for item1, item2, item3, item4 in zip(list1, list2, tupple1, dict2):
    print(item1, item2, item3, item4, dict2[item4])
