#!/usr/bin/python3
"""contains the definition of a state and an instance"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """creation of an instance of Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,\
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
