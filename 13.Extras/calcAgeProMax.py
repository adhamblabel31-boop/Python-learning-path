# --------------------------------------------------
#! --------------- calculate the age ---------------
# --------------------------------------------------
# i did this program after video 94

import datetime

print("-" * 50)
print(" Adham ".center(50, "-"))
print("-" * 50)

print("Welcome to Age to Time Converter!")

print("enter your birth day")
Day = int(input("plz enter day   : "))
if Day < 0 or Day > 31:
    raise Exception("day can't be zero or less than zero or more than 31")

Month = int(input("plz enter month : "))
if Month < 0 or Month > 12:
    raise Exception("month can't be zero or less than zero or more than 12")

Year = int(input("plz enter year  : "))
if Year < 1900:
    raise Exception("year can't be less than 1900")
19

myBirth = datetime.datetime(Year, Month, Day)
dateNow = datetime.datetime.now()
livedFor = (dateNow - myBirth).days

days = livedFor
years = days / 365.25
months = days / 30
weeks = days / 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"You are lived for: {years:.3f} years")

look = True
cont=''
while (look):

    print(           "                                              mo  ,  w  ,   d  ,  h   ,   m    ,    s ")
    timeType = input("Enter the time type you want to convert to (months, weeks, days, hours, minutes, seconds): ").lower().strip()

    if timeType == "months" or timeType == "mo":
        print(f"You are lived for: {months:.3f} months")

    elif timeType == "weeks" or timeType == "w":
        print(f"You are lived for: {weeks:.3f} weeks")

    elif timeType == "days" or timeType == "d":
        print(f"You are lived for: {days:.3f} days")

    elif timeType == "hours" or timeType == "h":
        print(f"You are lived for: {hours:,} hours")

    elif timeType == "minutes" or timeType == "m":
        print(f"You are lived for: {minutes:,} minutes")

    elif timeType == "seconds" or timeType == "s":
        print(f"You are lived for: {seconds:,} seconds")

    else:
        print("Invalid time type entered.")

    cont=input("plz press y to continue or press n to exit : ")
    if (cont == 'n'):

        look = False

    elif (cont == 'y'):

        look = True

    else:

        print("invalid input, exiting the program\n")
        look = False
