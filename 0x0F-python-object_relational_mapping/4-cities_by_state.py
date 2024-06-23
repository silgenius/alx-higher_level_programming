#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves and prints all cities
from the `cities` table in the hbtn_0e_4_usa database. It requires three
command-line arguments: the database username, the database password, and
the database name.

The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id and displayed as they are
retrieved.

Usage:
    ./script.py <db_username> <db_passwd> <db_name>
"""

if __name__ == "__main__":

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
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
