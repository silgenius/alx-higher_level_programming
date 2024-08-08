#!/usr/bin/python3

"""contains the class definition of a State"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """contains the class definition of a City"""

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False
            )

    name = Column(
            String(128),
            nullable=False
            )

    cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
            )


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
