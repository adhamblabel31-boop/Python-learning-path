# --------------------------------------------------
#! --------------- calculate the age ---------------
# --------------------------------------------------
print("-" * 50)
print(" Adham ".center(50, "-"))
print("-" * 50)

print("Welcome to Age to Time Converter!")

age = int(input("Enter your age: ").strip())
timeType = input("Enter the time type you want to convert to (months, weeks, days, hours, minutes, seconds): ").lower().strip()

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if timeType == "months" or timeType == "mo":
    print(f"You are lived for: {months:,} months")
elif timeType == "weeks" or timeType == "w":
    print(f"You are lived for: {weeks:,} weeks")
elif timeType == "days" or timeType == "d":
    print(f"You are lived for: {days:,} days")
elif timeType == "hours" or timeType == "h":
    print(f"You are lived for: {hours:,} hours")
elif timeType == "minutes" or timeType == "m":
    print(f"You are lived for: {minutes:,} minutes")
elif timeType == "seconds" or timeType == "s":
    print(f"You are lived for: {seconds:,} seconds")
else:
    print("Invalid time type entered.")
