#!/usr/bin/python3

"""
Module that prints the State object with the name passed as argument from the
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
    search = sys.argv[4]

    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).filter(State.name == search).first()

    if state:
        print(f'{state[0]}')
    else:
        print("Not found")

    session.close()
