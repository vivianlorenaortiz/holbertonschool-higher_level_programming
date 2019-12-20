#!/usr/bin/python3
""" Cities by states """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    for row in cur:
        print("{}".format(row))
    cur.close()
    db.close()
