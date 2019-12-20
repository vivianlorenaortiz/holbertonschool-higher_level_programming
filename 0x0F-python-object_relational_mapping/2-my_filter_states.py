#!/usr/bin/python3
"""
script that lists all states with a name starting.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states where name\
            LIKE BINARY '{}'".format(sys.argv[4])
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
