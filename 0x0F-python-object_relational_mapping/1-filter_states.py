#!/usr/bin/python3
"""
lists all states with a name starting with N from the database hbtn_0e_0_usa
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
        if row[1][0] == 'N':
            print(row)

    # close cursor and database connection
    cursor.close()
    db.close()
