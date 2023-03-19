#!/usr/bin/python3
"""Adds the state object to the database"""

from model_state import State, Base
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    obj = State(name='Louisiana')
    states = session.add(obj)
    session.commit()
    print(obj.id)
