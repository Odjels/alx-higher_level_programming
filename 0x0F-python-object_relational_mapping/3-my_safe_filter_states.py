#!/usr/bin/python3
"""
    write a script that is free from SQL injections
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
     my_db = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
