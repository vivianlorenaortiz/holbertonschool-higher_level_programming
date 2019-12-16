#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if _name_ =="_main_":
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]


    db = MySQLdb.connect("localhost",username,password,name)
    cur = db.cursor ()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
         print(row)
    cur.close()
    db.close()
