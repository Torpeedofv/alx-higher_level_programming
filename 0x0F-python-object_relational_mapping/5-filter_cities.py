#!/usr/bin/python3
"""a script that takes in the name of a state as an
argument and lists all cities of that state using 
the database hbtn_0e_4_usa"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    arg = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id=states.id WHERE states.name= %s ORDER BY cities.id ASC", (arg,))
    row = cur.fetchall()
    print(", ".join(rowe[0] for rowe in row))
