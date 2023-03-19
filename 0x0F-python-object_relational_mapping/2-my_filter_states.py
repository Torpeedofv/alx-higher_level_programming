#!/usr/bin/python3
import MySQLdb
import sys
"""A script that takes in an argument and displays all values
in the states table of hbtn-0e_0_usa where the name matches the argument
"""

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE\
                name = %s ORDER BY id ASC", (arg,))
    row = cur.fetchall()
    [print(rows) for rows in row]
