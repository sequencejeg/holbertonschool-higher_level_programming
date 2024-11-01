#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    On the 'if' condition, we ensure the script runs only when
    executed directly, and not when imported as a module.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    """
    Above we create a cursor object to execute SQL queries.
    """

    """
    Below we execute the MySql Query.
    """
    cur.execute("SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name = '{}')\
                ORDER BY id".format(sys.argv[4]))

    """
    Below we are obtaining the Query result, and printing the result in rows.
    """
    rows = cur.fetchall()
    tabl = []
    for row in rows:
        tabl.append(row[0])
    print(', '.join(tabl))

    """
    Below we close the cursor, and the database connection.
    """
    cur.close()
    db.close()
