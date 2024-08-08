#!/usr/bin/python3

"""
Module that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
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

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
