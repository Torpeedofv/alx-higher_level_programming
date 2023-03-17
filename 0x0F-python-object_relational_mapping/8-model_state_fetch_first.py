#!/usr/bin/python3
from model_state import State, Base
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    count = session.query(State).count()
    if (count < 1):
        print("Nothing")
    else:
        states = session.query(State).order_by(State.id).first()
        print("{}: {}".format(states.id, states.name))
