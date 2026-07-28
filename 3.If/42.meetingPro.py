# --------------------------------------------------
#! nested if
# --------------------------------------------------
name = input("Enter your name: ").capitalize().strip()
country = input("Enter your country: ").capitalize().strip()
checkStudent = input("Are you a student? y/n: ").lower().strip()
mName = "Adham"
meeting = 100

if country == "Egypt":
    if checkStudent == "y":
        print(f"hi {name} because you are from {country} and you are a student")
        print(f"you have to pay {meeting - 99} $ for the meeting")
    else:
        print(f"hi {name} because you are from {country}")
        print(f"you have to pay {meeting - 90} $ for the meeting")
elif country == "Oman":
    if checkStudent == "y":
        print(f"hi {name} because you are from {country} and you are a student")
        print(f"you have to pay {meeting - 20} $ for the meeting")
    else:
        print(f"hi {name} because you are from {country}")
        print(f"you have to pay {meeting - 15} $ for the meeting")
elif country == "Ksa":
    if checkStudent == "y":
        print(f"hi {name} because you are from {country} and you are a student")
        print(f"you have to pay {meeting - 10} $ for the meeting")
    else:
        print(f"hi {name} because you are from {country}")
        print(f"you have to pay {meeting - 5} $ for the meeting")
else:
    if checkStudent == "y":
        print(f"hi {name} because you are from {country} and you are a student")
        print(f"you have to pay {meeting - 2} $ for the meeting")
    else:
        print(f"hi {name} because you are from {country}")
        print(f"you have to pay {meeting - 1} $ for the meeting")
