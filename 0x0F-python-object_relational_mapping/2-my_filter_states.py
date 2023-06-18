#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
    # create a query with user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    parameters = (argv[4],)
    # execute query
    cursor.execute(query, parameters)
    # fetch all rows
    rows = cursor.fetchall()
    # print results
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # close cursor and database connection
    cursor.close()
    db.close()
