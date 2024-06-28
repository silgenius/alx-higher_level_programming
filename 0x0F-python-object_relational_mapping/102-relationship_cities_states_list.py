#!/usr/bin/python3

"""
 a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(
            State,
            City).select_from(
                    State
                    ).join(City):
        print(f'{city.id}: {city.name} -> {state.name}')

    session.close()
