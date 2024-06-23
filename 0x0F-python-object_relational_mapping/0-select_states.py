#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves and prints the names
of all states in the `states` table. It requires three command-line arguments:
the database username, the database password, and the database name.

Usage:
    ./script.py <db_username> <db_passwd> <db_name>
"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    db_username = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=db_username,
            passwd=db_passwd,
            db=db_name,
            port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
