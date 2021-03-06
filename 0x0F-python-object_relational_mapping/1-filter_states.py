#!/usr/bin/python3
"""
script that lists all states with a name starting.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, name)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states where name LIKE BINARY 'N%'""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
