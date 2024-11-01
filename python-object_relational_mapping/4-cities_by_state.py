#!/usr/bin/python3
"""
This script lists all cities from the database of hbtn_0e_4_usa.
It takes 3 command-line args: MySQL username, password, and database name.
"""

import MySQLdb
import sys

"""
Above we import MySQLdb to be able to interact with MySQL.
We also import sys to handle command-line args for the username,
password, and database name.
"""

"""
Below we declare a function to create the cities query. We use a function
in order to improve readability, reusability, and maintainability
of the code.
"""


def get_cities_query():
    """
    Creates the SQL query to fetch cities and their corresponding states.

    Returns:
        string: The SQL query.
    """
    return """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
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
    Below we execute the SQL query, and get the cities from the database.
    """
    cur.execute(get_cities_query())
    """
    Above we execute the SQL query.
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
