# ----------------------------------------------------
#! ---------------- password guess -------------------
# ----------------------------------------------------

tries = 5
password = "Adham"

inPass = input("Enter your password: ")
while inPass != password:
    tries -= 1
    print(f"Wrong password! plz try again.")
    print(f"You have {'last' if tries == 0 else tries} tries left.")
    inPass = input("Enter your password: ")
    if tries == 0:
        print("You have been blocked!")
        break

else:
    print("correct password! welcome back.")
