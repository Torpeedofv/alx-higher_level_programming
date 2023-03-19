#!/usr/bin/python3
"""contains the definition of a state and an instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """creation of an instance of Base"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref="state", cascade='all, delete')
