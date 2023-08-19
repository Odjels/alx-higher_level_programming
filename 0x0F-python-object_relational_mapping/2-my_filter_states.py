#!/usr/bin/python3
"""
Displays the values in the states table of the database hbtn_0e_0_usa
whose name matches with the supplied as argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                         passwd=argv[2], db=argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    stats = cr.fetchall()
    for stat in stats:
        if stat[1] == argv[4]:
            print(stat)
    cr.close()
    db.close()
