#!/usr/bin/python3

"""
This script contains the class definition of a State and an instance
Base = declarative_base(). The State class links to the MySQL table 'states'.

City class:
- Inherits from Base
- Links to the MySQL table 'cities'
- Has class attributes:
  - id: Represents a column of an auto-generated, unique integer,
  can’t be null and is a primary key
  - name: Represents a column of a string with a maximum of 128 characters
  and can’t be null

The script connects to a MySQL server running on localhost at port 3306.

Usage:
    Define the State class and connect to the database using SQLAlchemy.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey

Base = declarative_base()

class City(Base):
    """
    State class that links to the MySQL table 'states'.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
