#!/usr/bin/python3
"""connect to the database and fetch data
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    my_db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = my_db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
