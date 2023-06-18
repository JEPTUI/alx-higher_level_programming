#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create cursor object
    cursor = db.cursor()
    # create a query with user input
    query = """SELECT cities.name
    FROM states
    INNER JOIN cities ON states.id = cities.state_id
    WHERE states.name LIKE %s
    ORDER BY cities.id ASC"""
    parameters = (argv[4],)
    # execute query
    cursor.execute(query, parameters)
    # format to display cities of same state separated by a comma
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))
    # close cursor and database connection
    cursor.close()
    db.close()
