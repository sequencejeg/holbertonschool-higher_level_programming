#!/usr/bin/python3
'''This script takes a name from state and lists all cities in said state'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    cities = ', '.join([row[0] for row in rows])
    print(cities)
    cur.close()
    db.close()
