# ----------------------------------------------------
# ! --------------- debugging code -------------------
# ----------------------------------------------------
# this file is (51.changeLetter)
# F11 , F5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        print(f"{num} is odd number")
    else:
        print(f"{num} is even number")

print("-" * 52)
nme = ""
name = "Adham"
for letter in name:
    if letter == "A" or letter == "a":
        letter = "@"
    nme += letter

print(nme)
