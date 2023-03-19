#!/usr/bin/python3
"""contains the definition of a city and an instance"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

Base = declarative_base()


class City(Base):
    """creation of an instance of Base"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
