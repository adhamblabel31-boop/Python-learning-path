# ----------------------------------------------------
#! -------------- important information --------------
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create database and connect
db = sqlite3.connect("app.db")

# setting up the cursor
cr = db.cursor()

my_tupple = ('go', '00', 5)

# insert data
cr.execute("insert into skills values(?, ?, ?)",my_tupple)

# fetch data from database & insert
# cr.execute("select * from skills orde+r by name limit 4 offset 2")
# cr.execute("select * from skills where user_id > 1")
# cr.execute("select * from skills where user_id in(1, 3)")
cr.execute("select * from skills where user_id not in(1, 3)")

# assign data to variable
results = cr.fetchall()

# loop on result
for row in results:
    print(f"name --> {row[0]},", end=" ")
    print(f"progress --> {row[1]},", end=" ")
    print(f"user_id --> {row[2]}")

# save(commit) changes
db.commit()

# close database
db.close()
