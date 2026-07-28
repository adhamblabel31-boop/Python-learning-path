# ----------------------------------------------------
#! -------------------- data base --------------------
# ----------------------------------------------------
# ? [1] database is a place where we can store data
# ? [2] database organized into tables (users, categorise)
# ? [3] tables has columns (ID, username, password)
# ? [4] there's many types of databases (mongoDB, MySQL, SQLite)
# ? [5] SQL --> structured query language
# ? [6] SQLite --> can run in memory or in a single file
# ? [7] you can browse file with https://sqlitebrowser.org/
# ? [8] data inside database has types (text, integer, data)

# ----------------------------------------------------
# ! ---------- create data base and connect ----------
# ----------------------------------------------------
# ? [1] connect
# ? [2] execute
# ? [3] close
# ----------------------------------------------------

# import SQLite module
import sqlite3

# create database and connect
db = sqlite3.connect("app.db")

# create the taable and fields
db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# close database
db.close()
