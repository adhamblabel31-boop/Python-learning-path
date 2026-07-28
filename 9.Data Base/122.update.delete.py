# ----------------------------------------------------
# ! --------------- update and delete ----------------
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create database and connect
db = sqlite3.connect("app.db")

# setting up the cursor
cr = db.cursor()

# update data
# cr.execute("update users set name = 'aDham' where user_id = 1")
# cr.execute("update users set name = 'Adham' where user_id = 2")
# cr.execute("update users set name = 'aDhaM' where user_id = 3")

# delete data
cr.execute("delete from users where user_id = 4")

# fetch data
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# save (commit) changes
db.commit()

# close database
db.close()