# ----------------------------------------------------
# ! ---------- retrive data from data base -----------
# ----------------------------------------------------
# ? fetchone        --> returns a single record or None if no more rows are available.
# ? fetchall        --> fetches all the rows of a query result. It returns all the rows
# ? fetchmany(size) --> as a list of tuples. An empty list is returned if there is no record to fetch.
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create database and connect
db = sqlite3.connect("app.db")

# setting up the cursor
cr = db.cursor()

# create the taable and fields
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

# insert data
# cr.execute("insert into users(user_id,name) values(1, 'Adham')")
# cr.execute("insert into users(user_id,name) values(2, 'adham')")
# cr.execute("insert into users(user_id,name) values(3, 'ADHAM')")

# fetch data
cr.execute("select * from users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# print(cr.fetchall())

print(cr.fetchmany(2))

# save(commit) changes
db.commit()

# close database
db.close()
