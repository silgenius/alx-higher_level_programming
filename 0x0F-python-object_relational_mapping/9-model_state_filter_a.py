#!/usr/bin/python3

"""
Module lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State.id, State.name).filter(State.name.like('%a%'))

    for state_id, state_name in states:
        print(f'{state_id}: {state_name}')

    session.close()
