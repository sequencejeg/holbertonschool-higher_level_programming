#!/usr/bin/python3
'''This script selects all state that start with letter N'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if 'N' in row[1][0]:
            print(row)
    cur.close()
    db.close()
