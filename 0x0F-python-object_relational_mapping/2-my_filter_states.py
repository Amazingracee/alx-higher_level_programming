#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3]
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%s'" %(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
