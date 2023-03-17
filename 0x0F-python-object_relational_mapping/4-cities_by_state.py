#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC")
    row = cur.fetchall()
    [print(rows) for rows in row]
