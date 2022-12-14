#!/usr/bin/python3
""""A script that lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb
# db = MySQLdb.connect(mysql username=sys.argv[0],mysql
# password=sys.argv[1],database name=sys.argv[3],localhost=3306)
if __name__ == '__main__':
    conn = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name like binary\
            '{}' order by states.id asc".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
