#!/usr/bin/python3
"""changes the name of a state object from the database"""

from relationship_state import State, Base
from relationship_city import City, Base
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    ca = State(name='California')
    sf = City(name='San Francisco')
    ca.cities.append(sf)
    session.add(ca)
    session.commit()
    session.close()
