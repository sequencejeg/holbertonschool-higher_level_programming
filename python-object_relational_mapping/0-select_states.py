#!/usr/bin/python3
"""
On this script we list all states from the database hbtn_0e_0_usa.
It takes 3 command line args: MySQL username, password, and
database name.
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

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    """
    Above we execute an SQL query to select ALL states from the database,
    in ascending order.
    """

    """
    Below we fetch all the rows from the result of the query.
    """
    rows = cur.fetchall()

    """
    Below we iterate over the fetched results, and print each state.
    """
    for row in rows:
        print(row)

    """
    Below we close the cursor, and the database connection.
    """
    cur.close()
    db.close()
