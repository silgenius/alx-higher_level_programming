#!/usr/bin/python3

"""
This script connects to a MySQL database and lists all cities of a given state
from the `cities` table in the hbtn_0e_4_usa database. It requires four
command-line arguments: the database username, the database password, the
database name, and the state name.

The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id and displayed as they
are retrieved.

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
    query = "SELECT cities.name FROM states JOIN cities ON\
            states.id = cities.state_id WHERE states.name = %s"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    result = ""
    for row in rows:
        result += row[0] + ", "
    print(result[0:-2])
