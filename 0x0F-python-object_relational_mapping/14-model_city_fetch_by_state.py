#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    cities = session.query(City.name, City.id, State.name)\
        .join(State, State.id == City.state_id).order_by(City.id).all()
    for city, city_id, state_name in cities:
        print("{}: ({}) {}".format(state_name, city_id, city))
