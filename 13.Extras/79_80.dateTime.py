# ----------------------------------------------------
#!--------- introduction to date and time ------------
# ----------------------------------------------------

import datetime

# print(dir(datetime))
# print("-----"*15)
# print(dir(datetime.datetime))

# current date and time
print(f"Current date and time: {datetime.datetime.now()}")
print("-----" * 15)

# current year
print(f"Current year: {datetime.datetime.now().year}")
print("-----" * 15)

# current month
print(f"Current month: {datetime.datetime.now().month}")
print("-----" * 15)

# current day
print(f"Current day: {datetime.datetime.now().day}")
print("-----" * 15)

# start and end of date
print(f"Start of date : {datetime.datetime.min}")
print(f"End of date   : {datetime.datetime.max}")

print("*****" * 15)

# ----------------------------------------------------

# curent time
print(f"Current time: {datetime.datetime.now().time()}")
print("-----" * 15)

# current hour
print(f"Current hour: {datetime.datetime.now().time().hour}")
print("-----" * 15)

# current minute
print(f"Current minute: {datetime.datetime.now().time().minute}")
print("-----" * 15)

# current second
print(f"Current second: {datetime.datetime.now().time().second}")
print("-----" * 15)

# start and end of time
print(f"Start of time : {datetime.time.min}")
print(f"End of time   : {datetime.time.max}")

print("*****" * 15)
# ----------------------------------------------------

# specific date
print(f"Specific date: {datetime.datetime(2008, 1, 10)}")

myBirth = datetime.datetime(2008, 1, 10)
dateNow = datetime.datetime.now()
livedFor = (dateNow - myBirth).days

print(f"i lived for: {livedFor} days")
print(f"i lived for: {(livedFor/ 365.25):.2f} years")

print("#####" * 15)
# ----------------------------------------------------
# ! ---------------- format date ---------------------
# ----------------------------------------------------
# ? https://strftime.org/
# ----------------------------------------------------

myBirth = datetime.datetime(2008, 1, 10)
print(myBirth.strftime("%b"))
print(myBirth.strftime("%A"))
print(myBirth.strftime("%d %b %Y"))
