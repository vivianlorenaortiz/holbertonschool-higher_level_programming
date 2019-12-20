#!/usr/bin/python3
"""SQL Injection... """

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4],))
    for row in cur:
        print("{}".format(row))
    cur.close()
    db.close()
