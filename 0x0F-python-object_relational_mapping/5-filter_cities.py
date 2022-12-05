#!/usr/bin/python3
"""
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """

    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id,cities.name FROM cities JOIN states ON\
            states.id = cities.state_id WHERE\
            states.name = %(state_name)s ORDER\
            BY cities.id ASC", {'state_name': argv[4]})
    cities = cur.fetchall()
    if cities is not None:
        print(", ".join([city[1] for city in cities]))
    cur.close()
    conn.close()
