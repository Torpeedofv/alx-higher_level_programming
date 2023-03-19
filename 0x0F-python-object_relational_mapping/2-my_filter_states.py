#!/usr/bin/python3
"""A script that takes in an argument and displays all values
in the states table of hbtn-0e_0_usa where the name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                BINARY name = '{}'".format(sys.argv[4]))
    row = cur.fetchall()
    [print(rows) for rows in row]
