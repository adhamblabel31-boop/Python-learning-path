# ----------------------------------------------------
# ! ------------------- skills app -------------------
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create database and connect
db = sqlite3.connect("app.db")

# setting up the cursor
cr = db.cursor()


def com_clo():
    """commit changes and close connection to database"""
    db.commit()  # save (commit) changes
    db.close()  # close database
    print("connection is closed")


# user id
uid = 1

# input message to user
input_message = """
what do you want to do ?
"s" --> show all skills
"a" --> add new skill
"u" --> update skill progress
"d" --> delete a skill
"q" --> quit the app
choose option : """

# input option choose
user_input = input(input_message).strip().lower()


# define the methods
def show():
    cr.execute(f"select * from skills where user_id = '{uid}'")
    result = cr.fetchall()
    print(f"you have {len(result)} skills")

    if len(result) > 0:
        print("skills with progress : ")
        for row in result:
            print(f"skill --> {row[0]} , progress --> {row[1]}%")
    else:
        print("you have no skills")

    com_clo()


def add():
    sk = input("enter the skill name : ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    result = cr.fetchone()
    if result == None:
        prog = input("enter the new progress of skill : ").strip()
        cr.execute(f"insert into skills(progress, user_id) values('{prog}', '{uid}')")
    else:
        print("skill is already exist")
        choose = input("you can update it if you want yes or no ? [y/n] : ")
        if choose == "y":
            prog = input("enter the new progress of skill : ").strip()
            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
            com_clo()
        elif choose == "n":
            com_clo()
        else:
            print("invalid input")
            com_clo()


def update():
    sk = input("enter the skill name : ").strip().capitalize()
    prog = input("enter the new progress of skill : ").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
    com_clo()


def delete():
    sk = input("enter the skill name : ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = {uid}")
    com_clo()


# command list
command_list = ["s", "a", "d", "u", "q"]

# check if command list is exists
if user_input in command_list:
    if user_input == "s":
        show()

    elif user_input == "a":
        add()

    elif user_input == "u":
        update()

    elif user_input == "d":
        delete()

    else:
        print("app is close .")
        com_clo()

else:
    print(f"command '{user_input}' is false")
