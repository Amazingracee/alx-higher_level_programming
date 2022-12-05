#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON states.id = cities.state_id;")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
