#!/usr/bin/python3
"""
script that lists all states with a name starting.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_passwd, db=mysql_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".
                format(mysql_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == mysql_name:
            print(row)
    cur.close()
    db.close()
