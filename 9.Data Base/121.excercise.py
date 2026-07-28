# ----------------------------------------------------
# ! --------------- data base excercise --------------
# ----------------------------------------------------

import sqlite3


def getData():
    try:
        # connect to database
        db = sqlite3.connect("app.db")

        # setting up the cursor
        cr = db.cursor()

        # create the taable and fields
        cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

        # insert data
        cr.execute("insert into users(user_id,name) values(1, 'Adham')")
        cr.execute("insert into users(user_id,name) values(2, 'adham')")
        cr.execute("insert into users(user_id,name) values(3, 'ADHAM')")

        # print success connecting
        print("connecting to database is successfully")

        # fetch data from database
        cr.execute("select * from users")

        # assign data to variable
        results = cr.fetchall()
        print(results)

        # print num of raw
        print(f"there is {len(results)} raws")

        # printing message
        print("showing data: ")

        # loop on result
        for row in results:
            print(f"userId --> {row[0]},", end=" ")
            print(f"user name --> {row[1]}")

    except sqlite3.Error as sqler:
        print(f"error taking data {sqler}")

    finally:
        if db:
            # close database
            db.close()
            print("database is clossed")


getData()
