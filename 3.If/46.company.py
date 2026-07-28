# ----------------------------------------------------
#!------------------- company ------------------------
# ----------------------------------------------------
admin = ["Adham", "Osama", "Ahmed", "Mahmoud"]
name = input("Enter your name: ").capitalize().strip()

if name in admin:
    print(f"Hi {name} you are admin")
    option = input("delete or update your name : ").capitalize().strip()

    if option == "Update":
        newName = input("Enter your new name : ").capitalize().strip()
        admin[admin.index(name)] = newName
        print("Your name updated")
        print(admin)

    elif option == "Delete":
        admin.remove(name)
        print("Your name deleted")
        print(admin)

    else:
        print("Invalid option")
else:
    print(f"Hi {name} you are not admin")
    join = input("do you want to join admin group y/n ?").strip().lower()

    if join == "y":
        admin.append(name)
        print("You have been added to the admin group.")
        print(admin)

    elif join == "n":
        print("as you wish, goodbye!")

    else:
        print("Invalid option")
