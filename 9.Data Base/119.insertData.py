# ----------------------------------------------------
# ! ----------- insert data into data base -----------
# ----------------------------------------------------
# ? [1] cursor --> all operation in SQL done by cursor not the conncetion itself
# ? [2] commit --> save all changes
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create database and connect
db = sqlite3.connect("app.db")

# setting up the cursor
cr = db.cursor()

# create the taable and fields
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# # insert data
cr.execute("insert into users(user_id,name) values(1, 'Adham')")
cr.execute("insert into users(user_id,name) values(2, 'adham')")
cr.execute("insert into users(user_id,name) values(3, 'ADHAM')")

# userList=["Adham","adham","ADHAM","aDHAM","adhaM"]
# for key , user in enumerate(userList):
#     cr.execute(f"insert into users(user_id,name) values({key+1}, '{user}')")

# save(commit) changes
db.commit()

# close database
db.close()