#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
            states.id = cities.state_id WHERE\
            states.name = %(state_name)s ORDER\
            BY cities.id ASC", {'state_name': argv[4]})
    cities = cur.fetchall()
    lists = []
    for city in cities:
        lists += city
    print(", ".join(lists))
    cur.close()
    conn.close()
