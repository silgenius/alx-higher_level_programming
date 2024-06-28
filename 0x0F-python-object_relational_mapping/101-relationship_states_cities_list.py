#!/usr/bin/python3

"""
 a script that lists all State objects, and corresponding City objects,
 contained in the database hbtn_0e_101_usa
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
    for state in session.query(State).all():
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
