#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves and prints all rows
from the `states` table in the hbtn_0e_0_usa database where the state name
matches the provided argument. It requires four command-line arguments:
the database username, the database password, the database name,
and the state name to search for.

The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and
displayed as they are retrieved.

Usage:
    ./script.py <db_username> <db_passwd> <db_name> <state_name>
"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    db_username = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=db_username,
            passwd=db_passwd,
            db=db_name,
            port=3306
    )

    cur = db.cursor()
    format = "SELECT id, name FROM states WHERE name=%s"
    cur.execute(format, (state_name,))
    rows = cur.fetchall()

    for row in rows:
        if row[1] == state_name:
            print(row)

    cur.close()
    db.close()
