# ----------------------------------------------------
#! ------------- membership opetator -----------------
# ----------------------------------------------------
# ? in
# ? not in
# ----------------------------------------------------
# todo# string
name = "Adham"
print("a" in name)  # True
print("A" in name)  # True
print("dham" in name)  # True
print("q" in name)  # False
print("ham" not in name)  # False
# ----------------------------------------------------
# todo# list

name = input("Enter your name: ").capitalize().strip()

whiteCountries = ["Egypt", "Oman", "Ksa"]
blackCountries = ["Usa", "Uk", "Canada"]

country = input("Enter your country: ").capitalize().strip()
checkStudent = input("Are you a student? y/n: ").lower().strip()
mName = "Adham"
meeting = 100


if country in whiteCountries:
    if checkStudent == "y":
        print(f"hi {name} because you are from {country} and you are a student")
        print(f"you have to pay {meeting - 99} $ for the meeting")
    else:
        print(f"hi {name} because you are from {country}")
        print(f"you have to pay {meeting - 90} $ for the meeting")
elif country in blackCountries:
    if checkStudent == "y":
        print(f"hi {name} because you are from {country} and you are a student")
        print(f"you have to pay {meeting + 50} $ for the meeting")
    else:
        print(f"hi {name} because you are from {country}")
        print(f"you have to pay {meeting + 100} $ for the meeting")
else:
    print(f"hi {name} because you are from {country}")
    print(f"you have to pay {meeting} $ for the meeting")
