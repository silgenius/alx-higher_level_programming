#!/usr/bin/python3
"""
Module defining the State class and connecting to a MySQL database.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create an engine and connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
    
    # Create all tables in the database
    Base.metadata.create_all(engine)

