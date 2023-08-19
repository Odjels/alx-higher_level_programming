#!/usr/bin/python3
""" takes in the name of a state as an argument and
    lists all cities of that state,
    using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    my_db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = my_db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))
    cur.close()
    my_db.close()
