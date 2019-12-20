#!/usr/bin/python3
"""SQL Injection... """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states where name = %s", [sys.argv[4]])

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
