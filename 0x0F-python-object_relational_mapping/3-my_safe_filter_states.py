#!/usr/bin/python3
"""Write a script that takes in arguments and displays
all values in states table of hbtn_0e_0u_usa where
name matches the argument
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (arg,))
    row = cur.fetchall()
    [print(rows) for rows in row]
