#!/usr/bin/python3
"""All cities by state """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
    states.id = cities.state_id WHERE states.name=%s",
                (sys.argv[4],))
    result = cur.fetchall()
    arr = []
    for row in result:
        arr.append(row[0])
    print(", ".join(arr))
    cur.close()
    db.close()
