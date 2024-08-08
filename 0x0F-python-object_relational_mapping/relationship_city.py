#!/usr/bin/python3

"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Representation of a City"""

    __tablename__ = 'cities'

    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)


if __name__ == "__main__":

    import sys
    from sqlalchemy import create_all

    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and connect to the MySQL database
    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)
