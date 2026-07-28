# --------------------------------------------------
#! if , elif , else
# --------------------------------------------------
name = input("Enter your name: ").strip().capitalize()
country = input("Enter your country: ").strip().capitalize()
mName = "Adham"
meeting = 100

if country == "Egypt":
    print(f"hi {name} because you are from {country}")
    print(f"you have to pay {meeting - 99} $ for the meeting")
elif country == "Oman":
    print(f"hi {name} because you are from {country}")
    print(f"you have to pay {meeting-10} $ for the meeting")
elif country == "KSA":
    print(f"hi {name} because you are from {country}")
    print(f"you have to pay {meeting - 5} $ for the meeting")
else:
    print(f"hi {name} because you are from {country}")
    print(f"you have to pay {meeting - 1} $ for the meeting")
