#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(name)s\
            ORDER BY states.id ASC", {'name': argv[4]})
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
