#!/usr/python3
"""
lists all states from the database hbtn_0e_0_usa
takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create cursor object
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # fetch all rows
    rows = cursor.fetchall()
    # print results
    for row in rows:
        print(row)

    # close cursor and database connection
    cursor.close()
    db.close()
