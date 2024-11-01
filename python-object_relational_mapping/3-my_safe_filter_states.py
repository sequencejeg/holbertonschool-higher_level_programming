#!/usr/bin/python3
"""
This script takes an argument and displays all values in
the states table of  hbtn_0e_0_usa where name matches the argument.
It takes 4 command-line args: MySQL username, password, database name,
and state name searched.
"""

import MySQLdb
import sys

"""
Above we import MySQLdb to be able to interact with MySQL.
We also import sys to handle command-line args for the username,
password, and database name.
"""


"""
On the 'if' condition below, we ensure the script runs only when
executed directly, and not when imported as a module.
"""
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )
    """
    Above we establish the MySQL database connection.
    sys.argv[1], sys.argv[2], sys.argv[3] are command-line args for MySQL
    username, password, and database name.
    """

    cur = db.cursor()
    """
    Above we create a cursor object to execute SQL queries.
    """

    """
    Below we create the query, and get the state name from the command-line.
    We use Like Binary to ensure that the string comparison is done in
    a case-sensitive manner.
    """
    state_name = sys.argv[4]
    query = """SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY
    id ASC"""
    cur.execute(query, (state_name,))
    """
    Above we execute an SQL query.
    """

    """
    Below we fetch all rows, and print the matching row.
    """
    for row in cur.fetchall():
        print(row)

    """
    Below we close the cursor, and the database connection.
    """
    cur.close()
    db.close()
